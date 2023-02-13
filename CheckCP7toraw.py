import os

correct_file=[]
missing_file=[]

#Checking differences between raw data for the first CP pipeline and the output of the first CP pipeline
filepath='/rds/general/user/mas515/home/CP_MOVIE2/input2/6_timepoint_split_drift_corrected_channel_split'
for root, dirs, files in os.walk(filepath): # will open up all the folders, dirs is all the name of the folder it finds, files will contain all the filenames it finds
    for file in files:               
        nfile=file+'f'
        if nfile in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/input2/7_KuO_output3') or nfile in os.listdir('/rds/general/user/mas515/home/CP_MOVIE2/movies_removed/removed_from_7'):
            if nfile not in correct_file:
                correct_file.append(file)
        else:
            if 'Ch3' in nfile and nfile not in missing_file:
                missing_file.append(file)
