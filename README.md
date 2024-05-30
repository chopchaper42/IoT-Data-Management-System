# NSI Homework #4

## Pico code:

```python
from machine import UART,Pin, Timer
import utime
import random

uart = UART(0, baudrate=9600, tx=0, rx=1)

led = Pin('LED', Pin.OUT)
timer = Timer()
 
def blink(timer):
    led.toggle()
 
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

while True:
    
    temperature = random.uniform(15.0, 30.0)
    
    uart.write(f'{temperature}\n')
    print(f'{temperature}')
    
    utime.sleep(5)
```