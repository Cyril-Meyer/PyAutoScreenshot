import argparse
import os
import time
import mss

parser = argparse.ArgumentParser()
parser.add_argument('output', type=str,
                    help='output folder')
parser.add_argument('--wait', default=5.0, type=float,
                    help='wait time between screenshots (s)')
parser.add_argument('--limit', default=200, type=int,
                    help='max number of screenshots')
args = parser.parse_args()

if not os.path.isdir(args.output):
    os.makedirs(args.output)
if not os.path.isdir(args.output):
    raise NotADirectoryError

for i in range(args.limit + 1):
    time.sleep(args.wait)

    with mss.mss() as sct:
        f = sct.shot(output=f'{args.output}/{i+1:05d}.png')
        print(f)
