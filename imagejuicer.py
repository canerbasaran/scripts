#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# imagejuicer - picture minimizer to upload sites.
#
# Copyright 2012 Caner BAŞARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os
from glob import glob
from PIL import Image
from tempfile import mkdtemp

destination_dir = mkdtemp(prefix="resized_img_", dir=os.curdir)

for infile in glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    (width, height) = im.size
    im_ratio = width / float(height)
    if im_ratio >= 1:
        im = im.resize((720,int(720/im_ratio+0.5)), Image.ANTIALIAS)
    else:
        im = im.resize((int(720*im_ratio+0.5),720), Image.ANTIALIAS)
    im.save(destination_dir + os.path.sep + file + ext)
