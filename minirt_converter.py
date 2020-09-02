#!/usr/bin/python3.6

'''
Convert .obj files for miniRT project at 42
'''

import os
import sys


def get_triangle(line, d, color):
    i = line.split(' ')
    i1 = i[1].split('/')[0]
    i2 = i[2].split('/')[0]
    i3 = i[3].split('/')[0]
    vertex1 = ','.join((d[i1]['x'], d[i1]['y'], d[i1]['z']))
    vertex2 = ','.join((d[i2]['x'], d[i2]['y'], d[i2]['z']))
    vertex3 = ','.join((d[i3]['x'], d[i3]['y'], d[i3]['z']))
    triangle = ' '.join(('tr', vertex1, vertex2, vertex3, color)) + '\n'
    return triangle

def parse_polygons(filename, obj_file, d, color):
    with open(filename, 'w') as out:
        for line in obj_file:
            if line[:2] == 'f ':
                out.write(get_triangle(line, d, color))

def parse_vertices(obj_file, d):
    count = 1
    for line in obj_file:
        if line[:2] == 'v ':
            coord = line.split(' ')
            d[str(count)] = {'x': coord[1], 'y': coord[2], 'z': coord[3][:-1]}
            count += 1
    return d

def convert_to_rt(filename, color):
    d = dict()
    count = 0
    outname = filename.split('.')[0] + '.rt'
    with open(filename, 'r') as f:
        obj_file = f.readlines()
    d = parse_vertices(obj_file, d)
    parse_polygons(outname, obj_file, d, color)

if len(sys.argv) != 3:
    print('Usage: python minirt_converter.py <file.obj> <color>')
else:
    filename = os.path.join(sys.argv[1])
    color = sys.argv[2]
    convert_to_rt(filename, color)
