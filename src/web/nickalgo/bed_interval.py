#!/usr/bin/env python3
from collections import Counter
import json
from numpy import ones

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.coverage = Counter()

    def add_coverage(self, start, end, depth):
        for i in range(start, end + 1):
            if self.start <= i <= self.end:
                self.coverage.update(list(map(int, ones(depth)*i)))

    # @property
    # def mean_coverage(self):
    #     running_sum = 0
    #     for i in range(self.start, self.end + 1):
    #         running_sum += self.coverage[i]
    #     return float(running_sum) / self.size

    @property
    def max_coverage(self):
        if len(self.coverage) == 0:
            return 0
        out = self.coverage.most_common(1)[0][1]
        return out

    @property
    def size(self):
        return self.end - self.start


class BedData(object):

    def __init__(self):
        self.chr_totals = 0
        self.reads = {}

    def sort_intervals(self):
        for chrm in self.reads:
            self.reads[chrm] = sorted(self.reads[chrm], key=lambda x: x.start)

    def load_bed(self, bed):
        with open(bed) as bf:
            for read in bf:
                data = read.split()
                chrm = data[0]
                chrm = chrm.replace('chr', '')  # get value down to only number or letter
                start_pos = int(data[1])
                end_pos = int(data[2])
                if chrm not in self.reads:
                    self.reads[chrm] = []
                self.reads[chrm].append(Interval(start_pos, end_pos))
        self.sort_intervals()
        self.chr_totals = self.get_total_bases_from_contig()

    def add_interval(self, chrm, start, end):
        if chrm not in self.reads:
            self.reads[chrm] = []
        self.reads[chrm].append(Interval(start, end))

    def copy_interval(self, chrm, interval):
        if chrm not in self.reads:
            self.reads[chrm] = []
        self.reads[chrm].append(interval) #ensures coverage values being shared

    def is_overlap(self, chrm, start_pos, end_pos, padding=0):
        start_pos -= padding
        end_pos += padding
        chrm = chrm.replace('chr', '') # get value down to only number or letter
        if chrm not in self.reads:
            return False
        chr_data = self.reads[chr]
        can_stop = False
        found_overlap = None
        while not can_stop:
            for coord in chr_data:
                if coord.start <= start_pos <= coord.end:
                    found_overlap = coord
                    break
                if coord.start <= end_pos <= coord.end:
                    found_overlap = coord
                    break
                if start_pos <= coord.start and end_pos >= coord.end:
                    found_overlap = coord
                    break
                if coord.start > end_pos:
                    break
            can_stop = True
        return found_overlap

    def get_total_bases_from_contig(self):
        chr_totals = {}
        for chrm in self.reads:
            total_bases = 0
            for coord in self.reads[chrm]:
                total_bases += coord.size
            chr_totals[chrm] = total_bases
        return chr_totals


    # def get_self_overlaps(self, set_overlap):
    #     overs = BedData()
    #     for chr in self.reads:
    #         for interval in self.reads[chr]:
    #             padding = 0
    #             if set_overlap<0:
    #                 padding = abs(set_overlap)
    #             if self.is_overlap(chr, interval.start, interval.end, padding):


    def dump_intervals(self, file_name, k=1):
        self.sort_intervals()
        with open(file_name, 'w') as output_f:
            for chrm in self.reads:
                for interval in self.reads[chrm]:
                    if interval.max_coverage>=k:
                        line = 'chr{0}\t{1}\t{2}\t{3}\n'.format(chrm, interval.start,
                                                                interval.end,
                                                                # interval.mean_coverage,
                                                                interval.max_coverage)
                        output_f.write(line)

    def dump_intervals_json(self, file_name, k=1):
        self.sort_intervals()
        dump_data = {}
        for chrm in self.reads:
            # chrm_t = 'chrm{}'.format(chrm)
            dump_data[chrm] = []
            for interval in self.reads[chrm]:
                if interval.max_coverage >= k:
                    dump_data[chrm].append({'start': interval.start,
                                            'max_coverage': interval.max_coverage,
                                            'size': interval.size})
        with open(file_name, 'w') as output_f:
            output_f.write(json.dumps(dump_data))
