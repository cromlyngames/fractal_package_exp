# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 09:01:12 2026

@author: pb910
"""

from os import path

from shapes_1 import shape_maker

# take in slice
# generate expected shape
# measure fit, deform and repeat until it fits.

# report the solution, and residual error

#take in slice.
 #take abs path
 #swap currnt folder for slicer folder / output slice
 # ingest file

target_file = '\Output.txt'
t = path.abspath(__file__)
t2 = t[0:-len("\deformation\deform2fit.py")]
t2 = t2 + "\mesh_slicer\output_slices"
t2 = t2 + target_file
# feels very brittle/manual, but may be unavoidable?

with open(t2) as f:
    slices = f.readlines()
    
shapes = []
for s in slices:
    shapes.append(shape_maker(len(s)))
        
print(shapes)
