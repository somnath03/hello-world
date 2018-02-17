import os
directory = 'D:\Python' #because my files are located on This location
os.chdir(directory) #chdir stands for Change directory
current_name = 'SomnathGhosh.jpg' 
new_name = 'renamed.jpeg' # you can also change the file extensions like 1.jpeg to renamed.png
os.rename(current_name, new_name)
