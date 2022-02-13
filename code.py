import board
import pwmio
import digitalio
import time
from adafruit_motor import stepper
dc = 2**15
freq = 2000
# out1 = pwmio.PWMOut(board.GP10, frequency=freq, duty_cycle=dc)
# out2 = pwmio.PWMOut(board.GP11, frequency=freq, duty_cycle=dc)
# out3 = pwmio.PWMOut(board.GP20, frequency=freq, duty_cycle=dc)
# out4 = pwmio.PWMOut(board.GP21, frequency=freq, duty_cycle=dc)
out1 = digitalio.DigitalInOut(board.GP10)
out1.direction = digitalio.Direction.OUTPUT
out2 = digitalio.DigitalInOut(board.GP11)
out2.direction = digitalio.Direction.OUTPUT
out3 = digitalio.DigitalInOut(board.GP20)
out3.direction = digitalio.Direction.OUTPUT
out4 = digitalio.DigitalInOut(board.GP21)
out4.direction = digitalio.Direction.OUTPUT
# xmotor = stepper.StepperMotor(ain1=out1,ain2=out2,bin1=out3,bin2=out4,microsteps=None)
# out3.pull =  digitalio.Pull.UP

for i in range(500):
    # xmotor.onestep(direction=stepper.FORWARD,style=stepper.DOUBLE)
    out3.value = True
    time.sleep(0.01)
    out3.value = False
    time.sleep(0.01)

# xmotor.release()