import sys

if __name__ == "__main__":
    for line in sys.stdin:
        sys.stdout.write("{},{}\n".format(str(line.split('   ')[0]), float(line.split('   ')[2])))