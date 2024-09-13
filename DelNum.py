import os

def add_zeros(number):
    if number < 10 :
        number_with_zeros = "00" + str(number)    
    elif number >= 10 and number < 100 :
        number_with_zeros = "0" + str(number)
    elif number >= 100 :
        number_with_zeros = str(number)        


    return number_with_zeros


def add_numeration():
    folder_path = os.path.dirname(os.path.abspath(__file__))

    files = os.listdir(folder_path)

    only_files = []
    # files_with_numeration = []

    for f in files:
        if os.path.isfile(os.path.join(folder_path, f)):
            only_files.append(f)

    files = only_files

    #check if numeration exist and remember last/max number
    for file_name in files:
        floor_index = file_name.find('_')
        if file_name[floor_index+1].isdigit():
            if file_name[floor_index+2].isdigit():
                if file_name[floor_index+3].isdigit():
                    if file_name[floor_index+4] == "_":
                        num_to_del = file_name[floor_index:floor_index+5]
                        new_name = file_name.replace(num_to_del, "_",1)            
                        old_file = os.path.join(folder_path, file_name)
                        new_file = os.path.join(folder_path, new_name)                        
                        os.rename(old_file, new_file)

def main() :
    add_numeration()

if __name__ == '__main__':
    main()