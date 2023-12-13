import argparse
import time

import matplotlib.pyplot as plt

from collatz import collatz


parser = argparse.ArgumentParser()
parser.add_argument('end_n', type=int)
parser.add_argument('--print-seqs', action='store_true')
parser.add_argument('--show-steps', action='store_true')

args = parser.parse_args()

start_time = time.time()

seqs = []
steps = []

for n in range(1, args.end_n + 1):
    seq, i = collatz(n, seqs)
    seqs.append(seq)
    steps.append(i)
    if args.print_seqs:
        print(seq)

elapsed_time = time.time() - start_time
print(f'time={elapsed_time}[s]')

if args.show_steps:
    plt.plot(steps, linestyle='None', marker='o')
    plt.show()