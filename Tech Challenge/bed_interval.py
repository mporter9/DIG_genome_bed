#!/usr/bin/env python3
from collections import defaultdict
import json

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.coverage = defaultdict(int)

    def add_coverage(self, start, end, depth):
        for i in range(start, end + 1):
            if self.start <= i <= self.end:
                self.coverage[i] += depth

    @property
    def mean_coverage(self):
        running_sum = 0
        for i in xrange(self.start, self.end + 1):
            running_sum += self.coverage[i]
        return float(running_sum) / self.size

    @property
    def size(self):
        return self.end - self.start


class BedData(object):

    def __init__(self):
        self.chr_totals = 0
        self.reads = {}

    def sort_intervals(self):
        for chr in self.reads:
            self.reads[chr] = sorted(self.reads[chr], key=lambda x: x.start)

    def load_bed(self, bed):
        with open(bed) as bf:
            for read in bf:
                data = read.split()
                chr = data[0]
                chr = chr.replace('chr', '')  # get value down to only number or letter
                start_pos = int(data[1])
                end_pos = int(data[2])
                if chr not in self.reads:
                    self.reads[chr] = []
                self.reads[chr].append(Interval(start_pos, end_pos))
        self.sort_intervals()
        self.chr_totals = self.get_total_bases_each_contig()

    def add_interval(self, chr, start, end):
        if not chr in self.reads:
            self.reads[chr] = []
        self.reads[chr].append(Interval(start, end))

    def is_overlap(self, chr, start_pos, end_pos, padding=0):
        start_pos -= padding
        end_pos += padding
        chr = chr.replace('chr', '') # get value down to only number or letter
        if chr not in self.reads:
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
                if found_overlap:
                    self.
            can_stop = True
        return found_overlap

    def get_total_bases_from_contig(self):
        chr_totals = {}
        for chr in self.reads:
            total_bases = 0
            for coord in self.reads[chr]:
                total_bases += coord.size
            chr_totals[chr] = total_bases
        return chr_totals


    def get_self_overlaps(self, set_overlap):
        overs = BedData()
        for chr in self.reads:
            for interval in self.reads[chr]:
                padding = 0
                if set_overlap<0:
                    padding = abs(set_overlap)
                if self.is_overlap(chr, interval.start, interval.end, padding):


    def dump_intervals(self, file_name):
        self.sort_intervals()
        with open(file_name, 'w') as of:
            for chr in self.reads:
                for interval in self.reads[chr]:
                    of.write('{0}\t{1}\t{2}\n'.format(chr, interval.start, interval.end))

    def dump_intervals_json(self, file_name):
        self.sort_intervals()
        dump_data = {}
        for chr in self.reads:
            dump_data[chr] = []
            for interval in self.reads[chr]:
                dump_data[chr].append({'start': interval.start, 'size': interval.size})
        with open(file_name, 'w') as of:
            of.write(json.dumps(dump_data))
