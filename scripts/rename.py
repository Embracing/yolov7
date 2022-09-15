import glob
import os

path = r'D:\Dataset\food\5food\labels'

files = glob.glob(os.path.join(path, '*.txt'))
print(len(files))

files = sorted(files)

for file in files:
    new_file_name = file.replace(' ', '_')
    os.rename(file, new_file_name)
    # print(file)
    # print(new_file_name)
    # break