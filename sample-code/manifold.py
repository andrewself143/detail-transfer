from __future__ import print_function

import numpy as np
import os
import os.path
import sys
import subprocess
from termcolor import colored
# import pymesh
from plyfile import (PlyData, PlyElement)
# from objfile import objData
import argparse

"""
script to first uniform resample the mesh and then quadractic mesh simplify using meshlab
"""

def load_ply_data(filename):
	""" read ply file, only vertices and faces """

	mesh = {}
	plydata = PlyData.read(filename)
	vertices = plydata['vertex'].data[:]
	if len(vertices[0]) ==3:
	   vertices = np.array([[x, y, z] for x,y,z in vertices])
	else:
	   vertices = np.array([[x, y, z] for x,y,z,x1,y1,z1 in vertices]) #check for normals

	# input are all traingle meshes
	faces = plydata['face'].data['vertex_indices'][:]
	faces = np.array([[f1, f2, f3] for f1,f2,f3 in faces])

	mesh['vertices'] = vertices
	mesh['faces'] = faces
	return mesh

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default=10000, help='input_path')
parser.add_argument('--file', type=str, default=8000, help='path of text file')
opt = parser.parse_args()


if __name__ == "__main__":
	input_dir = opt.path
	output_dir = opt.path

	# with open(os.path.join(input_dir, opt.file)) as f:
	with open(opt.file) as f:
		for line in f:
			line = line.strip()
			print("HERE")
			print(line)

			if (line == "Icon"):
				continue

			inp = os.path.join(input_dir, line)
			out = os.path.join(output_dir, line)

			if inp.endswith('obj'):
				mesh = objData(inp)
				ver = len(mesh["vertices"])
			elif inp.endswith('.ply'):
				# mesh = pymesh.load_mesh(inp)
				mesh = load_ply_data(inp)
				#ver = len(mesh.vertices)
				ver = len(mesh['vertices'])

			# if ver > opt.ver:
			#     continue

			# create the script for meshlab
			script = os.path.join(input_dir,"nomanifold_script.mlx")
			with open(script, "w") as file:
				file.write("<FilterScript> \n")
				file.write("<filter name=\"Remove Faces from Non Manifold Edges\"> \n")
				file.write("</filter> \n")
				file.write("</FilterScript> \n")

			command = '/Applications/meshlab.app/Contents/MacOS/meshlabserver -i ' + inp
			command += ' -o ' + out
			command += ' -s ' + script

			print('No Manifold mesh......')
			output = subprocess.check_output(command, shell=True)
			last_line = output.splitlines()[-1]
