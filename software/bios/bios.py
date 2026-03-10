from contextlib import contextmanager
from dataclasses import dataclass
import struct
import time


MEM = memoryview(bytearray(b"\0" * 0x200000))

def read2(addr: int, mem=MEM):
	return int.from_bytes(mem[addr:addr+2], "little")

def read3(addr: int, mem=MEM):
	return int.from_bytes(mem[addr:addr+3], "little")

def halt():
	""" HALT operation """

def jump_to_cart(addr: int):
	""" JRL to code on cartridge at addr """

def jump_to_ram(addr: int):
	""" JRL to code in RAM at addr """

class MemProxy:
	def ld(self, value):
		raise NotImplementedError

	def __bool__(self):
		return bool(int(self))

	def __int__(self):
		raise NotImplementedError

	def __index__(self):
		return int(self)

	def __add__(self, o):
		return int(self) + int(o)

	def __iadd__(self, o):
		self.ld(int(self) + int(o))

	def __and__(self, o):
		return int(self) & int(o)

	def __iand__(self, o):
		self.ld(int(self) & int(o))

	def __or__(self, o):
		return int(self) | int(o)

	def __ior__(self, o):
		self.ld(int(self) | int(o))

	def __xor__(self, o):
		return int(self) ^ int(o)

	def __ixor__(self, o):
		self.ld(int(self) ^ int(o))

	def __lt__(self, o):
		return int(self) < int(o)

	def __le__(self, o):
		return int(self) <= int(o)

	def __eq__(self, o):
		if isinstance(o, MemProxy):
			return self is o
		return int(self) == int(o)

	def __gt__(self, o):
		return int(self) > int(o)

	def __ge__(self, o):
		return int(self) >= int(o)

class Register(MemProxy):
	def __init__(
		self, 
		addr: int, 
		shift: int = 0, 
		mask: int = 0xff,
		invert: bool = False,
	):
		self.addr = addr
		self.shift = shift
		self.mask = mask
		self.invert = invert

	@classmethod
	def bit(cls, addr: int, bit: int, invert: bool = False):
		return cls(addr, bit, 1 << bit, invert)

	@classmethod
	def sized(cls, addr: int, shift: int, size: int):
		return cls(addr, shift, ((1 << size) - 1) << shift)

	def ld(self, value: int|bool):
		adjusted = (int(value) << self.shift)
		if self.invert:
			adjusted = ~adjusted
		adjusted &= self.mask
		addr = self.addr
		while adjusted:
			MEM[addr] = adjusted & 0xff
			adjusted >>= 8
			addr += 1

	def clear(self):
		""" Write 1 to strobe """
		self.ld(0)
	__call__ = clear  # for reset

	def __int__(self):
		mask = self.mask
		addr = self.addr
		res = 0
		shift = 0
		while mask:
			res |= (MEM[addr] << shift) >> self.shift
			mask >>= 8
			shift += 8
		return res

	def __invert__(self):
		return int(self) & self.mask

class RegisterMapper:
	def __setattr__(self, name: str, value):
		reg = getattr(self, name)
		if isinstance(reg, MemProxy):
			fn = getattr(self, f"set_{name}")
			reg.ld(fn(value)
				if callable(fn) and isinstance(value, str)
				else value)

class IRQ(RegisterMapper):
	def __init__(self, enable_addr: int, enable_bit: int):
		self.enabled = Register.bit(enable_addr, enable_bit)
		self.factor = Register.bit(enable_addr + 4, enable_bit)

class Console(RegisterMapper):
	awake = Register.bit(0x2001, 5)

	# Exactly what these disable and how is unclear
	timers_osc3 = Register.bit(0x2019, 5)
	timers_osc1 = Register.bit(0x2019, 4)
console = Console()

class LCD(RegisterMapper):
	""" LCD Controller, communication with Driver/LCD """
	default_contrast = Register(0x2000, 2, 0xFC)
	chip_enabled = Register.bit(0x2000, 0)

	# IRQs
	irq_priority = Register.sized(0x2020, 6, 2)
	copy_complete = IRQ(0x2023, 7)
	frame_divider_overflow = IRQ(0x2023, 6)

	# Renderer
	render_config = Register(0x2080)
	render = Register.bit(0x2080, 3)
	render_sprites = Register.bit(0x2080, 2)
	render_map = Register.bit(0x2080, 1)
	map_size = Register(0x2080, 4, 3 << 4)
	invert_map = Register.bit()
	frame_counter = Register.sized(0x2081, 4, 4)
	rate_divider = Register.sized(0x2081, 1, 3)
	initialized = Register.bit(0x2081, 0)
	tile_base = Register(0x2082, mask=0x1FFFF8)
	scroll_x = Register(0x2085, mask=0x7F)
	scroll_y = Register(0x2086, mask=0x7F)
	sprite_base = Register(0x2082, mask=0x1FFFC0)
	line_counter = Register(0x208A, mask=0x7F)

	def set_map_size(self, v: str):
		self.map_size.ld({
			"12 x 16": 0, "16 x 12": 1,
			"24 x 8": 2,  "24 x 16": 3,
		}[v])

	def set_rate_divider(self, v: str):
		self.rate_divider.ld({
			"1/3": 0, "1/6": 1, "1/9": 2, "1/12": 3,
			"1/2": 4, "1/4": 5, "1/6": 6, "1/8": 7,
		}[v])

	# Commands
	raw_ctrl = Register(0x20FE)
	raw_data = Register(0x20FF)

	def send_on(self): self.raw_ctrl = 0xAF
	def send_off(self): self.raw_ctrl = 0xAE
	def send_set_display_start_line(self, line: int):
		self.raw_ctrl = 0x40 | (line & 0x3F)
	def send_set_page(self, page: int):
		self.raw_ctrl = 0xB0 | (page & 0x0F)
	def send_set_column(self, col: int):
		self.raw_ctrl = 0x10 | ((col & 0x0F) >> 4)
		self.raw_ctrl = (col & 0x0F)
	def send_adc_normal(self): self.raw_ctrl = 0xA0
	def send_adc_reverse(self): self.raw_ctrl = 0xA1
	def send_invert_on(self): self.raw_ctrl = 0xA7
	def send_invert_off(self): self.raw_ctrl = 0xA6
	def send_set_all_on(self): self.raw_ctrl = 0xA5
	def send_set_all_off(self): self.raw_ctrl = 0xA4
	def send_lcd_bias(self, bias: str):
		if bias == "1/9": self.raw_ctrl = 0xA2
		elif bias == "1/7": self.raw_ctrl = 0xA3
		else: raise ValueError(bias)
	def send_rmw_start(self): self.raw_ctrl = 0xE0
	def send_end(self): self.raw_ctrl = 0xEE
	def send_reset(self): self.raw_ctrl = 0xE2
	def send_set_row_direction_normal(self): self.raw_ctrl = 0xC0
	def send_set_row_direction_reverse(self): self.raw_ctrl = 0xC8
	def send_set_power(self, v: int):
		self.raw_ctrl = 0x28 | (v & 7)
	def send_set_resistor_ratio(self, v: int):
		self.raw_ctrl = 0x20 | (v & 7)
	def send_set_contrast(self, c: int):
		self.raw_ctrl = 0x81
		self.raw_ctrl = c & 0x3F
	def send_static_indicator(self, m: int):
		if m:
			self.raw_ctrl = 0xAD
			self.raw_ctrl = m & 3
		else:
			self.raw_ctrl = 0xAC
	def send_nop(self): self.raw_ctrl = 0xE3
	def send(self, data: int): self.raw_data = data
