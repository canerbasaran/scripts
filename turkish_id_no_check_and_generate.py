#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The validation and generator of Turkish Identification Number
#
# Copyright 2011 Caner BAŞARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from random import randint


def check_generate(tc_no=None):
    """
    >>> check_generate(98768109974)
    True
    >>> check_generate()
    '71362682128'
    """
    chk = False
    if not tc_no:
        tc_no = randint(100000000, 1000000000)
        chk = True
    list_tc = map(int, str(tc_no))
    tc10 = (sum(list_tc[0:10:2])*7 - sum(list_tc[1:9:2])) % 10
    tc11 = (sum(list_tc[0:9]) + tc10) % 10
    if chk:
        return "%s%s%s" % (tc_no, tc10, tc11)
    else:
        return True if list_tc[9] == tc10 and list_tc[10] == tc11 else False