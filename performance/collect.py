import os
import shutil
import subprocess
import argparse
import re
import sys
import json

parser = argparse.ArgumentParser(description='Make a timing plot.')
parser.add_argument('DIR', help='Root directory with the location of the benchmark.')
args = parser.parse_args()

def get_qe_time(fname):
    f = open(fname, 'r')
    result = 0
    for line in f.readlines():
        # PWSCF        :  27m49.03s CPU  11m50.52s WALL
        #m = re.search('\s+PWSCF\s+:(\w+)CPU(\w+)WALL', line)
        m = re.search('\s+PWSCF\s+:(.*)CPU(.*)WALL', line)
        # match is successful
        if m:
            val = 0
            # try to match 'XmY.YYs'
            m1 = re.search('(\d+)m\s*(\d+)\.(\d+)s', m.group(2).strip())
            if m1:
                val = 60 * int(m1.group(1)) + int(m1.group(2))
            else:
                # try to match XhYm
                m1 = re.search('(\d+)h\s*(\d+)m', m.group(2).strip())
                if m1:
                    val = 3600 * int(m1.group(1)) + 60 * int(m1.group(2))

            print("%s  ---> %i sec."%(m.group(0), val))
            result = val

    f.close()
    return result

def main():

    title = os.path.basename(args.DIR)

    print(f"Looking in {args.DIR}")

    results = {}

    for root, label, files in os.walk(args.DIR):
        for f in files:
            if f == 'slurm-stdout.txt':
                p, task_id = os.path.split(root)
                p, label = os.path.split(p)
                print(task_id)
                print(label)
                print(root)
                tts = get_qe_time(f"{root}/slurm-stdout.txt")
                m = re.search('(\d+)N_(\d+)R_(\d+)T', task_id)
                N = int(m.group(1))
                print(f"nodes: {N}")
                if label not in results:
                    results[label] = []
                results[label].append((N, tts))

    sorted_results = {}
    for e in results:
        sorted_results[e] = sorted(results[e])


    with open("output.json", "w") as out:
        json.dump(sorted_results, out)

    return


if __name__ == "__main__":
    main()
