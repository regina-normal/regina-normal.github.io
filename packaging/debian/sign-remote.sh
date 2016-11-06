#!/bin/bash
set -e

# Copyright © 2009 Stefano Zacchiroli <zack@upsilon.cc>
# Modified by Ben Burton to make this specific to signing Regina's
# debian/ubuntu package repository.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

host=people.debian.org
suites="jessie trusty xenial yakkety"

for suite in $suites; do
  echo "--------------------"
  echo "$suite "
  echo "--------------------"
  echo "I: preparing to sign for $suite ..."
  path="/home/bab/public_html/regina/$suite/Release"
  base=$(dirname "$path")

  tmp=`mktemp -t sign`
  sig="$tmp.gpg"
  trap "rm -f $tmp $sig" EXIT

  echo "I: retrieving file to sign from remote host ..."
  scp "$host:$path" $tmp
  echo "I: signing ..."
  gpg --default-key 0x36B861C1 --digest-algo SHA256 --detach-sign -o $sig $tmp
  echo "I: sending back signature ..."
  scp $sig "$host":"$path.gpg"
  echo "I: remote signing done."
done