lcd = LCD()

class Cartridge(RegisterMapper):
	chip_enabled = Register.bit(0x2000, 1)

	multicart_mode = Register.bit(0x2001, 3)
	multicart_game_id = Register.sized(0x2001, 0, 3)
	autoboot_slot_0 = Register.bit(0x2001, 0)

	# IRQs
	irq_priority = Register.sized(0x2021, 4, 2)
	ejected = IRQ(0x2024, 1)
	irq = IRQ(0x2024, 0)
	detect_edge = Register.bit(0x2051, 1)
	irq_edge = Register.bit(0x2051, 0)  # idk maybe

	inserted = Register.bit(0x2053, 1, invert=True)
	ctk = Register.sized(0x2055, 0, 3)
	powered = Register.bit(0x2071, 2, invert=True)
cartridge = Cartridge()

OSC1 = 0
OSC3 = 1
class CPU(RegisterMapper):
	osc = Register.bit(0x2002, 3)
	osc3_enabled = Register.bit(0x2002, 2)
	vdc = Register.sized(0x2002, 0, 2)

	# Registers that don't really make sense in Python
	SC = 0
	SP = 0
cpu = CPU()

class SVD(RegisterMapper):
	criteria_voltage = Register.sized(0x2010, 0, 4)
	on = Register.bit(0x2010, 4)
	voltage_low = Register.bit(0x2010, 5)
svd = SVD()

class SecondsTimer(RegisterMapper):
	enabled = Register.bit(0x2008, 0)
	reset = Register.bit(0x2008, 1)
	counter = Register(0x2009, mask=0xFFFFFF)
seconds_timer = SecondsTimer()

class PTM(RegisterMapper):
	def __init__(self, hi: bool, psc_addr: int, control_addr: int, irq_bit: int|None):
		self.clocked = Register.bit(psc_addr, 7 if hi else 3)
		self.prescaler = Register.sized(psc_addr, 4 if hi else 0, 3)
		self.osc = Register.bit(psc_addr + 1, int(hi))

		self.ptout = Register.bit(control_addr, 3)
		self.running = Register.bit(control_addr, 2)
		self.reset = Register.bit(control_addr, 1)
		self.external_clock = Register.bit(control_addr, 0)
		self.preset = Register(control_addr + 2)
		self.compare_data = Register(control_addr + 4)
		self.count = Register(control_addr + 6)

		self.underflow: IRQ|None = None
		self.compare_match: IRQ|None = None
		if irq_bit is not None:
			self.underflow = IRQ(0x2023, irq_bit)

	@classmethod
	def hi(cls, psc_addr: int, control_addr: int, irq_bit: int|None = None):
		return cls(True, psc_addr, control_addr, irq_bit)

	@classmethod
	def lo(cls, psc_addr: int, control_addr: int, irq_bit: int|None = None):
		return cls(False, psc_addr, control_addr, irq_bit)

class PTM16(RegisterMapper):
	def __init__(self, control_addr: int):
		self.mode16 = Register.bit(control_addr, 7)
		self.preset = Register(control_addr + 2, mask=0xFFFF)
		self.compare_data = Register(control_addr + 4, mask=0xFFFF)
		self.count = Register(control_addr + 6, mask=0xFFFF)

class ProgrammableTimerA(PTM16):
	ptm1 = PTM.hi(0x2018, 0x2030, 3)
	ptm0 = PTM.lo(0x2018, 0x2031, 2)
	irq_priority = Register.sized(0x2021, 2, 2)
ptm_a = ProgrammableTimerA(0x2030)

class ProgrammableTimerB(RegisterMapper):
	ptm3 = PTM.hi(0x201A, 0x2038, 5)
	ptm2 = PTM.lo(0x201A, 0x2039, 4)
	irq_priority = Register.sized(0x2021, 4, 2)
ptm_b = ProgrammableTimerB(0x2038)

class ProgrammableTimerC(RegisterMapper):
	ptm5 = PTM.hi(0x201C, 0x2048, 1)
	ptm5.compare_match = IRQ(0x2020, 0)
	ptm4 = PTM.lo(0x201C, 0x2049)
	irq_priority = Register.sized(0x2021, 0, 2)
ptm_c = ProgrammableTimerC(0x2048)

class ClockTimer(RegisterMapper):
	reset = Register.bit(0x2040, 1)
	enabled = Register.bit(0x2040, 0)
	count = Register(0x2041)
	hz32 = IRQ(0x2024, 5)
	hz8 = IRQ(0x2024, 4)
	hz2 = IRQ(0x2024, 3)
	hz1 = IRQ(0x2024, 2)
	irq_priority = Register.sized(0x2021, 6, 2)
clock_timer = ClockTimer()

RISING = 0
FALLING = 1
class Key(RegisterMapper):
	def __init__(self, bit: int):
		self.edge = Register.bit(0x2050, bit)
		self.data = Register.bit(0x2052, bit)
		self.pressed = Register.bit(0x2052, bit, invert=True)
		self.irq = IRQ(0x2025, bit)

class Keypad(RegisterMapper):
	power = Key(7)
	right = Key(6)
	left = Key(5)
	down = Key(4)
	up = Key(3)
	c = Key(2)
	b = Key(1)
	a = Key(0)
	keys = [power, right, left, down, up, c, b, a]
	all = Register(0x2052)
	ctk = Register(0x2054, mask=0x77)
	ctk_lo = Register(0x2054, mask=0x07)
	ctk_hi = Register(0x2054, mask=0x70)
	irq_priority = Register.sized(0x2021, 2, 2)
