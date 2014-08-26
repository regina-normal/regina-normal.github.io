#!/usr/bin/regina-python

import sys

c = NContainer()
c.setPacketLabel('Census')

line = sys.stdin.readline().strip()
while line:
    bits = line.split()
    name = bits[0] + ' : ' + bits[2] + '(' + bits[3] + ', ' + bits[4] + ')'
    tri = NTriangulation.fromIsoSig(bits[5])
    if tri.isOrientable():
        tri.orient()
    tri.setPacketLabel(name)
    c.insertChildLast(tri)

    line = sys.stdin.readline().strip()

c.save('census.rga')
