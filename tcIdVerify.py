#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tcIdVerify.py Turkish ID Verification Client for KPS Public Service
#
# Copyright 2014 Caner BAŞARAN
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.tx

import xml.etree.ElementTree as ET
from urllib2 import Request, urlopen

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
      <TCKimlikNo></TCKimlikNo>
      <Ad></Ad>
      <Soyad></Soyad>
      <DogumYili></DogumYili>
    </TCKimlikNoDogrula>
  </soap12:Body>
</soap12:Envelope>"""
header = {'Content-Type': 'application/soap+xml; charset=utf-8'}


def query(id, name, surname, birth_year):
    """
    >>> query("10000000146", "GAZİ MUSTAFA KEMAL PAŞA", "ATATÜRK", "1881")
    'true'
    """
    element = ET.fromstring(xml)
    element[0][0][0].text = id
    element[0][0][1].text = name.decode(encoding="utf-8")
    element[0][0][2].text = surname.decode(encoding="utf-8")
    element[0][0][3].text = birth_year
    element_str = ET.tostring(element, encoding="UTF-8")
    response = urlopen(Request("https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx", data=element_str, headers=header)).read()
    response_element = ET.fromstring(response)
    return response_element[0][0][0].text