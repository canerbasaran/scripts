#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Caner BAŞARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve


def down(download_dict):
    """
    >>> sample = {'scrpt.py': 'http://barrrrrrr/scrpt.py', 'foo.tar': 'http://foooooooo.com/foo.tar'}
    >>> down(sample)
    """
    for name in download_dict:
        if not os.path.isfile(name):
            urlretrieve(download_dict[name], name)