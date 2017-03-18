import re
import os
import xml.etree.ElementTree as ET
import pdb

tree = ET.parse('tote301.xml')
root = tree.getroot()
print "start"

f = open('workfile', 'w')
for item in root.iter('bndbox'):
    xmin = item.find('xmin').text
    ymin = item.find('ymin').text
    xmax = item.find('xmax').text
    ymax = item.find('ymax').text
    s = str(xmin)+' '+ str(ymin)+' '+str(xmax)+' '+str(ymax)+' 1'+'\n'
    f.write(s)

    
#output: names, xmin, ymin, xmax, ymax, score