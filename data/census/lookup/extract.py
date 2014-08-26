#!/usr/bin/regina-python

import sys

t = regina.open(sys.argv[1])

p = t
while p:
    if p.getPacketType() == NTriangulation.packetType:
        print p.isoSig(), p.getPacketLabel()
    p = p.nextTreePacket()

