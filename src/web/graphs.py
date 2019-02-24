import glob
import matplotlib.pyplot as plt

files = glob.glob("data/resultc1c2c3.bed")

plt.style.use('seaborn-whitegrid')

fig = plt.figure()
ax = plt.axes()

y_values = {}

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

# chrm_colors = {}
# for i in range(24):
#     chrm_colors[k] = colors[i % len(colors)]

# plt.yticks(np.array(list(range(1, len(line.keys())+1))), line.keys())
# plt.ylim(-1, len(chrm_colors)+1)



def plot_segment(ax, chrm, start, end, opts="", line_width=2, **kwargs):
    ax.plot([start, end], [0] * 2, opts, linestyle="-", color="blue", linewidth=line_width,
             **kwargs)


def plot_chromosome(ax, chrm_data):
    for row in chrm_data[:5]:
        plot_segment(ax, *row, )


def generate_chromosome_images(line):

    plt.xlim(0, 3000000)

    thing = plt.subplots(len(line.keys()), 1, sharex=True, sharey=False)
    thing[0].subplots_adjust(wspace=0)

    for i, chrm in enumerate(line.keys()):
        thing[1][i].set_ylim(-1, 1)
        thing[1][i].set_ylabel(chrm)
        plot_chromosome(thing[1][i], line[chrm])

    plt.savefig('web/static/img/plots/testingplot.png', dpi=4000)