keypad = Keypad()

INPUT = 0
OUTPUT = 1
class Port(RegisterMapper):
	irq: IRQ|None = None

	def __init__(self, bit: int):
		self.direction = Register.bit(0x2060, bit)
		self.data = Register.bit(0x2061, bit)

class IO(RegisterMapper):
	unknown = Port(7)
	shock = Port(6)
	shock.irq = IRQ(0x2026, 6)
	ir_disable = Port(5)
	rumble = Port(4)
	eeprom_clock = Port(3)
	eeprom_data = Port(2)
	ir_txd = Port(1)
	ir_rxd = Port(0)
	ir_rxd.irq = IRQ(0x2026, 7)
	irq_priority = Register.sized(0x2022, 0, 2)
io = IO()

class Audio(RegisterMapper):
	mute = Register.sized(0x2070, 0, 2)  # TODO: real purpose?
	volume = Register.sized(0x2071, 0, 2)
audio = Audio()

class Unknown(RegisterMapper):
	r01_7 = Register.bit(0x2001, 7)
	r01_6 = Register.bit(0x2001, 6)
	r01_4 = Register.bit(0x2001, 4)
	r02_7 = Register.bit(0x2002, 7)
	r02_6 = Register.bit(0x2002, 6)
	r02_5 = Register.bit(0x2002, 5)
	r02_4 = Register.bit(0x2002, 4)
	r44 = Register(0x2044)
	r45 = Register(0x2045)
	r46 = Register(0x2046)
	r47 = Register(0x2047)
	r62 = Register(0x2062)
	r70 = Register.bit(0x2070, 2)

	irq_22 = IRQ(0x2026, 5)
	irq_24 = IRQ(0x2026, 4)

	irq_3A = IRQ(0x2026, 2)
	irq_3C = IRQ(0x2026, 1)
	irq_3E = IRQ(0x2026, 0)
	irq_priority = Register.sized(0x2021, 0, 2)
unknown = Unknown()

class Location(MemProxy):
	def __init__(self, addr, size_bytes: int = 1):
		self.addr = addr
		self.size = size_bytes

	@property
	def end(self):
		return self.addr + self.size

	def ld(self, value: bytes|int):
		if isinstance(value, int):
			value = value.to_bytes(self.size, "little")
		MEM[self.addr:self.addr + len(value)] = value

	def get(self):
		return MEM[self.addr:self.end]

	def __getitem__(self, key: int):
		return MEM[self.addr + key]

	def __setitem__(self, key: int, value: bytes|int):
		if isinstance(value, bytes):
			assert len(value) == 1
			value = value[0]
		MEM[self.addr + key] = value

	def __int__(self):
		assert 0 < self.size <= 3
		return int.from_bytes(self.get(), "little")

	def __eq__(self, o) -> bool:
		if isinstance(o, bytes):
			return bytes(self.get()) == o
		if isinstance(o, MemProxy):
			return self is o
		assert 0 < self.size <= 3
		n2 = int(o)
		if n2 < 0:
			n1 = int.from_bytes(self.get(), "little", signed=True)
			return n1 == n2
		return int(self) == n2

class RAM(RegisterMapper):
	""" Not actually registers just named RAM """
	remaining_plays = Location(0x14E0)
	key_pad = Location(0x14E1)
	num_game_structs = Location(0x14E2)
	loop_n = Location(0x14E3)
	game_structs = Location(0x14E4, 64)
	next_game_struct = Location(0x1524, 2)
	next_tile_pos = Location(0x1526, 2)
	current_row_start = Location(0x1528)
	final_name_row_start_min48 = Location(0x1529)
	final_name_row_start = Location(0x152A)
	move_cooldown = Location(0x152B)
	key_history = Location(0x152C)
	total_anim_frames = Location(0x152D, 2)
	frames_remaining = Location(0x152F)
	blank_tilemap = Location(0x1530, 96)
	game_select_map = Location(0x1590, 96)
	game_names_map = Location(0x15F0, 96)
	insert_cart_maps = Location(0x1650, 180)
	low_battery_maps = Location(0x1740, 300)
	tileset_base = Location(0x1830, 328)
	v_flip_start = 0x1920
	v_flipped_tiles = Location(0x1978, 88)
	game_name_tiles = Location(0x19D0, 576)
ram = RAM()

@dataclass
class KeyData:
	pressed: bool
	newly_pressed: bool

class KeypadData:
	def __init__(self, pressed: int|MemProxy, newly_pressed: int|MemProxy):
		kd = lambda m: KeyData(bool(pressed & m), bool(newly_pressed & m))
		self.power = kd(0x80)
		self.right = kd(0x40)
		self.left = kd(0x20)
		self.down = kd(0x10)
		self.up = kd(0x08)
		self.c = kd(0x04)
		self.b = kd(0x02)
		self.a = kd(0x01)
		self.pressed = pressed
		self.newly_pressed = newly_pressed


@contextmanager
def suppress_interrupts():
	""" Set interrupt flags to NMI only """
	SC = cpu.SC
	cpu.SC = 0xC0
	yield
	cpu.SC = SC

# BIOS code
def _reset_vector():
	""" Stage 0 of boot: Hard reset """
	seconds_timer.reset()
	seconds_timer.enabled = True
	lcd.default_contrast = 31  # 50%
	unknown.r02_7 = \
		unknown.r02_6 = \
		unknown.r02_5 = \
		unknown.r02_4 = \
		cpu.vdc = 0
	cpu.osc = OSC1
	cpu.osc3_enabled = False
	return _reset2()

