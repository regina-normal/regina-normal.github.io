Large Test Suite: Exhaustive Lists of Angle Structures
------------------------------------------------------

This directory contains a complete list of angle structures for all
triangulations in the SnapPea census of cusped hyperbolic manifolds.

The main reason for this list is so that, when the angle structure
enumeration algorithm is changed, the author can verify that the new code
produces the same results as the old code.

The files in this directory were created using Regina 4.5.

The regina-python script that produces the angle structures is stored
alongside the gzipped output file in this directory.  This script requires
a census file as an argument, which should be the copy of snappea-census.rga
that is shipped with regina.

WARNING: This script does not delete angle structure lists, which means
it can consume a *very* large amount of memory when run over a large
census.  This is due to ownership constraints in regina-python, and will
be fixed if the need becomes pressing.

