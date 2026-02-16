#!/usr/bin/env python3

from math import ceil
import sys
from io import BytesIO
from pathlib import Path
from typing import IO
from PIL import Image, ImageOps


MS_PER_FRAME = 1000 / 36


def decode_bytes(data: IO[bytes], length: int = -1):
	out = BytesIO()
	b = data.read(1)
	while b and length:
		if b == b"\xf9":
			out.write(b"\0" * (data.read(1)[0] + 1))
		elif b == b"\xfb":
			out.write(data.read(1) * (data.read(1)[0] + 1))
		else:
			out.write(b)
		b = data.read(1)
		length -= 1

	# Flip and copy last 11 tiles
	out.seek(-88, 1)
	for a in out.read():
		b = 0
		if a & 0x80: b |= 0x01
		if a & 0x40: b |= 0x02
		if a & 0x20: b |= 0x04
		if a & 0x10: b |= 0x08
		if a & 0x08: b |= 0x10
		if a & 0x04: b |= 0x20
		if a & 0x02: b |= 0x40
		if a & 0x01: b |= 0x80
		out.write(b.to_bytes())

	out.seek(0)
	return out.read()


def to_image(data: bytes):
	return ImageOps.invert(Image.frombytes("1", (8, len(data)), data).rotate(90, expand=True))


def to_mapped(img: Image.Image, map: list[int]):
	max_idx = img.width // 8
	out = Image.new("1", (12 * 8, len(map) // 12 * 8))
	for i, idx in enumerate(map):
		if idx >= max_idx:
			idx = max_idx
		y, x = divmod(i, 12)
		left = 8 * idx
		out.paste(
			img.crop((left, 0, left + 8, 8)),
			((x * 8, y * 8))
		)
	return out


if __name__ == "__main__":
	if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "/?"):
		print(f"Usage: {sys.argv[0]} bios.min")
	
	in_file = Path(sys.argv[1])
	if len(sys.argv) < 3:
		out_folder = in_file.with_suffix("")
	else:
		out_folder = Path(sys.argv[2])
	out_folder.mkdir(exist_ok=True)

	with in_file.open("rb") as f:
		f.seek(0x0e22)
		battery_frame_info = list[tuple[int, int]]()
		frame_data = f.read(20)
		footer = f.read(2)
		assert footer[1] >> 1 == 20
		battery_total_frames = ((footer[1] & 1) << 8) | footer[0]
		for off, extra in zip(frame_data[18::-2], frame_data[19::-2]):
			addr = ((extra & 1) << 8) | off
			battery_frame_info.append((addr, extra >> 1))

		insert_cart_frame_info = list[tuple[int, int]]()
		frame_data = f.read(6)
		footer = f.read(2)
		assert footer[1] >> 1 == 6
		insert_cart_total_frames = ((footer[1] & 1) << 8) | footer[0]
		for off, extra in zip(frame_data[4::-2], frame_data[5::-2]):
			addr = ((extra & 1) << 8) | off
			insert_cart_frame_info.append((addr, extra >> 1))

		data = decode_bytes(f)
		used_data = [False] * len(data)

		def get_data(start: int, length: int=0):
			start -= 0x1530
			for x in range(start, start+length if length else len(data)):
				used_data[x] = True
			return data[start:start+length if length else None]

		with (out_folder / "decoded.bin").open("wb") as out:
			out.write(data)
			print(f"Wrote bytes to {out.name}")

		out_file = out_folder / "tileset.png"
		img_data = get_data(0x1830)
		tileset = to_image(img_data)
		tileset.save(out_file)
		print(f"Exported tileset to {out_file}")

		# Add an all-black tile
		tmp = Image.new("1", (tileset.width + 8, tileset.height))
		tmp.paste(tileset, (0, 0))
		tileset = tmp
		
		# Output mappings
		to_mapped(tileset, get_data(0x1530, 12*8)).save(out_folder / "map0_blank.png")
		to_mapped(tileset, get_data(0x1590, 12*8)).save(out_folder / "map1_game_select_outer.png")
		to_mapped(tileset, get_data(0x15f0, 12*8)).save(out_folder / "map2_game_select_inner.png")

		for fn, frame_info, total_frames in [
			("map3_battery.gif", battery_frame_info, battery_total_frames),
			("map4_insert_cart.gif", insert_cart_frame_info, insert_cart_total_frames),
		]:
			imgs = list[Image.Image]()
			durations = list[int]()
			frame_count = 0
			for addr, frames in frame_info:
				imgs.append(to_mapped(tileset, get_data(0x1650 + addr, 12*5)))
				frame_count += frames
				durations.append(frames * MS_PER_FRAME)
			img = imgs.pop(0)
			img.save(out_folder / fn,
				append_images=imgs,
				duration=durations,
				loop=ceil(total_frames / frame_count))

		print(f"Exported rendered tilemaps to {out_folder}")

		with (out_folder / "used.bin").open("wb") as out:
			out.write(b"".join(int(x).to_bytes() for x in used_data))
			print(f"Wrote accounting to {out.name}")
