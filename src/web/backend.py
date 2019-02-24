import glob
import json

files = glob.glob("data/*.bed")

lines = []

for i, file in enumerate(files):
    lines.append({})
    with open(file, "r") as f:
        while True:
            line = f.readline()

            if not line:
                break

            #parts = [part.strip() for part in line.split(" ")]
            #parts = parts[0].split("\t")
            line.replace(" ", "")

            parts = line.replace("\n", "").split("\t")

            if parts[0] not in lines[i]:
                lines[i][parts[0]] = []

            try:
                lines[i][parts[0]].append((parts[0], int(parts[1]), int(parts[2]),))
            except:
                continue


def bed_to_json(bed_data):
    chromosomes = list(bed_data.keys())

    result = {}

    for chrm in chromosomes:
        overlaps = []
        ref_gaps = []
        nonoverlaps = []
        for row in bed_data[chrm]:
            nonoverlaps.append({
                "start": row[1],
                "sep": row[2] - row[1]
            })
        chrm_data = {
            "overlaps": 59373566,
            "undefined": 36389037,
            "nonoverlaps": nonoverlaps,
            "ref_gaps": [],
            "overlaps": []
        }

        result[chrm] = chrm_data
        result["name"] = "none"

    return json.dumps(result)


