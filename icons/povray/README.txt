Regina POV-Ray Directory
------------------------

This directory contains original povray scene descriptions that were used to
generate various Regina icons.

Example usage:
  povray +Ireginasmall.pov +Oregina.png +Q11 +A0.0 +UA
  povray +Ireginasmall.pov +Oregina.png +H129 +W172 +Q9 +A0.0

Building the final image:
  povray +Iregina.pov +Oraw.png +Q11 +A0.0 +UA +H3072 +W4096
  convert -crop 3072x3072+400+0 raw.png regina.png
  increase highlights from 0 to ~3/4 in macos preview
  in gimp:
    translate 36 pixels up
    add a (20, 20, 45) drop shadow
    apply a gradient to the background
