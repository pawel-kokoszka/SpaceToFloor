import os

#folder_path = 'G:/renametest'
folder_path = os.path.dirname(os.path.abspath(__file__))

files = os.listdir(folder_path)

only_files = []
for f in files:
    if os.path.isfile(os.path.join(folder_path, f)) and  " " in f:
        only_files.append(f)

files = only_files


for file_name in files:
        
    new_name = file_name.replace(' ', '_')
    
    old_file = os.path.join(folder_path, file_name)
    new_file = os.path.join(folder_path, new_name)
    
    os.rename(old_file, new_file)

    print(f"Renamed: {file_name} -> {new_name}")