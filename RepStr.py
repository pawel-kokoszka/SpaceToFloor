import os
import sys
import fnmatch

def replace_string(str_to_replace, replacing_str):
    
    folder_path = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(folder_path)

    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f)) and str_to_replace in f]

    for file_name in files:        
            new_name = file_name.replace(str_to_replace, replacing_str,1)
            
            old_file = os.path.join(folder_path, file_name)
            new_file = os.path.join(folder_path, new_name)
            
            os.rename(old_file, new_file)

def main() :
    if len(sys.argv) != 3:
        print("Error, please provide 2 strings")
        sys.exit()
    
    replace_string(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()