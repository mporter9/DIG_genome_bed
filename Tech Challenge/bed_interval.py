#!/usr/bin/env python3
from collections import defaultdict
import json

class Interval(object):
    def __init__(self, start, end, depth):
        self.start = start
        self.end = end
        self.name = name
        self.coverage = defaultdict(int)

    def add_coverage(self, start, end, depth):
        for i in xrange(start, end + 1):
            if self.start <= i <= self.end:
                self.coverage[i] += depth

    def get_total_bases_from_contig(self):
        chr_totals = {}
        for chr in self.reads:
            total_bases = 0
            for coord in self.reads[chr]:
                total_bases += coord.size
            chr_totals[chr] = total_bases
        return chr_totals