def _reset2():
	""" Stage 1 of boot: Soft reset """
	with suppress_interrupts():
		# Initialize things, mostly to 0
		cpu.SP = 0x2000  # initial stack location
		initregs()
		lcd.render_config = 0
		#NB = CB = 0x01
		# Start booting up and configuring hardware
		ram.key_pad = keypad.all
		cartridge.chip_enabled = \
			lcd.chip_enabled = True
		unknown.r02_7 = unknown.r02_6 = 1
		init_io()
		lcd.render_map = True
		lcd.rate_divider = "1/2"
		lcd.tile_base = ram.tileset_base.addr
		lcd.scroll_x = lcd.scroll_y = 0
		lcd.sprite_base = 0
		power_cart()
		wait_8000_cycles()
		cartridge.ejected.enabled = True
	cpu.SC = 0x80

	# Clear visible portion LCD RAM
	lcd.send_nop()
	for page in range(0, 8):
		lcd.send_set_page(page)
		lcd.send_set_column(0)
		for _ in range(0, 96):
			lcd.send(0)

	apply_default_contrast()
	init_display(wait=True)
	decode_picture()
	if not cartridge.inserted:
		# TODO: how does this continue from pa__return?
		return insert_cart_screen()
	
	# Check voltage
	svd.on = 1
	time.sleep(0.0005)  # 202 cycles, TODO: calculate for real
	svd.on = 0
	if svd.voltage_low:
		low_battery_screen()
	return check_cart_type()

def nintendo_check():
	""" Stage N of boot """
	cpu.SP = 0x2000
	addr_on_cart = 0x21A4
	nintendo_string = "NINTENDO"
	string_on_cart = MEM[addr_on_cart : addr_on_cart + len(nintendo_string)]
	if string_on_cart != nintendo_string:
		return insert_cart_screen()

	# Reinitialize
	lcd.render_config = 0
	lcd.rate_divider = "1/12"
	lcd.tile_base = 0
	unknown.r01_4 = 0
	initregs()

	# Clear RAM
	for addr in range(0x1000, 0x2000):
		MEM[addr] = 0
	
	# Clear registers EXCEPT BA
	#IX = BR = HL = 0
	BA = (ram.key_pad, ram.remaining_plays)
	cpu.SC &= 0xC0  # keep only interrupt flags
	return jump_to_cart(0x2102, BA)

def initregs():
	BR = 0x20  # where the registers are, for [BR:ll] addressing
	# Zero general purpose stuff
	BA = EP = XP = YP = HL = IX = IY = 0

def init_io():
	svd.criteria_voltage = 8
	console.timers_osc3 = console.timers_osc1 = False
	lcd.irq_priority = \
		ptm_a.irq_priority = \
		ptm_b.irq_priority = \
		ptm_c.irq_priority = \
		clock_timer.irq_priority = \
		keypad.irq_priority = \
		unknown.irq_priority = \
		io.irq_priority = 0
	cartridge.irq_priority = 2
	clock_timer.enabled = False
	unknown.r44 = 0
	for key in keypad.keys:
		key.edge = FALLING  # on-press
	cartridge.detect_edge = \
		cartridge.irq_edge = RISING  # ejected
	keypad.ctk_lo = 1
	cartridge.ctk = 1

	io.eeprom_clock.direction = \
		io.eeprom_data.direction = OUTPUT
	io.eeprom_data.data = 0
	io.eeprom_clock.data = 1
	io.eeprom_data.data = 1
	io.shock.data = \
		io.rumble.data = \
		io.eeprom_clock.data = \
		io.eeprom_data.data = \
		io.ir_txd.data = \
		io.ir_rxd.data = 0
	io.ir_disable.data = 1
	io.ir_disable.direction = \
		io.rumble.direction = \
		io.ir_txd.direction = OUTPUT
	io.unknown = \
		io.shock.direction = \
		io.eeprom_clock.direction = \
		io.eeprom_data.direction = \
		io.ir_rxd = INPUT
	unknown.r62 = 0
	unknown.r70 = 0
	audio.mute = 0
	cartridge.powered = True
	audio.volume = 0

def _prc_frame_copy_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2108)

def _prc_render_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x210E)

def _timer_2h_underflow_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2114)

def _timer_2l_underflow_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x211A)

def _timer_1h_underflow_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2120)

def _timer_1l_underflow_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2126)

def _timer_3h_underflow_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x212C)

def _timer_3_cmp_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2132)

def _timer_32hz_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2138)

def _timer_8hz_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x213E)

def _timer_2hz_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2144)

def _timer_1hz_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x214A)

def _ir_rx_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2150)

def _shake_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2156)

def _cartridge_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x219E)

def _key_right_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2162)

def _key_left_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2168)

def _key_down_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x216E)

def _key_up_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2174)

def _key_c_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2180)

def _key_a_irq():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2186)

def _unknown_irq0():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x218C)

def _unknown_irq1():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2192)

def _unknown_irq2():
	if not console.awake:
		wake_from_irq()
	return jump_to_cart(0x2198)

def wake_from_irq():
	if cpu.osc == OSC1:
		with suppress_interrupts():
			enter_high_speed_operation()
	if not cartridge.powered and unknown.r02_6:
		with suppress_interrupts():
			power_cart()
			if unknown.r01_6:
				prepare_selected_game()
	if unknown.r01_7:
		# modifies the stack to remove the call to wake_from_irq
		# so that the IRQ won't go to software, just to this
		# RAM address, and the stack is restored to pre-IRQ state
		cpu.SC += 3
		return jump_to_ram(0x1FFD)  # last 3 bytes of RAM
	with suppress_interrupts():
		prepare_selected_game()
		console.awake = True
	return

def _key_power_irq():
	if not console.awake:
		if unknown.r01_4:
			return _reset2()
		# same as in wake_from_irq
		if cpu.osc == OSC1:
			with suppress_interrupts():
				enter_high_speed_operation()
		if not cartridge.powered and unknown.r02_6:
			with suppress_interrupts():
				power_cart()
				if unknown.r01_6:
					prepare_selected_game()
		# differs
		if unknown.r01_7 and not unknown.r02_5:
			return jump_to_ram(0x1FFD)  # last 3 bytes of RAM
		if not unknown.r01_7:
			# same as in wake_from_irq
			with suppress_interrupts():
				prepare_selected_game()
				console.awake = True
		if unknown.r02_5:
			keypad.power.irq.factor.clear()
			return
	return jump_to_cart(0x215C)  # software handler

def prepare_selected_game():
	if cartridge.multicart_mode:
		game_id = cartridge.multicart_game_id
	elif cartridge.autoboot_slot_0:
		game_id = 0
	else:
		return
	flash_select_bank(7, 0)
	flash_prepare_game(game_id)

def _cart_eject_irq():
	if console.awake or unknown.r01_4:
		return _reset2()
	if cpu.osc == OSC1:
		with suppress_interrupts():
			enter_high_speed_operation()
	if not unknown.r01_7 or unknown.r01_6:
		return _shutdown()
	if not cartridge.powered and unknown.r02_6:
		with suppress_interrupts():
			power_cart()
	return jump_to_ram(0x1FFD)  # last 3 bytes of RAM

