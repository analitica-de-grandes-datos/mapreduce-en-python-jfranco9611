import sys
maxi = 2
if __name__ == "__main__":
    for line in sys.stdin:
        a, b = line.split('\t')
        a = a.zfill(maxi)
        b =list(b.strip().split(','))
        for x in b:
            sys.stdout.write("{}\t{}\n".format(x,a))
