#python script to concatenate tiff files of split timepoint movies
#Author: M. Secchi with the help of N. Gogoberidze
#Date: 2022-12-06

#Lines 16 and 39 have to be edited to match the path of the folder containing the split movies and the path of the folder where the concatenated movies will be saved

import os
import natsort
from natsort import natsorted
import numpy as np
from skimage import io
from tifffile import imwrite

filename =[]
#copy your path here
filepath='/rds/general/user/mas515/home/CP/output_data_movie_test'
for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:               
        if file.endswith(" - T=0.tiff"):
            ind=file.index("_Ch3_xyzCorrected.tif - T=0.tiff")#_Ch3_xyzCorrected.tif - T=0.tiff
            rep=file[ind:]
            file_init=file.replace(rep, '_')
            filename.append(file_init)
filename

sequence=[]
im_data_sequences = []
for root, dirs, files in os.walk(filepath):
	for unique_file in filename:
		sequence=[os.path.join(root, i) for i in files if unique_file in i]# i is representing an individual file name 
		x=natsorted(sequence)
		im_data_sequence = [io.imread(fn) for fn in x]
		im_data_sequences.append((unique_file, im_data_sequence)) #the parenthesis is creating a tuple which has 2 elements
		print(x)

for movie_name, movie_timepoints in im_data_sequences:#because tuple : first element will be movie name, second element will be movie_timepoint
    # try:
    out_image = io.concatenate_images(movie_timepoints)
    imwrite(f'/rds/general/user/mas515/home/CP/concatenated_KuO_output/{movie_name}Ch8_xyzCorrected.tiff', out_image, imagej=True, metadata={'axes': 'TZYX'})
    print(f'did write movies/{movie_name}.tiff')
    # except:
        # print(f'failed to write movies/{movie_name}.tiff')