cmake -G 'MSYS Makefiles' \
  -DCMAKE_INCLUDE_PATH=/mingw/include:/include:/c/Boost/include/boost-1_54 \
  -DCMAKE_LIBRARY_PATH=/mingw/lib:/usr/lib:/c/Boost/lib \
  -DCMAKE_INSTALL_PREFIX=/home/bab/software \
  -DQT_QMAKE_EXECUTABLE=/c/Qt/4.8.6/bin/qmake \
  -DREGINA_DOCS=/home/bab/src/docs.zip \
  ..
