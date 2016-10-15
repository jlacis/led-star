import json
import RPi.GPIO as GPIO
import time

class Engine(object):

    def __init__(self, pin_map=None):
        self.pin_map = pin_map
        self.seq = []

    def run(self, seq=None, map=False):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_map, GPIO.OUT)

        if seq is None:
            seq = self.seq

        def set_pins(note, state=1):
            if state == 1:
                i = 1
            else:
                state = 0
                i = 2
            if not isinstance(note[i], (list, tuple)):
                pins = [note[i]]
            else:
                pins = note[i]
            if map:
                pins = [self.pin_map[p] for p in note[i]] 
            GPIO.output(pins, state)
        
        for note in seq:
            if note[1] != []:
                set_pins(note)
            if note[2] != []:
                set_pins(note, state=0)
            if note[0] <= 0:
                break
            else:
                time.sleep(note[0])

    def build(self, block):
        self.seq.extend(block)

    def build_from_file(self, infile):
        with open(infile, 'r') as fi:
            sheet = json.load(fi)
        self.seq.extend(sheet['composition']

    def export_to_file(self, outfile):
        pass
