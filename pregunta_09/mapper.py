import sys
maxi = 3
if __name__ == "__main__":
    for line in sys.stdin:
        strnum = line.split('   ')[2].strip()
        strnum = strnum.zfill(maxi)
        sys.stdout.write("{}   {}   {}\n".format(strnum, line.split('   ')[0] , line.split('   ')[1]))