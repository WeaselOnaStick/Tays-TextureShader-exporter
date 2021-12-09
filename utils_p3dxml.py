from xml.dom import minidom
import re
import os
import base64
import struct
import math
from mathutils import Matrix, Vector
import xml.etree.cElementTree as ET


def p3d_et(ver=4.4):
    return ET.Element('Pure3DFile', LucasPure3DEditorVersion=(str(ver)))


def write_val(loc, name, value=None):
    """returns a value ET element with Name=name and Value=value at loc"""
    if (value is None):
        return ET.SubElement(loc, 'Value', Name=name)
    else:
        return ET.SubElement(loc, 'Value', Name=name, Value=(str(value)))


def write_xyz(loc, name, x, y, z, element='Value', yzswap=True):
    """returns a value ET element with Name=name and set XYZ at loc. SWAPS Y AND Z"""
    if yzswap:
        y,z = z,y
    if name:
        ET.SubElement(loc, element, Name=name, X=(str(x)), Y=(str(z)), Z=(str(y)))
    else:
        ET.SubElement(loc, element, X=(str(x)), Y=(str(z)), Z=(str(y)))


def write_comment(loc, text):
    """writes a comment at loc"""
    loc.append(ET.Comment(text))


def write_chunk(loc, chunk_type: str):
    """returns a chunk ET element with Type=type at loc"""
    return ET.SubElement(loc, 'Chunk', Type=chunk_type)


def write_ET(root, filepath):
    """writes entire root ET element into a file at filepath"""
    with open(filepath, "w") as f:
        f.write('\n'.join([line for line in minidom.parseString(ET.tostring(
            root, 'unicode')).toprettyxml(indent='\t').split('\n') if line.strip()]))
        f.close()