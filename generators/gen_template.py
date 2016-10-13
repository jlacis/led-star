import argparse
import json
import os
import sys
import subprocess
elpath = os.path.join(os.path.split(os.path.realpath(__file__))[0], '../')
sys.path.append(elpath)
from elements import star

outpath = '/home/pi/workspace/led-star/scripts'

parser = argparse.ArgumentParser()
parser.add_argument('outfile')
parser.add_argument('-d', '--outpath', default=None)
parser.add_argument('-a', '--author', default='John Lacis')
args = parser.parse_args()

st = star()

script = {'composition': [], 'author': args.author}

# ADD generator script HERE
#
# script['composition'].append() etc... 

if args.outpath is None:
    filename = os.path.join(outpath, args.outfile)
else:
    filename = os.path.join(args.outpath, args.outfile)
with open(filename, 'w') as fi:
    json.dump(script, fi)
