# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 17:25:31 2026

@author: pb910
"""

import pandas as pd
import glob 

import os.path

meshes = glob.glob('input_mesh/*.csv')

for mesh in meshes:
    mesh_in = pd.read_csv(mesh)

print(mesh_in.head())
#do stuff

slices_out = "This is slice 1 of the input file"

with open("output_slices/Output.txt", "w") as text_file:
    text_file.write(slices_out)