def _flash_read_ids():
	""" Return in BA """
	with suppress_interrupts():
		flash_begin_cmd()
		MEM[0x5555] = 0x90
		return MEM[0x2100], MEM[0x2101]
flash_read_ids = _flash_read_ids

def _flash_reset():
	with suppress_interrupts():
		flash_begin_cmd()
		MEM[0x5555] = 0xF0
flash_reset = _flash_reset

def _flash_program_byte(addr: int, byte: int):
	""" Address in XP:IX, byte in A """
	with suppress_interrupts():
		flash_begin_cmd()
		MEM[0x5555] = 0xA0
		MEM[addr] = byte
		for _ in range(8):
			if MEM[addr] != byte:
				continue
			if MEM[addr] != byte:
				continue
			return 0
		return -1
flash_program_byte = _flash_program_byte

def _flash_erase_sector(sector: int):
	""" Sector address in XP:IX"""
	with suppress_interrupts():
		flash_begin_cmd()
		MEM[0x5555] = 0x80
		MEM[0x5555] = 0xAA
		MEM[0x2AAA] = 0x55
		MEM[sector] = 0x30
		for _ in range(5001):
			if MEM[sector] != 0xFF:
				continue
			if MEM[sector] != 0xFF:
				continue
			return 0
		return -1
flash_erase_sector = _flash_erase_sector

def _flash_enter_bank_select_mode():
	""" Sector address in XP:IX"""
	with suppress_interrupts():
		flash_begin_cmd()
		MEM[0x5555] = 0xD0
flash_enter_bank_select_mode = _flash_enter_bank_select_mode

def _flash_select_bank(page: int, bank: int):
	""" Sector address in XP:IX"""
	with suppress_interrupts():
		flash_enter_bank_select_mode()
		MEM[(page << 16) | 0xFFFF] = bank
		flash_reset()
flash_select_bank = _flash_select_bank

def _flash_allow_remapping_page_0(bank: int):
	with suppress_interrupts():
		flash_begin_cmd()
		MEM[0x5555] = 0xC9
		MEM[0x5555] = bank
flash_allow_remapping_page_0 = _flash_allow_remapping_page_0

def _flash_remap_ids():
	with suppress_interrupts():
		flash_begin_cmd()
		MEM[0x5555] = 0xC0
flash_remap_ids = _flash_remap_ids

def _flash_prepare_game(game_id: int):
	with suppress_interrupts():
		# Reading from external page 1, which
		# should have been remapped (to bank 0)
		# before calling this.
		addr = 0x041048 + game_id * 0x60
		external_page_0_bank = MEM[addr]
		if external_page_0_bank < 8:
			flash_allow_remapping_page_0(external_page_0_bank)
		bank_mappings = list(MEM[addr:addr + 8])
		flash_enter_bank_select_mode()
		for addr, bank in zip(range(0x03FFFF, 0x23FFFF, 0x040000), bank_mappings):
			MEM[addr] = bank
		flash_reset()
flash_prepare_game = _flash_prepare_game

def flash_begin_cmd():
	MEM[0x5555] = 0xAA
	MEM[0x2AAA] = 0x55

def flash_detect():
	""" Return True if Z=0 """
	b, a = MEM[0x5555], MEM[0x2AAA]
	MEM[0x2AAA] = 0xFF
	MEM[0x2AAA] = 0xFF
	flash_reset()
	flash_remap_ids()
	ba = flash_read_ids()
	flash_reset()
	is_expected_flash = ba == 0xBFD9
	if not is_expected_flash:
		MEM[0x5555] = b
		MEM[0x2AAA] = a
	a = MEM[0x2AAA]
	return is_expected_flash

def check_cart_type():
	""" Stage 2 of boot: check boot method """
	if flash_detect():
		# Remap external page 1 (internal page 4~7
		# inclusive) to bank 0, then read from it.
		flash_select_bank(7, 0)
		startup_action = MEM[0x041300]
		if startup_action & 2:
			if startup_action & 1:
				# Startup action 3
				start = ram.game_name_tiles.addr
				end = ram.game_name_tiles.end
				for ix in range(start, end):
					MEM[ix] = 0
				ram.num_game_structs = 0
				ram.next_game_struct = ram.game_structs.addr
				ram.next_tile_pos = start

				# starting at type byte for entry 0
				iy = 0x041050 - 96
				for loop_n in range(8):
					# done in ram.loop_n but only used here so don't care
					iy += 96
					a = MEM[iy]
					if a and a != 0xff:
						if a != 0xfe:
							ix = iy + 1
							if MEM[ix] & 0x80 == 0:
								if not flash_program_byte(ix - 1, 0):
									return insert_cart_screen()
								continue
							# Find the first 0 bit within 15 bytes
							# reading bits MSB -> LSB
							l = 0
							mask = 0x80
							for ix in range(ix, ix + 15):
								idx = f"{MEM[ix]:08b}".find("0")
								if idx >= 0:
									# mask has a 1 where the first 0 is
									mask = 1 << (7 - idx)
									l += idx
									break
								l += 8
							# rolls mask left and checks vs 0x01 but that's annoying
							if mask == 0x80:
								ix -= 1
								b = 0xFE # include cpl
							else:
								b = (~mask) & 0xFF
							b &= MEM[ix]
							a = l - 1
						# loc_0x0688
						ram.num_game_structs += 1
						hl = ram.next_game_struct
						MEM[hl:hl + 5] = struct.pack(
							"<BBBH",
							int(loop_n),
							a,
							b,
							ix
						)
						ram.next_game_struct = hl + 8
						hl = ram.next_tile_pos
						ix = iy - 80
						# loc_0x06B2
						for b in range(72, 0, -1):
							MEM[hl] = MEM[ix]
							hl += 1
							ix += 1
						ram.next_tile_pos = hl
				if not ram.num_game_structs:
					return insert_cart_screen()
				# loc_0x06D6
				cartridge.multicart_mode = 1
				return game_select_screen()
				# loc_0x0C0E
			else:
				# Startup action 2
				flash_prepare_game(0)
				cartridge.autoboot_slot_0 = 1
		else:
			# Startup action 0 or 1
			# page 04 maps to 00 on cart
			ram.remaining_plays = jump_to_cart(0x041400)
			return nintendo_check()
	ram.remaining_plays = -1
	return nintendo_check()

