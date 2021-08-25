import matplotlib.pyplot as plt
import numpy as np
import json
import argparse

parser = argparse.ArgumentParser(description='Create a plot.')
parser.add_argument('filename', help='JSON dictionary with results.')
parser.add_argument('lmap', metavar='labels', type=str, nargs='*',
        help='Human-readable plot labels provided as a list of old:new maps')
args = parser.parse_args()

lmap = {}
for e in args.lmap:
    i = e.find(':')
    lmap[e[:i]] = e[i+1:]

with open(args.filename) as json_file:
    inp = json.load(json_file)

data_points = {}
for p in inp["data"]:
    xy_unsorted = []
    for d in inp["data"][p]:
        nodes = d['nodes']
        scf_time = d['scf_time']
        energy = d['energy']
        xy_unsorted.append((nodes, scf_time))

    xy_sorted = sorted(xy_unsorted)
    res = list(zip(*xy_sorted))
    data_points[p] = {}
    data_points[p]['x'] = res[0]
    data_points[p]['y'] = res[1]

nodes = []
ymax = 0
for e in data_points:
    ymax = max(ymax, data_points[e]['y'][0])
    if not nodes:
        nodes = data_points[e]['x']
    else:
        if nodes != data_points[e]['x']:
            raise RuntimeError('Wrong number of nodes')

xlabels = [str(e) for e in nodes]

x = np.arange(len(xlabels))

## time in sec.
#qe_native_time = [207, 169, 169]
## energy in kJ
#qe_native_energy = [893.503, 1436.458, 2087.321]
#
#qe_sirius_time = [143, 141, 109]
#qe_sirius_energy = [395.230, 716.140, 898.400]
#
#
#for i in range(len(nodes)):
#    qe_native_time[i] = qe_native_time[i] * nodes[i] / 3600.0
#    qe_sirius_time[i] = qe_sirius_time[i] * nodes[i] / 3600.0
#

fig, ax = plt.subplots()


ax.set_title(lmap.get('title', inp['title']))

ax.set_ylabel('Time to solution (sec.)')
ax.set_xticks(x)
ax.set_xlabel("Nodes")
ax.set_xticklabels(xlabels)

for e in data_points:
    ax.plot(x, data_points[e]['y'], 'o-', label=lmap.get(e, e))

ax.set_ylim(ymin=0)
ax.grid(True)
ax.legend()

plt.savefig(f"{inp['title']}.pdf", format="pdf", transparent=True)
#plt.savefig("output.png", format="png", dpi=300, transparent=True)
