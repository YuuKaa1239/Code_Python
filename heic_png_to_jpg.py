import os
from PIL import Image
from pillow_heif import register_heif_opener
def convert_file(dir,old,new):
    for file in os.listdir(dir):
        if file.endswith(old):
            new_name = file[:-len(old)]+new
            old_file=os.path.join(dir,file)
            new_file=os.path.join(dir,new_name)
            os.rename(old_file,new_file)

path = "YOUR PATH TO FILE IMAGE"

#convert to png and jpg(if you want to convert another,  you can change parameter in ext, example: ext=['.png','.PNG','jpeg'] 
ext = ['.png','.PNG']
for e in ext:
    convert_file(path,e,".jpg")

##convert HEIC to jpg
help(register_heif_opener)
register_heif_opener()
HEIC_file = [photo for photo in os.listdir(path) if '.HEIC' in photo]
# for x in HEIC_file:
#     print(x)
os.chdir(path)
for f in HEIC_file:
    temp_img=Image.open(f)
    jpg_photo = f.replace('.HEIC','.jpg')
    temp_img.save(jpg_photo)
    os.remove(f)

#rename file
i=0
for file in os.listdir():
    new_file_name="pic{}.jpg".format(i)
    os.rename(file,new_file_name)
    i=i+1
