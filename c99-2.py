import os
import shutil

sourcePath = "C:/Users/sudhi/OneDrive/Desktop/C98/txt/"
destination = "C:/Users/sudhi/OneDrive/Desktop/C98/test4/"

listOfFiles = os.listdir(sourcePath)

for file in listOfFiles:
    shutil.copy((sourcePath + file), destination)

