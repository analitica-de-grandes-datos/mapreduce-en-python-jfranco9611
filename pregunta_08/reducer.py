import sys

if __name__ == '__main__':

    curkey = None
    total = 0
    reg = 0
    for line in sys.stdin:
        key, val, count = line.split(",")
        val = float(val)
        count = float(count)

        if key == curkey:
            total += val
            reg += count

        else:
            if curkey is not None:
                prom = total / reg
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, prom))
            curkey = key
            total = val
            reg = count

    prom = total / reg
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, prom))