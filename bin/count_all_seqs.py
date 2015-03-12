#!/usr/bin/env python

import os
import sys
sys.path.append('/home/user/bin')
import seq_utils

directory = sorted(os.listdir('/home/user/Documents/python/sequences'))

def count_all(directory):
    for file in directory:
        if file.endswith('.fasta'):
          filename = open(file)
          seq_count = seq_utils.count_seqs(filename)
          print seq_count,"in",file

if len(sys.argv) != 2:
   print >>sys.stderr, sys.argv[0], "expects an argument"
   sys.exit("BAKA")

print count_all(sys.argv[1])
