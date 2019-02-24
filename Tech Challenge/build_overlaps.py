#!/usr/bin/env python
# Nick Weiner
# HudsonAlpha Tech Challenge
# from sys import argv
from datetime import datetime
import glob
from collections import deque
from bed_interval import Interval, BedData
start_t = datetime.now()

def bring_in_data(bed_file):
    file_data = {}
    with open(bed_file) as infile:
        for line in infile:
            line = line.strip()
            chrm, start, end, = line.split("\t")[0:3]
            if chrm not in file_data:
                file_data[chrm] = []
            file_data[chrm].append((int(start), int(end)))
    return file_data


def get_overlaps(chrm, f_name, data, overlap_amt):
    #   compare starts and ends
    for seg1 in bed_dict[f_name][chrm]:
        seg1
        start1, end1 = seg1
        overlaps = ''
        for file in data:
            if file == f_name:
                continue
            for start2, end2 in data[file][chrm]:
                start = max(start1,start2) #+1
                end = min(end1,end2)
                overlap = end - start
                if overlap >= overlap_amt:
                    overlaps+='\t'.join((chrm, str(start), str(end), f_name, file)) + '\n'
    return overlaps


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Make overlaps data""")
    parser.add_argument("bed_files_path", type=str, default="", help="path to bed files to be read")
    parser.add_argument("overlap", help="Amount of overlap between fragments", type=int,
                        default=50)
    parser.add_argument("k", type=int, help="minimum number of other files a segment must"
                                            " overlap", default=1)
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='Multiple flags increase verbosity')
    parser.add_argument('-test', '-t', action='store_true',
                        help='Do not store the data')
    args = parser.parse_args()
    bed_files = glob.glob('{}*[0-9].bed'.format(args.bed_files_path))
    # in_files = deque([BedData() for f in range(bed_files.len())])
    # fs = args.bed_files.split(',')
    beds = []
    for f in bed_files:
        new_bed = BedData()
        new_bed.load_bed(f)
        beds.append(new_bed)
    current_files = deque(beds)
    overlaps = BedData()

    while current_files:
        my_bed = current_files.popleft()
        for chrm in my_bed.reads
            for i in my_bed.reads[chrm]:
                my_bed.reads[chrm][i].start

        overlaps.add_interval
    # while True:
    #     try:
    #         bed_file = BedData()
    #         f = in_files.popleft()
    #         bed_file.load_bed(f)
    #     except IndexError:
    #         break
    import json
    result = json.dumps(o_laps)
    f = open('overlaps.json', 'w')
    f.write(result)
    f.close()

    with open('overlap.bed', 'w') as f2:
        f2.write(o_laps)
        f2.close()
    print("loaded in " + str(datetime.now() - start_t))

