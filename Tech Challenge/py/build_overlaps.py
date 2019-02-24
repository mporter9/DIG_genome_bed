#!/usr/bin/env python
# Nick Weiner
# HudsonAlpha Tech Challenge
# from sys import argv
from datetime import datetime
import glob
from collections import deque
from bed_interval import Interval, BedData
start_t = datetime.now()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""Make overlaps data""")
    parser.add_argument("overlap", help="Amount of overlap between fragments", type=int,
                        default=50)
    parser.add_argument("k", type=int, help="minimum number of other files a segment must"
                                            " overlap", default=1)
    parser.add_argument("-path", type=str, default="",
                        help="path to bed files to be read")
    parser.add_argument('--verbose', '-v', action='count', default=0,
                        help='Multiple flags increase verbosity')
    parser.add_argument('-test', '-t', action='store_true',
                        help='Do not store the data')
    args = parser.parse_args()
    bed_files = glob.glob('{}*[0-9].bed'.format(args.path))
    beds = []
    if args.verbose:
        print('Processing:')
    for f in bed_files:
        new_bed = BedData()
        if args.verbose:
            print('...{}'.format(f))
        new_bed.load_bed(f)
        beds.append(new_bed)
    current_files = deque(beds)
    overlaps = BedData()

    unmade_beds = []
    while current_files:
        my_bed = current_files.popleft()
        for chrm in my_bed.reads:
            read_count = len(my_bed.reads[chrm])
            # get self overlaps in current file
            for i in range(read_count):
                # loop over current file looking for internal overlaps
                i_stt = my_bed.reads[chrm][i].start
                i_end = my_bed.reads[chrm][i].end
                for j in range(i+1, read_count):
                    j_stt = my_bed.reads[chrm][j].start
                    if i_end - j_stt >= args.overlap:
                        # print('Coverage occurred')
                        my_bed.reads[chrm][i].add_coverage(j_stt,
                                                           min(j_stt, i_end), 1)
                # loop over previously processed bed files
                for b in unmade_beds:
                    other_bed_len = len(b.reads[chrm])
                    for j in range(other_bed_len):
                        j_stt = b.reads[chrm][j].start
                        if i_end - j_stt >= args.overlap:
                            # print('Coverage occurred')
                            my_bed.reads[chrm][i].add_coverage(j_stt,
                                                               min(j_stt, i_end), 1)
                if my_bed.reads[chrm][i].max_coverage > 0:
                    overlaps.copy_interval(chrm, my_bed.reads[chrm][i])
        unmade_beds.append(my_bed)

    overlaps_f_name = 'overlaps_of_{}-{}_{}_{}_out'.format(bed_files[0][-5],
                                                              bed_files[-1][-5],
                                                              args.overlap,
                                                              args.k)
    overlaps.dump_intervals(overlaps_f_name+'.bed', args.k)
    overlaps.dump_intervals_json(overlaps_f_name+'.json', args.k)

    #print runtime for comparison with fortran solution
    print("loaded in " + str(datetime.now() - start_t))