def run_selected_game(loaded_game_id: int):
	addr = ram.game_structs.addr + loaded_game_id * 8
	game_id = MEM[addr]
	ram.remaining_plays = MEM[addr + 1]
	if ram.remaining_plays != -2:
		new_remaining_plays = MEM[addr + 2]
		write_addr = 0x040000 | read2(addr + 3)
		if flash_program_byte(write_addr, new_remaining_plays) != 0:
			return insert_cart_screen()
	cartridge.multicart_game_id = game_id
	flash_prepare_game(game_id)
	return nintendo_check()

def _suspend_system():
	with suppress_interrupts(), set_br():
		unknown.r02_5 = 1
		# Back up registers that will be changed
		backup_lcd = int(lcd.render_config)
		backup_kp_polarity = [int(k.edge) for k in keypad.keys]
		backup_kp_priority = int(keypad.irq_priority)
		irqs_enabled = MEM[0x2023:0x2027]
		do_shutdown()
		# after resuming...
		lcd_on()
		unknown.r02_5 = 0
		MEM[0x2023:0x2027] = irqs_enabled
		if unknown.r01_6:
			cartridge.ejected.enabled = True
		keypad.irq_priority = backup_kp_priority
		for k, e in zip(keypad.keys, backup_kp_polarity):
			k.edge = e
		lcd.render_config = backup_lcd

def do_shutdown():
	"""
	part of _suspend_system but is called directly
	by _shutdown, which sets things up so that the
	system restarts before hitting the resume code
	"""
	for k in keypad.keys:
		k.edge = RISING
	keypad.power.edge = FALLING
	MEM[0x2023:0x2027] = b"\0\0\0\0"  # disable all IRQs
	keypad.power.irq.enabled = True
	keypad.irq_priority = 3
	wait_8000_cycles()
	keypad.power.irq.factor.clear()
	halt_cpu_and_lcd(2)

def _sleep():
	with suppress_interrupts(), set_br():
		halt_cpu_and_lcd(1)

def _sleep_with_display():
	with suppress_interrupts(), set_br():
		lcd.render = False
		halt_cpu(1)

def _shutdown():
	with suppress_interrupts(), set_br():
		cpu.SP = 0x2000
		init_io()
		return shutdown()

def shutdown():
	with suppress_interrupts():
		unknown.r01_7 = unknown.r01_4 = 1
		return do_shutdown()

def _sleep2():
	with set_br(), suppress_interrupts():
		halt_cpu_and_lcd(1)

def halt_cpu_and_lcd(interrupt_flags):
	lcd_off()
	return halt_cpu(interrupt_flags)

def halt_cpu(interrupt_flags):
	if not unknown.r01_7 or unknown.r01_6:
		cartridge.ejected.enabled = True
		cartridge.irq_priority = 3
	cartridge.detect_edge = RISING  # ejected
	cartridge.ctk = 1
	console.awake = False
	unpower_cart()
	enter_low_speed_operation()
	cpu.SC = interrupt_flags << 6
	halt()
	cpu.SC = 3 << 6  # NMI-only

def _default_contrast(contrast: int):
	lcd.default_contrast = contrast
	set_temp_contrast(get_default_contrast())
default_contrast = _default_contrast

def _change_contrast(up: bool):
	contrast = get_default_contrast()
	if up:
		if contrast == 63:
			return -1
		contrast += 1
	elif contrast == 0:
		return -1
	else:
		contrast -= 1
	default_contrast(contrast)
	return 0

def _apply_default_contrast():
	set_temp_contrast(get_default_contrast())
apply_default_contrast = _apply_default_contrast

def _get_default_contrast():
	return int(lcd.default_contrast)
get_default_contrast = _get_default_contrast

def _set_temp_contrast(contrast: int):
	render = bool(lcd.render)
	lcd.render = False
	lcd.send_set_contrast(contrast)
	if render:
		lcd.render = True
set_temp_contrast = _set_temp_contrast

def _lcd_on():
	with set_br():
		lcd_on()

def lcd_on():
	with suppress_interrupts():
		unknown.r02_4 = cpu.osc3_enabled
		lcd.initialized = True
		init_display(wait=True)

def _reset_lcd():
	with set_br():
		init_display(wait=False)

# init_display_without_wait == init_display(wait=False)
def init_display(wait: bool):
	with suppress_interrupts():
		if not lcd.initialized:
			return
		render = bool(lcd.render)
		lcd.render = False
		lcd.send_nop()
		lcd.send_set_all_off()
		lcd.send_static_indicator(2)
		lcd.send_end()
		lcd.send_set_display_start_line(0)
		lcd.send_lcd_bias("1/9")
		lcd.send_adc_normal()
		lcd.send_set_row_direction_normal()
		lcd.send_invert_off()
		lcd.send_set_power(7)
		if wait:
			if cpu.osc == OSC1:
				time.sleep(...)  # wait 5711 cycles
			else:
				time.sleep(...)  # wait 349978 cycles
		lcd.send_on()
		lcd.render = render

def _lcd_off():
	with set_br():
		lcd_off()

def lcd_off():
	lcd.render = False
	lcd.send_off()
	lcd.send_static_indicator(0)
	lcd.send_set_power(0)
	lcd.send_set_all_on()  # sleep mode
	lcd.initialized = False

def _ena_ram_vec():
	# TODO: rename
	with set_br(), suppress_interrupts():
		if not unknown.r01_7:
			unknown.r01_7 = 1
			unknown.r01_6 = 1
			console.awake = 0

def _dis_ram_vec():
	# TODO: rename
	with set_br():
		if unknown.r01_6:
			cartridge.ctk = 1
			cartridge.irq_edge = RISING
			with suppress_interrupts():
				cartridge.irq_priority = 3
				cartridge.ejected.enabled = True
				console.awake = True
				unknown.r01_6 = False
				unknown.r01_7 = False

def _disable_cart_eject_irq_if():
	with set_br():
		if unknown.r01_6:
			cartridge.ejected.enabled = False

def _enable_cart_eject_irq_if():
	with set_br():
		if unknown.r01_6:
			cartridge.ejected.enabled = True

# skip_if_01_not_bit6 has been integrated in place

def _unknown_eject1():
	with set_br(), suppress_interrupts():
		if not unknown.r01_7:
			cartridge.ejected.enabled = False
			unknown.r01_7 = True
			console.awake = False

def _unknown_eject2():
	with set_br():
		if unknown.r01_7 or not unknown.r01_6:
			cartridge.ctk = 1
			cartridge.irq_edge = RISING
			with suppress_interrupts():
				cartridge.irq_priority = 3
				cartridge.ejected.enabled = True
				console.awake = True
				unknown.r01_7 = False

