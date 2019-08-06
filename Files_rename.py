	
import os
  
path = 'FILE_PATH_TO_BE_RENAME'
new_path = 'FILE_PATH_TO_BE_RENAME'
os.chdir(path)

for index,img in sorted(enumerate(os.listdir(path), 1)):
    if img.endswith('.jpg'):
        #{index:01}.jpg = 1.jpg
        #{index:02}.jpg = 01.jpg
        #{index:03}.jpg = 001.jpg
        os.rename(img, f'{new_path}/{index:01}.jpg')
