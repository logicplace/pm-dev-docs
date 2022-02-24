## Operation

The 256Hz Timer is enabled by writing the LSB of TIM256_CTL to 1. This activates the timer. It might be a good idea to also reset the timer by writing the 2nd bit to 1 also.

When the timer is active register TIM256_CNT is incremented 256 times a second. Since it's an 8 bit register counting from 0 to 255 it overflows exactly 1 time a second.

## IRQs tied to 256 Hz timer

The counter register TIM256_CNT is also used to fire some interrupts at frequencies derived from the 256 Hz clock:

When TIM256_CNT overflows the 1 Hz IRQ $0E is fired.
When TIM256_CNT bit 8 increments (overflow from bit 7) the 2 Hz IRQ $0D
is fired.
When TIM256_CNT bit 6 increments (overflow from bit 5) the 8 Hz IRQ $0C
is fired.
When TIM256_CNT bit 4 increments (overflow from bit 3) the 32 Hz IRQ
$0B is fired.
