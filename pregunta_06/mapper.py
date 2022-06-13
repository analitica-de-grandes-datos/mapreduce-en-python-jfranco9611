import sys

if __name__ == "__main__":
    for line in sys.stdin:
        word = line.split(' ')
        sys.stdout.write("{},{}\n".format(str(word[0]), float(word[2])))
