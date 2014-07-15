#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# file to base64 encoder script
#
# Copyright 2013 Caner BAŞARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from os import listdir, curdir
from os.path import isfile, join, sep
import base64
from tempfile import mkdtemp

dest_dir = mkdtemp(prefix="based64_", dir=curdir)
only_files = [f for f in listdir(".") if isfile(join(".", f))]
for infile in only_files:
    with open(infile, "r") as s:
        with open(dest_dir + sep + infile + ".txt", "w") as d:
            d.write(base64.b64encode(s.read()))