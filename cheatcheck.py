#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       cheatcheck.py
#      
#       Copyright 2014 www.soycode.com
#      
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#      
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#      
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

"""
Recursively find and compare text for similarity, to check for plagiarism.
www.soycode.com
"""

import codecs
import difflib
import os
import pprint
import sys


def findfiles(ext, path='.'):
  """Get list of all files recursively in path w/extension."""
  walk = os.walk(path)  # default '.' for cwd
  files = []
  for w in walk:
    # os.walk gives path/file tuples, filter and join them
    files.extend([os.path.join(w[0], file)
                  for file in w[2] if file[-len(ext):] == ext])
  return files


def pairs(items):
  """Iterate through items and return list of tuples of all their pairs."""
  pairs = []
  for i in range(len(items)):
    for j in range(i + 1, len(items)):
      pairs.append((items[i], items[j]))
  return pairs


def simratio(doc1, doc2):
  """Return similarity ratio in [0,1] for strings."""
  junk = ' \t\n'  # characters to ignore
  matcher = difflib.SequenceMatcher(lambda x: str(x) in junk, doc1, doc2)
  # real_quick_ratio is too likely to falsely report ratio of 1.0
  # and this is still fast enough (<1 min running over thousands of pairs)
  return matcher.quick_ratio()


def comparefiles(filepairs):
  """Get similarity for all listed file pairs, return all list of tuples."""
  sim = []
  for pair in filepairs:
    # Using codecs to handle arbitrary encodings
    doc1 = codecs.open(pair[0]).read()
    doc2 = codecs.open(pair[1]).read()
    sim.append((pair, simratio(doc1, doc2)))
  return sim

  
def reportsim(sim, n):
  """Pretty-print the top n most similar file pairs."""
  pp = pprint.PrettyPrinter()
  pp.pprint(sorted(sim, key=lambda docrank: docrank[1], reverse=True)[:n])


def main():
  args = sys.argv[1:]
  # TODO parse args to allow for other options
  # For now, defaults
  ext = '.java'
  n = 10  # number of (most) similar pairs to report
  
  # Find all files w/extension in path and all subdirectories
  files = findfiles(ext)
  # Enumerate all pairs of files, and check them for similarity
  filepairs = pairs(files)
  sim = comparefiles(filepairs)
  # Sort by similarity and extract top n most similar file pairs
  reportsim(sim, n)


if __name__ == "__main__":
  main()
