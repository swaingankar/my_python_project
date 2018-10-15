from tkinter import filedialog
from tkinter import *

import os.path
from os import path
import hashlib


def file_write(folder, direc, count):

	for i in direc:
		count += 1

		filename = folder + '/' + i

		if path.isfile(filename):
			file = open(filename, "rb")
			bytes1 = file.read()
			hash_value = hashlib.sha256(bytes1).hexdigest()

			hash_array.append(hash_value + " " + filename)
			file.close()

		elif path.isdir(filename):
			new_folder = filename
			sub_direc_files = os.listdir(new_folder)
			file_write(new_folder, sub_direc_files, count)
	return hash_array, count


root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

directory = os.listdir(folder_selected)
print(directory)
hash_array = []

hash_file = open("f_hashfile.txt", "w+")
hash_list, nos_of_files = file_write(folder_selected, directory, 0)
for name_hash in hash_list:
	hash_file.write(str(name_hash))
	hash_file.write("\n")

hash_file.write("Totakl str(nos_of_files))
hash_file.close()

print(f'Total number of files = {nos_of_files}')


