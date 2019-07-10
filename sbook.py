#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# charlyoleg
# 2012/11/29
#
# sbook.py
# libre and free software
#
# This script parses text files and extracts paragraph containing the specified keywords.
# This script is thought to be used as phone directory.
# Use the sbook.sh bash file to use it more confortably.

import argparse
import sys            # for argv, exit
import re             # for split, sub

# global variable

sb_usage="""usage: sbook -d <my_directory.txt> [options] <key_word_1> <key_word_2>
example: sbook.py -d ../path/to/my_book.txt media
example: sbook.py -d ../path/to/my_book.txt media journal
example: sbook.py -d ../path/to/my_book.txt media\|ardennes
example: sbook.py -d ../path/to/my_book.txt media\|ardennes journal
"""

sb_parser = argparse.ArgumentParser(description=sb_usage)
sb_parser.add_argument('key_words', nargs='+', help='the searched words.')
sb_parser.add_argument('-d', '--directory', action='append', dest='sw_directory',
                      help="Path to the input file used as directory. Directory file format: one entry is a paragraph. Paragraph are marked off with one empty line. \# is comment and won't be displayed.")
sb_parser.add_argument('-g', '--grep', action='append', dest='sw_grep',
                      help="words used to select the displayed paragraph.")
sb_parser.add_argument('-v', '--grep_v', action='append', dest='sw_grep_v',
                      help="words used to unselect the displayed paragraph.")
sb_parser.add_argument('-a', '--append_filename', action='store_true', dest='sw_append_filename', default=False,
                      help="Append at the end of each entry its filename. This is useful when working with several directory files to get more filter possibilities.")
sb_args = sb_parser.parse_args()

if sb_args.sw_directory is None:
  print "ERR010: no path to the input file directory is defined!"
  sb_parser.print_help()
  sys.exit(2)

#print "dbg220: sb_args:", sb_args
#print "dbg221: sb_args.sw_grep:", sb_args.sw_grep
key_word_select = sb_args.key_words
key_word_unselect = []
if not sb_args.sw_grep is None:
  key_word_select.extend(sb_args.sw_grep)
if not sb_args.sw_grep_v is None:
  key_word_unselect.extend(sb_args.sw_grep_v)
if len(key_word_select)<1:
  print "ERR011: no key word has been defined!"
  sb_parser.print_help()
  sys.exit(2)
#print "dbg720: key_word_select:", key_word_select
#print "dbg721: key_word_unselect:", key_word_unselect

# read directories
entries_1 = []
for f_directory in sb_args.sw_directory:
  #print "dbg335: f_directory:", f_directory
  fh_directory = open(f_directory, 'r')
  one_txt = fh_directory.read()
  fh_directory.close()
  one_txt = re.sub('\n(\s*#.*\n)+','\n', one_txt) # remove lines containing only comments
  one_txt = re.sub('#.*\n','\n', one_txt) #remove comments written after data
  #print "dbg903: one_txt:", one_txt
  one_txt = re.sub('[ \t]+\n','\n', one_txt)
  #print "dbg904: one_txt:", one_txt
  one_txt = re.sub('\n\n+','\n\n', one_txt)
  #print "dbg905: one_txt:", one_txt
  if sb_args.sw_append_filename:
    tiplus = "\n{:s}\n\n".format(f_directory)
    one_txt = re.sub('\n\n', tiplus, one_txt)
    #print "dbg906: one_txt:", one_txt
  entries_1.extend(one_txt.split('\n\n'))
del one_txt
entry_nb=0
entries_2 = []
for et1 in entries_1:
  entry_nb += 1
  #print("dbg411: entry num: {:d}".format(entry_nb))
  #print("dbg412: {:s}".format(et1))
  et2 = re.sub('^\n', '', et1)
  sel = 1
  for kw in key_word_select: # must match all key words
    if not re.search(kw, et2, re.IGNORECASE):
      sel = 0
  for kw in key_word_unselect: # if match one key word, then ejected
    if re.search(kw, et2, re.IGNORECASE):
      sel = 0
  if sel == 1:
    entries_2.append(et2)
del entries_1

# display output
entry_nb=0
for et1 in entries_2:
  entry_nb += 1
  print("{:d}:".format(entry_nb))
  print("{:s}\n".format(et1))

print("Found entries: {:d}".format(entry_nb))

