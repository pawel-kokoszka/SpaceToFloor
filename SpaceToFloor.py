import os

folder_path = 'G:/renametest'

files = os.listdir(folder_path)

only_files = []

for f in files:
    if os.path.isfile(os.path.join(folder_path, f)) and  " " in f:
        only_files.append(f)

files = only_files


for filename in files:
    
    
        
    new_name = filename.replace(' ', '_')
    
    
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_name)
    
    
    os.rename(old_file, new_file)

    print(f"Renamed: {filename} -> {new_name}")