import glob
import matplotlib.pyplot as plt
import numpy as np

files = glob.glob("data/*.bed")

lines = []

for i, file in enumerate(files):
    lines.append({})
    with open(file, "r") as f:
        while True:
            line = f.readline()

            if not line:
                break

            parts = line.replace("\n", "").split("\t")

            if parts[0] not in lines[i]:
                lines[i][parts[0]] = []

            lines[i][parts[0]].append((parts[0], int(parts[1]), int(parts[2]),))

# for i in range(len(lines)):
#     lines[i].sort()

print(lines[0].keys())

plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()

fig = plt.figure()
ax = plt.axes()

y_values = {}

for i, k in enumerate(lines[0].keys()):
    y_values[k] = i + 1

colors = [
    "green",
    "blue",
    "orange",
    "violet",
    "black",
    "red",
    "brown",
    "magenta",
    "orchid",
    "maroon",
    "tomato",
    "goldenrod",
    "darkslategray",
    "gold",
    "lime",
    "coral",
    "sienna",
    "olivedrab",
    "firebrick",
    "teal",
    "sandybrown",
    "lightskyblue",
    "mediumseagreen"
]

chrm_colors = {}
for i, k in enumerate(lines[0].keys()):
    chrm_colors[k] = colors[i % len(colors)]

print(y_values)
print(chrm_colors)

plt.yticks(np.array(list(range(1, len(lines[0].keys())+1))), lines[0].keys())
plt.ylim(-1, len(chrm_colors)+1)

max_x = 0
for line in lines:
    for k in line:
        if line[k][-1][-1] > max_x:
            max_x = line[k][-1][-1]

plt.xlim(0, np.log10(max_x))


def plot_segment(chrm, start, end, opts="", line_width=2, **kwargs):
    plt.plot([start, end], [y_values[chrm]] * 2, opts, linestyle="-", color=chrm_colors[chrm], linewidth=line_width,
             **kwargs)


# plot_segment("chr12", 1, 50000)
# plot_segment("chr12", 99000, 120000)


for line in lines:
    for key, value in list(line.items()):
        for r in value[:5]:
            plot_segment(key, *r)

plt.show()
