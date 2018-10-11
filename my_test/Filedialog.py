from tkinter import filedialog
from tkinter import *
import os
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()


directory =  os.listdir(folder_selected)

for i in directory:
	
	file_folder = folder_selected+'/'+i
	print(file_folder)

# with os.scandir(folder_selected) as it:
#     for entry in it:
#         if not entry.name.startswith('.') and entry.is_file():
#             print(entry.name)