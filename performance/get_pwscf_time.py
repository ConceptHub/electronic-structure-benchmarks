import sys
import re

def main():
    f = open(sys.argv[1], 'r')
    for line in f.readlines():
        # PWSCF        :  27m49.03s CPU  11m50.52s WALL
        #m = re.search('\s+PWSCF\s+:(\w+)CPU(\w+)WALL', line)
        m = re.search('\s+PWSCF\s+:(.*)CPU(.*)WALL', line)
        # match is successful
        if m:
            val = 0
            # try to match 'XmY.YYs'
            m1 = re.search('(\d+)m(\d+)\.(\d+)s', m.group(2).strip())
            if m1:
                val = 60 * int(m1.group(1)) + int(m1.group(2))



            print("%s  ---> %i sec."%(m.group(0), val))

    f.close()

if __name__ == "__main__":
    main()
