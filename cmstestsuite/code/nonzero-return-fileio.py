import sys
# -*- coding: utf-8 -*-

n = int(open("input.txt").readline().strip())
f = open("output.txt", "w")
f.write("correct %d\n" % n)
f.close()
sys.exit(1)
