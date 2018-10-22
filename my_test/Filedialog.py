from tkinter import filedialog
from tkinter import *
import sys
import os.path
from os import path
import hashlib
import time
import shutil


def file_write(folder, direc, count, f_start_time, total_count):

    for i in direc:

        filename = folder + '/' + i

        if path.isfile(filename):
            count += 1
            h = hashlib.md5()
            file = open(filename, "rb")
            chunk = 0
            try:
                while chunk != b'':
                    chunk = file.read(1024)
                    h.update(chunk)
            except MemoryError:
                print(f'Filename for Memory Error : {filename}')

            hash_value = h.hexdigest()
            hash_array.append(hash_value + " " + filename)
            hash_dict[filename] = hash_value
            file.close()

        elif path.isdir(filename):

            new_folder = filename
            sub_direc_files = os.listdir(new_folder)
            f_start_time = time.time()
            hash_temp, nos_of_files, total_temp, dict_temp = file_write(new_folder, sub_direc_files, 0, f_start_time, count)
            count += nos_of_files

    if not path.isfile(folder):
        print(f'Hash Completed : {folder} with : {count} files ' + " in %s seconds " % (time.time() - f_start_time))
        total_count += count

    return hash_array, count, total_count, hash_dict



root = Tk()
root.withdraw()
try:
    folder_selected = filedialog.askdirectory()
except FileNotFoundError:
    print("Please select file correctly:")
    sys.exit(0)
start_time = time.time()
count = 0
total_count = 0
try:
    directory = os.listdir(folder_selected)
except FileNotFoundError:
    print("Please select file correctly:")
    sys.exit(0)

print(directory)
hash_array = []
start_time = time.time()

hash_dict = {}
hash_dict_new = {}
hash_file = open("f_hashfile.txt", "w+")
hash_list, nos_of_files, total_count, hash_dict = file_write(folder_selected, directory, count, start_time, total_count)

hash_dict_orig = hash_dict

for item_new in hash_dict.copy().items():
    if hash_dict_new.get(item_new[0]):
        continue
    for item in hash_dict.copy().items():
        if item[1] == item_new[1] and item[0] != item_new[0]:
            # print(f'Yes compared Item_New : {item_new[0]} and {item_new[1]} + Item_New : {item[0]} and {item[1]}')
            hash_dict_new[item[0]] = item_new[1]

if not os.path.exists('C:/Users/Sachin/Desktop/ToBeDeleted'):
    os.makedirs('C:/Users/Sachin/Desktop/ToBeDeleted')

for item in hash_dict_new.items():
    print(f'location {item[0]} and hash {item[1]}')
    copyfilename = os.path.split(item[0])
    if not os.path.isfile('C:/Users/Sachin/Desktop/ToBeDeleted/'+copyfilename[1]):
        shutil.move(item[0], 'C:/Users/Sachin/Desktop/ToBeDeleted')
    else:
        os.remove('C:/Users/Sachin/Desktop/ToBeDeleted/'+copyfilename[1])
        shutil.move(item[0], 'C:/Users/Sachin/Desktop/ToBeDeleted')

    count += 1
print(count)


for name_hash in hash_dict_new:
    hash_file.write(str(name_hash))
    hash_file.write("\n")

hash_file.write(str(count))
hash_file.close()
print(f'Total number of files = {total_count}')
print("-- %s seconds --" % round(time.time() - start_time))




