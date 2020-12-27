import tabula
import os
#import pathlib

#This is a local file I created which has my personal folder paths
import my_local_folder_path as lfp

#Folder path for input files for extraction
root_dir = lfp.input_folder

#Scanning for all folders and files in root directory
for dir_, _, files in os.walk(root_dir):
    for file_name in files:
        rel_dir = os.path.relpath(dir_, root_dir)
        rel_file = os.path.join(rel_dir, file_name)
        # print(rel_file)
        # print(rel_dir)
        # print(file_name)

        ### generating new file name
        entrySplit = file_name.split('.pdf')
        newFileName = entrySplit[0]
        # print(newFileName)

        #Creating new filepath using root and relative directories
        filePath = (os.path.join(root_dir, rel_file))


        ### output file
        output_path = lfp.output_folder+"{}.csv".format(newFileName)
        tabula.convert_into(filePath, output_path, output_format="csv", pages='all', stream=True)

#End of processing
print("Done Processing Files.........")
