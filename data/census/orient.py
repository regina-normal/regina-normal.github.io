#!/usr/bin/regina-python

import sys

t = regina.open(sys.argv[1])

changed = 0

p = t
while p:
    if p.getPacketType() == NTriangulation.packetType:
        if p.isOrientable() and not p.isOriented():
            p.orient()
            changed = changed + 1
    p = p.nextTreePacket()

if changed:
    print 'Saving: ' + sys.argv[1] + ' (' + str(changed) + ' oriented)'
    t.save(sys.argv[1])
