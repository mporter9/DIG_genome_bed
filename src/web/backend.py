import glob

files = glob.glob("../data/*.bed")

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


def get_data(index):
    return False
    return lines[index]
