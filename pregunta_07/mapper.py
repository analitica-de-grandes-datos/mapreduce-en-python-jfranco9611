
import sys
#from datetime import datetime
#print(sys.stdin.readlines()[0].split('   ')[2].strip())
maxi = 3
if __name__ == "__main__":
    for line in sys.stdin:
        strnum = line.split('   ')[2].strip()
        strnum = strnum.zfill(maxi)
        sys.stdout.write("{}   {}   {}\n".format(str(line.split('   ')[0]), strnum , line.split('   ')[1]))