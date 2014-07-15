#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# slidesharedownloader - command-line app for downloading slideshare slides.
#
# Copyright 2014 Caner BAŞARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from optparse import OptionParser
from pyquery import PyQuery
from tempfile import mkdtemp
import os
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

NAME = 'slidesharedownloader'
VERSION = '0.1'


def download(url, destination_dir):
    conn = PyQuery(url)
    titles = conn(".slide_image")
    for i in xrange(len(titles)):
        urlretrieve(titles.eq(i).attr("data-full"), "%s%s%s.jpg" % (destination_dir, os.path.sep, i+1))


def main():
    current_dir = os.curdir
    usage = "usage: %prog [options] url"
    version = "%s %s" % (NAME, VERSION)
    parser = OptionParser(usage, version=version)
    parser.add_option("-d", "--destination", action="store", dest="destination_dir")
    parser.add_option("-q", "--quiet", action="store_false",
                      dest="verbose", help="Be quiet. Don't write normal output, only errors.")

    (options, args) = parser.parse_args()

    if not options.destination_dir:
        options.destination_dir = mkdtemp(prefix="Slide_", dir=current_dir)
    abs_path_destination_dir = os.path.abspath(os.path.expanduser(options.destination_dir))

    if os.path.exists(abs_path_destination_dir):
        download(args[0], abs_path_destination_dir)
        print "Downloaded slide in " + abs_path_destination_dir
    else:
        print "ERROR: Destination directory does not exist."


if __name__ == "__main__":
    main()