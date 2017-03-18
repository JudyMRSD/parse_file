import re
import os
import xml.etree.ElementTree as ET
import pdb

tree = ET.parse('country_data.xml')
root = tree.getroot()

for country in root.iter('country'):
    year = country.find('year').text
    name = country.get('name')
    print year, name