def _dev_card0() -> int|None:
	""" Returns in A """
	with suppress_interrupts(), set_br():
		if unknown.r01_7 or not unknown.r01_6:
			if not cartridge.inserted:
				return 1
			backup_lcd = int(lcd.render_config)
			lcd.render_config = 0
			backup_power = bool(cartridge.powered)
			wait_8000_cycles()
			cartridge.ejected.factor.clear()
			class Return2(Exception): pass
			try:
				if select_boot():
					if not cartridge.multicart_mode:
						raise Return2("expected multicart")
					addr = 0x041050 + cartridge.multicart_game_id * 96
					playability = MEM[addr]
					if playability in (0x00, 0xff):
						raise Return2("empty or erased")
					flash_prepare_game(cartridge.multicart_game_id)
				elif cartridge.multicart_mode:
					raise Return2("unexpected multicart")
			except Return2:
				cartridge.powered = backup_power
				return 2
			unknown.r02_6 = 1
			lcd.render_config = backup_lcd
			return 0
	return None  # does not alter A

def _dev_card1() -> int|None:
	with suppress_interrupts(), set_br():
		if unknown.r01_7 or not unknown.r01_6:
			backup_lcd = lcd.render_config
			lcd.render_config = 0
			if not cartridge.inserted:
				return 1
			cart_slot_on()
			if select_boot():
				flash_select_bank(0x07, 0x01)
				result = -1
			else:
				result = 0
			lcd.render_config = backup_lcd
			return result
	return None

# skip_if_01_bit6_or_not_bit7 has been integrated in place

def select_boot():
	if flash_detect():
		flash_select_bank(0x07, 0x00)
		startup_action = MEM[0x041300]
		if startup_action & 1:
			return startup_action
		flash_prepare_game(0)
	return 0

def _enable_cart_eject_irq(priority: int):
	with set_br(), suppress_interrupts():
		cartridge.irq_priority = priority
		cartridge.ctk = 1
		cartridge.irq_edge = RISING
		wait_8000_cycles()
		cartridge.ejected.factor.clear()
		cartridge.ejected.enabled = True

def _disable_cart_eject_irq():
	with set_br():
		cartridge.ejected.enabled = False

def _check_ejected():
	""" True if Z=1 """
	with set_br():
		if cpu.SC >> 6 == cartridge.irq_priority:
			if cartridge.ejected.factor:
				cartridge.ejected.factor.clear()
				return True
	return False

def _enter_high_speed_operation():
	with set_br(), suppress_interrupts():
		enter_high_speed_operation()

def enter_high_speed_operation():
	cpu.vdc = 0
	time.sleep(...)  # 83 cycles
	cpu.osc3_enabled = True
	time.sleep(...) # 1639 cycles
	cpu.osc = OSC3
	unknown.r02_4 = 1

def _enter_low_speed_operation():
	with set_br(), suppress_interrupts():
		enter_low_speed_operation()

def enter_low_speed_operation():
	unknown.r02_4 = 0
	cpu.osc = OSC1
	cpu.osc3_enabled = False
	cpu.vdc = 1

def _cart_slot_off():
	with set_br(), suppress_interrupts():
		cart_slot_off()

def cart_slot_off():
	unknown.r02_6 = 0
	return unpower_cart()

def unpower_cart():
	cartridge.powered = False

def _cart_slot_on():
	with set_br(), suppress_interrupts():
		cart_slot_on()

def cart_slot_on():
	unknown.r02_6 = 1
	return power_cart()

def power_cart():
	cartridge.powered = True
	unknown.r02_7 = 1
	time.sleep(...)  # 203 cycles
	_ = MEM[0x2AAA]
	unknown.r02_7 = 1

def _cart_detect():
	""" True if Z=0 """
	with set_br():
		return bool(cartridge.inserted)

def _read_structure(addr: int):
	with set_br(), suppress_interrupts():
		bit0 = MEM[addr] & 1
		if bit0:
			func_addr = read3(addr + 8)
		comp = MEM[addr + 7]
		iy = read3(addr + 4)
		ix = read3(addr + 1)
		unknown.r02_7 = 1
		MEM[ix] = 0xff  # should not work with ROM?
		unknown.r02_7 = 1
		byte = MEM[iy]
		unknown.r02_7 = 1
		if bit0:
			call_a_hl(func_addr)
		return byte == comp

def call_a_hl(addr: int):
	""" call addr and return """

def _set_prc_rate(rate_divider: int):
	lcd.rate_divider = rate_divider

def _get_prc_rate(rate_divider: int):
	return int(lcd.rate_divider)

def _game_id_valid():
	with set_br():
		return bool(cartridge.multicart_mode)

def _ir_pulse(iy: int, wait: int):
	# interrupt doesn't require IY be $2061
	assert iy == 0x2061
	io.ir_txd.data = 1
	time.sleep(...)  # wait * 4 cycles

@contextmanager
def set_br():
	# push EP, BR in the caller
	EP = 0x00
	BR = 0x20
	yield
	# pop BR, EP at the return in the caller

def wait_8000_cycles():
	""" wait 8000 cycles including the CARL to get here """
	time.sleep(...)

def read_keys_buffer(h: int):
	"""
	Returns H, A; Clobbers B
	h (input): previously pressed keys
	h (return): currently pressed keys
	a: newly pressed keys
	"""
	b = ~keypad.all
	a = (h ^ b) & b
	return KeypadData(b, a)

def load_tilemap(iy: int|Location):
	""" Clobbers IX, L """
	if isinstance(iy, Location):
		iy = iy.addr
	ix = 0x1360  # tilemap
	for l in range(96):
		MEM[ix+l] = MEM[iy+l]

def load_middle_5_tilemap(iy: int|Location):
	""" Returns in IX, Clobbers L """
	if isinstance(iy, Location):
		iy = iy.addr
	for l in range(60):
		MEM[0x1378+l] = MEM[iy+l]
	return 0x1378

def copy_one_frame():
	""" Assumes BR=20 """
	lcd.copy_complete.factor.clear()
	lcd.render = True
	while not lcd.copy_complete.factor: pass
	lcd.render = False

