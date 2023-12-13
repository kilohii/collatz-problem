def step(n):
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    return n


def collatz(n, pre_calc_seqs=None):
    seq = []
    seq.append(n)
    i = 0

    while(n > 1):
        n = step(n)
        if pre_calc_seqs != None and n <= len(pre_calc_seqs):
            seq += pre_calc_seqs[n - 1]
            return seq, i + len(pre_calc_seqs[n - 1])
        seq.append(n)
        i += 1

    return seq, i
