#!/bin/sh
export PKG_CONFIG_PATH="$PKG_CONFIG_PATH:/home/bab/software/lib/pkgconfig:/c/Program Files/Graphviz2.38/lib/pkgconfig"
cmake -G 'MSYS Makefiles' -DQDBM=1 \
  -DCMAKE_BUILD_TYPE=Debug \
  -DCMAKE_PREFIX_PATH=/c/Qt/Qt5.5.1/5.5/mingw492_32 \
  -DCMAKE_INSTALL_PREFIX=/home/bab/software \
  ..
