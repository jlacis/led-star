class led(object):

    def __init__(self, pin):
	self.pin = pin

    def on(self, on_time=None):
        if on_time is None:
            on_time = -1
        seq = [(on_time, self.pin, [])]
        return seq

    def off(self, off_time=None):
        if off_time is None:
            off_time = -1
        seq = [(off_time, [], self.pin)]
        return seq

    def blink(self, Ncycles=10, high_time=1, low_time=1, end_state=0):
        seq = []
        for n in Ncycles:
            seq.append((high_time, self.pin, []))	
            seq.append((low_time, [], self.pin))
        return seq

class polygon(object):
    """
    Polygon object where each side is controlled by its own pin.
        If map is False (default), sequences are generated with edge numbers (0-N).
        If map is True, sequences are generated with pin numbers specified by pin_map.
    """
    def __init__(self, N=10, pin_map=(36,37,32,33,31,29,22,18,16,15), map=False):
        self.map = map
        if self.map:
            self.pin = pin_map
        else:
            self.pin = range(N)
        self.N = len(self.pin)

    def on(self, on_time=None):
        if on_time is None:
            on_time = -1
        seq = [(on_time, self.pin, [])
        return seq

    def off(self, off_time=None):
        if off_time is None:
            off_time = -1
        seq = [(off_time, [], self.pin)]
        return seq

    def rotate(self, carrier=[0], v=1, s=1, b='on', dt=1, Nsteps=10, run=True):
	"""
	carrier = initial strip position(s) to 'move'
	v = direction of rotation (1 or -1)
	s = step size of rotation
	dt = time between steps
	Nsteps = number of steps
	b = carrier state ('on' or 'off')
	"""

	if v > 0:
	    v = 1
	elif v < 0:
	    v = -1

	seq = []

	C = carrier
	C_ = [p for p in self.pin if p not in C]
	if b is 'off':
	    temp = C
	    C = C_
	    C_ = temp
	seq.append((dt, C, C_))

	def shift(edges):
            if map:
                edges = [self.pin_map.index(p) for p in edges]
	    new_seq = [((p + v*s) % self.N) for e in edges]
            if map:
                new seq = [self.pin_map[e] for e in new_seq]
            return new_seq    

        for rev in range(Nsteps):
	    C = shift(C)
	    C_ = shift(C_)
	    seq.append((dt, C, C_))
	
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='composition file (json)')
    args = parser.parse_args()

    penta = star()
    with open(args.file, 'r') as fi:
        script = json.load(fi)
    penta.engine(script['composition'])
