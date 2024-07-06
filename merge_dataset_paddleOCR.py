import os
from pathlib import Path
import shutil

def unit(file_name):
    data=""
    i=1
    for folder in os.listdir():
        pat="dataset_"+str(i)
        data1=""
        if not os.path.exists(pat) and not os.path.isdir(pat):
            break
        with open(pat+file_name) as fp:
            data1=fp.read()
            #print(data1)
        data+=data1
        data+='\n'
        i=i+1
    with open('./merged_dataset'+file_name,'w') as wd:
        wd.write(data)

def merge_img(folder_name):
    i=1
    path="merged_dataset"+folder_name
    if not os.path.exists(path):
        os.mkdir(path)
    for folder in os.listdir():
        pat="dataset_"+str(i)
        if not os.path.exists(pat) and not os.path.isdir(pat):
            break
        for file in os.listdir(pat+folder_name):
            if file.endswith('.jpg'):
                file_name=os.path.join(pat+folder_name,file)
                if os.path.isfile(file_name):
                    shutil.copy(file_name,path)
        i+=1

path="./dataset-text-detection/"
os.chdir(path)

sub=Path(__file__).parent.absolute

if os.path.isdir('./merged_dataset'):
    shutil.rmtree("merged_dataset")
os.mkdir("merged_dataset")

unit("/train.txt")
unit("/val.txt")

merge_img('/train')
merge_img('/val')

