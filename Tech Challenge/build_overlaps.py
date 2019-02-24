#!/usr/bin/env python
# Nick Weiner
# HudsonAlpha Tech Challenge

import re


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
    for seg1 in chrm:
        start1, end1 = seg1
        overlaps = []
        for file in data:
            if file == f_name:
                next()
            for i in data[file][chrm]:

            start = max(start1,start2) #+1
            end = min(end1,end2)
            overlap= end - start
            if overlap >= overlap_amt:
                overlaps.append(start, end, f_name, file)
    return overlaps


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Make overlaps data""")
    parser.add_argument("bed_files", type=str, help="bed files to be read")
    parser.add_argument("overlap", help="Amount of overlap between fragments", type=int,
                        default=50)
    parser.add_argument("k", type=int, help="minimum number of other files a segment must"
                                            " overlap", default=1)
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='Multiple flags increase verbosity')
    parser.add_argument('-test', '-t', action='store_true',
                        help='Do not store the data')
    args = parser.parse_args()
    fs = args.bed_files.split(',')
    bed_dict = {}
    for f in fs:
        bed_dict[f[-5:]] = bring_in_data(f)
    print(fs)
    for file in bed_dict:
        for chrm in file:
            get_overlaps(chrm, file, bed_dict)



