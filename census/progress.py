################################
#
#  Sample Python Script
#
#  Illustrates progress reporting during long operations.
#
#  See the file "progress.session" for the results of running this script.
#
################################

import time

# Create an 18-tetrahedron triangulation of a knot complement with real
# boundary faces (not an ideal vertex).  The knot is L106003 from the
# knot/link census.  We used Regina to truncate the ideal vertex, and
# then copied the isomorphism signature so that we can reconstruct the
# triangulation here.
sig = 'sfLfvQvwwMQQQccjghjkmqlonrnrqpqrnsnksaisnrobocksks'
tri = Triangulation3(sig)
print tri.size(), 'tetrahedra'

# Create a progress tracker to use during the normal surface enumeration.
# This will report the state of progress while the enumeration runs in
# the background.
tracker = ProgressTracker()

# Start the normal surface enumeration.
# Because we are passing a progress tracker to enumerate(), the
# enumeration will start in the background and control will return
# immediately to the python console.
surfaces = NormalSurfaces.enumerate(tri, NS_STANDARD, NS_VERTEX,
    NS_ALG_DEFAULT, tracker)

# At this point the enumeration is up and running.
# Output a progress report every half-second until it finishes.
while not tracker.isFinished():
    print 'Progress:', tracker.percent(), '%'
    time.sleep(0.5)


# The surface enumeration is now complete.
print surfaces.size(), 'normal surfaces'

