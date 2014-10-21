#!/usr/bin/python

from __future__ import print_function
import sys
import os
import string
import datetime
import re

argc = len(sys.argv)
if argc < 2 :
    print('Usage:' + sys.argv[0] + ' header1.h header2.h ...');
    sys.exit(1)
paths = sys.argv[1:argc]
basenames = [os.path.basename(p) for p in paths]

template = string.Template("""
/******************************************************************
** THIS FILE AUTOMATICALLY GENERATED by $script
** on $today as a unified combined header file of header files:
** $input_files
******************************************************************/

"""[1:])

print(template.substitute(
    script = os.path.basename(__file__),
    input_files = ", ".join(basenames),
    today = datetime.datetime.now().strftime("%Y-%m-%d")
))

p = re.compile('#include\s+"([^"]+)"')

for fn in paths :
  f = open(fn)
  fn = os.path.basename(fn)
  print("/* BEGIN INCLUDE OF " + fn + " */")
  for line in f :
    m = p.search(line) 
    if not m or not m.groups()[0] in basenames :
      sys.stdout.write(line)
  f.close()
  print("/* END INCLUDE OF " + fn + " */\n")
