import os

correct_file=[]
missing_file=[]

path_6='/rds/general/user/mas515/home/CP_MOVIE2/movies_removed/removed_from_6'  
path_7='/rds/general/user/mas515/home/CP_MOVIE2/movies_removed/removed_from_7'
path_10='/rds/general/user/mas515/home/CP_MOVIE2/movies_removed/removed_from_10'
path_12='/rds/general/user/mas515/home/CP_MOVIE2/movies_removed/removed_from_12'


#Checking differences between raw data for the first CP pipeline and the output of the first CP pipeline
# filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/6_'
# for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
#     for file in files:               
#         nfile=file+'f'
#         if nfile in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/7_'):
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
# filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/6_'
for root, dirs, files in os.walk(path_6): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:        
        if file.endswith(".tif") and 'Ch3' in file:
            file_Ch8=file.replace(r'Ch3_xyzCorrected.tif','Ch8_xyzCorrected.tiff')
            file_Ch5=file.replace(r'Ch3_xyzCorrected.tif','Ch5_xyzCorrected.tif')
            file_Ch5=file_Ch5+'f'
            nfile=file+'f'      
        # if file.endswith("_Ch3_xyzCorrected.tif - T=0.tif"):
        #     ind=file.index("_Ch3_xyzCorrected.tif - T=0.tif")#_Ch3_xyzCorrected.tif - T=0.tiff
        #     rep=file[ind:]
        #     file_Ch5=file.replace(rep, '_Ch5_xyzCorrected.tif - T=0.tiff')
        #     file_Ch8=file.replace(rep, '_Ch8_xyzCorrected.tiff - T=0.tif')
        #     nfile=file+'f'

            if file_Ch5 in os.listdir(path_12) and file_Ch8 in os.listdir(path_10) and nfile in os.listdir(path_7):
                correct_file.append(file)
            else:
                # if 'Ch3' in file:
                missing_file.append(file)

print('correct_file', correct_file)
print('to be removed from folder 6', missing_file)

correct_file=[]
missing_file=[]
# filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/12_'
for root, dirs, files in os.walk(path_12): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:   
        if file.endswith(".tiff"):
            file_Ch8=file.replace(r'Ch5_xyzCorrected.tif','Ch8_xyzCorrected.tiff')
            file_Ch8=file_Ch8[:-1]
            file_Ch3=file.replace(r'Ch5_xyzCorrected.tif','Ch3_xyzCorrected.tif')
            nfile=file_Ch3
            file_Ch3=file_Ch3[:-1]            
        # if file.endswith("_Ch5_xyzCorrected.tif - T=0.tiff"):
        #     ind=file.index("_Ch5_xyzCorrected.tif - T=0.tiff")#_Ch3_xyzCorrected.tif - T=0.tiff
        #     rep=file[ind:]
        #     file_Ch8=file.replace(rep, '_Ch8_xyzCorrected.tiff - T=0.tif')
        #     file_Ch3=file.replace(rep, '_Ch3_xyzCorrected.tif - T=0.tif')
        #     nfile=file_Ch3+'f'

            if file_Ch8 in os.listdir(path_10) and file_Ch3 in os.listdir(path_6) and nfile in os.listdir(path_7):
                correct_file.append(file)
            else:
                missing_file.append(file)
print('correct_file', correct_file)
print('to be removed from folder 12', missing_file)

correct_file=[]
missing_file=[]
# filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/10_'
for root, dirs, files in os.walk(path_10): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:
        if file.endswith(".tif"):
            file_Ch5=file.replace(r'Ch8_xyzCorrected.tiff','Ch5_xyzCorrected.tif')
            file_Ch5=file_Ch5+'f'
            file_Ch3=file.replace(r'Ch8_xyzCorrected.tiff','Ch3_xyzCorrected.tif')
            nfile=file_Ch3+'f'               
        # if file.endswith("_Ch8_xyzCorrected.tiff - T=0.tif"):
        #     ind=file.index("_Ch8_xyzCorrected.tiff - T=0.tif")#_Ch3_xyzCorrected.tif - T=0.tiff
        #     rep=file[ind:]
        #     file_Ch5=file.replace(rep, '_Ch5_xyzCorrected.tif - T=0.tiff')
        #     file_Ch3=file.replace(rep, '_Ch3_xyzCorrected.tif - T=0.tif')
        #     nfile=file_Ch3+'f'

            if file_Ch5 in os.listdir(path_12)  and file_Ch3 in os.listdir(path_6) and nfile in os.listdir(path_7):
                correct_file.append(file)
            else:
                missing_file.append(file)
print('correct_file', correct_file)
print('to be removed from folder 10', missing_file)

correct_file=[]
missing_file=[]
# filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/7_'
for root, dirs, files in os.walk(path_7): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:   
        if file.endswith(".tiff"):
            file_Ch5=file.replace(r'Ch3_xyzCorrected.tif','Ch5_xyzCorrected.tif')
            file_Ch5=file_Ch5
            file_Ch8=file.replace(r'Ch3_xyzCorrected.tif','Ch8_xyzCorrected.tiff')
            file_Ch8=file_Ch8[:-1]  
            file_Ch3=file[:-1]          
        # if file.endswith("_Ch3_xyzCorrected.tif - T=0.tiff"):
        #     ind=file.index("_Ch3_xyzCorrected.tif - T=0.tiff")#_Ch3_xyzCorrected.tif - T=0.tiff
        #     rep=file[ind:]
        #     file_Ch5=file.replace(rep, '_Ch5_xyzCorrected.tif - T=0.tiff')
        #     file_Ch3=file.replace(rep, '_Ch3_xyzCorrected.tif - T=0.tif')
        #     file_Ch8=file.replace(rep, '_Ch8_xyzCorrected.tiff - T=0.tif')

            if file_Ch5 in os.listdir(path_12) and file_Ch3 in os.listdir(path_6) and file_Ch8 in os.listdir(path_10):
                correct_file.append(file)
            else:
                missing_file.append(file)
print('correct_file', correct_file)
print('to be removed from folder 7', missing_file)

# correct_file=[]
# missing_file=[]
# filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/7_KuO_output3'
# for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
#     for file in files:               
#         if file.endswith(".tiff"):
#             file_Ch8=file.replace(r'Ch3_xyzCorrected.tif','Ch8_xyzCorrected.tiff')
#             nfile=file_Ch8[:-1]
#             if nfile in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/10_split_tracked_concatenated_KuO_output'):
#                 correct_file.append(file)
#             else:
#                 missing_file.append(file)
# print('correct_file', correct_file)
# print('to be removed from folder 6,7,12', missing_file)