def game_select_screen():
	""" Stage 2b of boot: multicart game select """
	ram.final_name_row_start = l = \
		((ram.num_game_structs - 1) * 12) & 0xff
	ram.final_name_row_start_min48 = max(l, 48)
	load_tilemap(ram.game_select_map)
	ix = ram.current_row_start
	iy = ram.move_cooldown
	ram.key_history = 0
	kp = KeypadData(~keypad.all, 0)
	MEM[ix] = l = 0
	draw_game_names(0, l)
	# loc_0x0C3E
	while True:
		lcd.frame_divider_overflow.factor.clear()
		# loc_0x0C41
		while not lcd.frame_divider_overflow.factor: pass
		init_display(wait=False)
		apply_default_contrast()
		kp = read_keys_buffer(kp.pressed)
		ram.key_history |= kp.newly_pressed
		for _ in range(1):  # to skip loc_0x0C6F
			if kp.newly_pressed:
				# if a new button was pressed
				MEM[iy] = 13
				# jrs loc_0x0C6C
			else:
				# loc_0x0C61
				if kp.pressed & ram.key_history:
					# if we're still pressing a button we've pressed before
					MEM[iy] -= 1
					if MEM[iy]:
						break
					MEM[iy] = 5
					# jrs loc_0x0C6C
				else:
					break
			# loc_0x0C6C
			# carl loc_0x0C71
			if kp.a.newly_pressed or kp.c.newly_pressed:
				a = l // 12
				lcd.render = False
				load_tilemap(ram.blank_tilemap)
				copy_one_frame()
				return run_selected_game()
			# loc_0x0C8B
			elif kp.power.newly_pressed or kp.b.newly_pressed:
				return shutdown()
			# loc_0x0C92
			elif kp.up.newly_pressed:
				a = l
				if not a:
					# loc_0x0CCB
					continue
				a -= 12
				l = a
				a = MEM[ix]
				if l:
					b = l
					if a == b:
						a -= 12
						MEM[ix] = a
				# loc_0x0CA8
			# loc_0x0CAA
			elif kp.down.newly_pressed:
				a = l
				b = MEM[0x152A]
				if a == b:
					# loc_0x0CCB
					continue
				a += 12
				l = a
				a = MEM[ix]
				if l != b:
					a += MEM[0x1529]
					b = l
					a = MEM[ix]
					if l == b:
						a += 12
						MEM[ix] = a
			else:
				# loc_0x0CCB
				continue
			# loc_0x0CC8
			draw_game_names(l, a)
			# loc_0x0CCB
			# return from loc_0x0C71
		# loc_0x0C6F

def draw_game_names(selected_row_start: int, screen_top_start: int):
	"""
	Clobbers B
	selected_row_start in L
	screen_top_start in A
	both are measured in tiles, 0-based
	"""
	ix = load_middle_5_tilemap(ram.game_names_map.addr + screen_top_start)
	iy = 0x1372 # tile 18 (6,1)
	if screen_top_start:
		MEM[iy] = 33  # up arrow with line above tile
	else:
		# loc_0x0CE4
		MEM[iy] = 31  # line above without arrow tile
	# loc_0x0CE6
	bottom = screen_top_start + ram.final_name_row_start_min48
	iy = 0x13BA  # tile 90 (6,7)
	if bottom != ram.final_name_row_start:
		MEM[iy] = 44  # down arrow with line below tile
	else:
		# loc_0x0CF6
		MEM[iy] = 42  # line below without arrow tile
	# loc_0x0CF8
	a = selected_row_start - screen_top_start + 1
	MEM[ix + a] = 11  # selection arrow tile
	lcd.render = True

def play_animation(footer_addr: int, data_addr: int):
	load_tilemap(ram.blank_tilemap)
	footer = read2(footer_addr)
	length = footer & 0x01FF
	size = footer >> 9
	ram.total_anim_frames = length
	lcd.frame_divider_overflow.factor.clear()
	while not lcd.frame_divider_overflow.factor:
		pass
	lcd.frame_divider_overflow.factor.clear()
	kp = KeypadData(~keypad.all, 0)
	l = size
	while ram.total_anim_frames:
		l -= 2
		data = read2(data_addr + l)
		if l == 0: l = size
		graphic_addr = data & 0x01FF
		ram.frames_remaining = data >> 9
		load_middle_5_tilemap(graphic_addr)
		lcd.render = True
		while ram.frames_remaining:
			while not lcd.frame_divider_overflow.factor:
				pass
			lcd.frame_divider_overflow.factor.clear()
			init_display(wait=False)
			apply_default_contrast()
			kp = read_keys_buffer(kp.pressed)
			if (
				kp.power.newly_pressed
				or kp.a.newly_pressed
				or kp.b.newly_pressed
				or kp.c.newly_pressed
			):
				# let caller check buttons
				yield kp
			ram.total_anim_frames -= 1
			if not ram.total_anim_frames: break
			ram.frames_remaining -= 1

def low_battery_screen():
	for kp in play_animation(
		low_battery_animation_footer,
		low_battery_animation
	):
		if kp.a.newly_pressed or kp.c.newly_pressed:
			break
		return shutdown()
	lcd.render = False
	load_tilemap(ram.blank_tilemap)
	copy_one_frame()

def insert_cart_screen():
	with suppress_interrupts():
		cartridge.powered = False
		for kp in play_animation(
			insert_cart_animation_footer,
			insert_cart_animation
		):
			if kp.power.newly_pressed or kp.b.newly_pressed:
				break
			if cartridge.inserted:
				return _reset2()
		return shutdown()

def decode_picture():
	source = imgdata
	dest = ram.blank_tilemap.addr
	while source != 0x1000:
		byte = MEM[source]
		source += 1
		if byte == 0xF9:
			# Fill some number of 00s
			count = MEM[source] + 1
			source += 1
			for _ in range(count):
				MEM[dest] = 0
				dest += 1
		elif byte == 0xFB:
			fill = MEM[source]; source += 1
			count = MEM[source]; source += 1
			for _ in range(count):
				MEM[dest] = fill
				dest += 1
		else:
			MEM[dest] = byte
			dest += 1

	# Vertically flip last 11 tiles (as new tiles)
	for source, dest in zip(
		range(ram.v_flip_start, ram.v_flipped_tiles.addr),
		range(ram.v_flipped_tiles.addr, ram.v_flipped_tiles.end),
	):
		MEM[dest] = int(f"{MEM[source]:08b}"[::-1])

low_battery_animation = 0x0E22
low_battery_animation_footer = 0x0E36
insert_cart_animation = 0x0E38
insert_cart_animation_footer = 0x0E3E
imgdata = 0x0E40
