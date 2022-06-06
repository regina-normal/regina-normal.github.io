#!/bin/bash
set -e

for i in 1-triangulations 2-surfaces 3-links 4-python; do
  convert "osx/$i.png" -resize 240x150 "thumb/$i.png"
  convert "osx/$i.png" -resize 480x300 "thumb/$i@2x.png"
  convert "osx/$i.png" -resize 720x450 "thumb/$i@3x.png"
done
