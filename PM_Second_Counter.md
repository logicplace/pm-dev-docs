## Second Counter Overview

The second timer, while simple, was misunderstood for a good portion of the initial reverse engineering process. SEC_CNT_\* provides a 24 bit second counter that increments with a one second period (based of a 32768hz crystal) and can be enabled, disabled or reset to zero using the SEC_CTL register. Initially, these registers were thought to be a general purpose counter, but is actually one half of the system's real time clock.

When a commercial game sets the time, it resets the timer and stores the current time and date in the [EEPROM](PM_EEPROM.md "wikilink"). Calculating the current time consists of simply adding the number of elapsed seconds to the second counter. Each time the system boots, commercial games compare the current seconds against a 24 bit value stored in EEPROM. This was the last known valid time. If the current second counter is less than the previous know valid, it is assumed that the clock is valid and a game resumes running normally.

Under no circumstances should any homebrew software reset or pause the second counter, as it will invalidate the time on the system. This counter continues to tick even when the system is suspended.
