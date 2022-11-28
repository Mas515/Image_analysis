import os

correct_file=[]
missing_file=[]

#Checking differences between raw data for the first CP pipeline and the output of the first CP pipeline
# filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/6_timepoint_split_drift_corrected_channel_split'
# for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
#     for file in files:               
#         nfile=file+'f'
#         if nfile in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/7_KuO_output3'):
#             correct_file.append(file)
#         else:
#             if 'Ch3' in nfile:
#                 missing_file.append(file)


#Checking differences between raw data for the first CP pipeline and the input of Ilasik
# filepath='/Users/secchim/Downloads/CellProfiler/movie_processing/11_timepoint_split_concatenated_corrected_v2'
# for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
#     for file in files:               
#         if file.endswith(" - T=0.tif"):
#             ind=file.index("_Ch5_xyzCorrected.tif - T=0.tif")#_Ch3_xyzCorrected.tif - T=0.tiff
#             rep=file[ind:]
#             file_init=file.replace(rep, '_Ch1_xyzCorrected.tif - T=0.tif')
#             if file_init in os.listdir('/Users/secchim/Downloads/CellProfiler/movie_processing/6_timepoint_split_drift_corrected_channel_split'):
#                 correct_file.append(file_init)
#             else:
#                 missing_file.append(file_init)     

#Checking differences between raw data for the first CP pipeline and the tracked input and the Ilastik input
filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/6_timepoint_split_drift_corrected_channel_split'
for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:               
        if file.endswith("_Ch3_xyzCorrected.tif - T=0.tif"):
            ind=file.index("_Ch3_xyzCorrected.tif - T=0.tif")#_Ch3_xyzCorrected.tif - T=0.tiff
            rep=file[ind:]
            file_Ch5=file.replace(rep, '_Ch5_xyzCorrected.tif - T=0.tiff')
            file_Ch8=file.replace(rep, '_Ch8_xyzCorrected.tiff - T=0.tif')
            nfile=file+'f'

        if file_Ch5 in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/12_Ilastik_MK') and file_Ch8 in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/10_split_tracked_concatenated_KuO_output') and nfile in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/7_KuO_output3'):
            correct_file.append(file)
        else:
            if 'Ch3' in file:
                missing_file.append(file)

print('correct_file', correct_file)
print('file_missing from downstream folders', missing_file)

correct_file=[]
missing_file=[]
filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/10_split_tracked_concatenated_KuO_output'
for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:               
        if file.endswith("_Ch5_xyzCorrected.tif - T=0.tiff"):
            ind=file.index("_Ch5_xyzCorrected.tif - T=0.tiff")#_Ch3_xyzCorrected.tif - T=0.tiff
            rep=file[ind:]
            file_Ch8=file.replace(rep, '_Ch8_xyzCorrected.tiff - T=0.tif')
            file_Ch3=file.replace(rep, '_Ch3_xyzCorrected.tif - T=0.tif')
            nfile=file_Ch3+'f'

        if file_Ch8 in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/12_Ilastik_MK') and file_Ch3 in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/6_timepoint_split_drift_corrected_channel_split') and nfile in os.listdir('rds/general/user/mas515/home/CP_MOVIE2/input2/7_KuO_output3'):
            correct_file.append(file)
        else:
            missing_file.append(file)
print('correct_file', correct_file)
print('to be removed from folder 10', missing_file)

correct_file=[]
missing_file=[]
filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/12_Ilastik_MK'
for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:               
        if file.endswith("_Ch8_xyzCorrected.tiff - T=0.tif"):
            ind=file.index("_Ch8_xyzCorrected.tiff - T=0.tif")#_Ch3_xyzCorrected.tif - T=0.tiff
            rep=file[ind:]
            file_Ch5=file.replace(rep, '_Ch5_xyzCorrected.tif - T=0.tiff')
            file_Ch3=file.replace(rep, '_Ch3_xyzCorrected.tif - T=0.tif')
            nfile=file_Ch3+'f'

        if file_Ch5 in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/10_split_tracked_concatenated_KuO_output') and file_Ch3 in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/6_timepoint_split_drift_corrected_channel_split') and nfile in os.listdir('rds/general/user/mas515/home/CP_MOVIE2/input2/7_KuO_output3'):
            correct_file.append(file)
        else:
            missing_file.append(file)
print('correct_file', correct_file)
print('to be removed from folder 12', missing_file)
