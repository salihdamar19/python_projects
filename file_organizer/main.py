#Auhor: Salih Damar

import os
import shutil

folder = os.path.dirname(os.path.abspath(__file__))
files = []
for each in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, each)):
        files.append(each)

def createFolder(extension):
    os.makedirs(os.path.join(folder,extension))
    return os.path.join(folder, extension)
        

for file in files:
    extension = os.path.splitext(file)[1]
    extension = extension.replace('.','')
    if extension == 'py':
        continue
    elif os.path.isdir(os.path.join(folder, extension)):
        shutil.move(os.path.join(folder, file), os.path.join(folder, extension))
    else:
        shutil.move(os.path.join(folder, file), createFolder(extension))
    
    

