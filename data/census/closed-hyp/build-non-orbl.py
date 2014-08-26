#!/usr/bin/regina-python
#
# This does not cover the extra case from the Hodgson-Weeks paper.
#
# Note: The Hodgson-Weeks paper gives non-orientable manifolds as
# surgeries on WLM, which I believe is actually m131.

import sys

c = NContainer()
c.setPacketLabel('Census')

line = sys.stdin.readline().strip()
while line:
    bits = line.split()
    src = bits[2]
    cusped = 'm' + src
    tri = NSnapPeaCensusManifold('m', int(src)).construct()
    s = NSnapPeaTriangulation(tri)
    s.fill(1, 0)

    if s.solutionType() != NSnapPeaTriangulation.SolutionType.geometric_solution:
        print 'Bad solution type'
        sys.exit(1)
    vol = s.volume()
    final = s.filledTriangulation()
    name = str(vol) + ' : m' + src + '(1, 0)'

    final.intelligentSimplify()
    final.intelligentSimplify()
    final.setPacketLabel(name)
    c.insertChildLast(final)

    line = sys.stdin.readline().strip()

c.save('census.rga')
