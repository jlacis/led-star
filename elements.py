import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class led(object):

    def __init__(self, pin):
	self.pin = pin
	GPIO.setup(self.pin, GPIO.OUT)

	self.clock_rate = 0.01

    def on(self, on_time=None):
	GPIO.output(self.pin, 1)
	start = time.time()
	if on_time is not None:
	    stop = start + on_time
	else:
	   return	

	while True:
 	    time.sleep(self.clock_rate)
            if stop < time.time():
	        break
	GPIO.output(self.pin, 0)

    def off(self, off_time=None):
	GPIO.output(self.pin, 0)
	start = time.time()
	if off_time is not None:
	    stop = start + off_time
        else:
	    return	

	while True:
 	    time.sleep(self.clock_rate)
	    if stop < time.time():
	        break
	GPIO.output(self.pin, 1)

    def blink(self, run_time=None, high=1, low=1, end_state=0):
	start = time.time()
	if run_time is not None:
	    stop = start + run_time

	while True:
	    self.on(high)
	    self.off(low)
	    if run_time is not None: 	
		if stop < time.time():
		    break
	GPIO.output(self.pin, end_state)

if __name__ == '__main__':
    pass
