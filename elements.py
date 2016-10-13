import json
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

class star(object):

    def __init__(self, pin_order=None):
        if pin_order is None:
            self.pin = (36,37,32,33,31,29,22,18,16,15)
        else:
            self.pin = pin_order
        self.N = len(self.pin)

        for pn in self.pin:
            GPIO.setup(pn, GPIO.OUT)

    def engine(self, seq):
        for d in seq:
            if d[1] != []:
                GPIO.output([self.pin[p] for p in d[1]], 1)
            if d[2] != []:
                GPIO.output([self.pin[p] for p in d[2]], 0)
            time.sleep(d[0])

    def on(self):
        GPIO.output(self.pin, 1)

    def off(self):
        GPIO.output(self.pin, 0)

    def rotate(self, carrier=[0], v=1, s=1, b='on', dt=1, Nsteps=10, run=True):
	"""
	carrier = initial strip position(s) to 'move'
	v = direction of rotation (1 or -1)
	s = step size of rotation
	dt = time between steps
	Nsteps = number of steps
	b = carrier state (on or off)
	"""

	if v > 0:
	    v = 1
	elif v < 0:
	    v = -1

	seq = []

	C = carrier
	C_ = [n for n in range(self.N) if n not in C]
	if b is 'off':
	    temp = C
	    C = C_
	    C_ = temp
	seq.append((dt, C, C_))

	def shift(plist):
	    return [((p + v*s) % self.N) for p in plist]

        for rev in range(Nsteps):
	    C = shift(C)
	    C_ = shift(C_)
	    seq.append((dt, C, C_))
	    print rev
	    print C
	    print C_
	
	if run:
            self.engine(seq)
	else:
	    return seq
 
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='composition file (json)')
    args = parser.parse_args()

    penta = star()
    with open(args.file, 'r') as fi:
        script = json.load(fi)
    penta.engine(script['composition'])
