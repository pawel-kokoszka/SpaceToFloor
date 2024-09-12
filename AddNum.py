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
    files_with_numeration = []

    for f in files:
        if os.path.isfile(os.path.join(folder_path, f)) and  "_" in f:
            only_files.append(f)

    files = only_files

    if files.__len__() == 0 :
        print("0 files detect to add numeration")
    else:
        print(files)

    max_number = 0
    tmp_number = 0
    #check if numeration exist and remember last/max number
    for file_name in files:
        floor_index = file_name.find('_')
        if file_name[floor_index+1].isdigit():
            if file_name[floor_index+2].isdigit():
                if file_name[floor_index+3].isdigit():
                    tmp_number = int(file_name[floor_index+1:floor_index+4])
                    
                    if tmp_number > max_number:
                        max_number = tmp_number

                    files_with_numeration.append(file_name)

    files = [f for f in files if f not in files_with_numeration]

    new_files = []
    file_enumerator = max_number + 1
    for file_name in files:
        floor_index = file_name.find('_')
        name_with_number = file_name[:floor_index+1] + add_zeros(file_enumerator) + "_" + file_name[floor_index+1:]
        new_files.append(name_with_number)
        file_enumerator += 1 

    print(new_files)

    for index, file_name in enumerate(files):
            
        new_name = new_files[index]
        
        old_file_full_path = os.path.join(folder_path, file_name)
        new_file_full_path = os.path.join(folder_path, new_name)
        
        os.rename(old_file_full_path, new_file_full_path)

        print(f"Renamed: {file_name} -> {new_name}")

def main() :
    add_numeration()

if __name__ == '__main__':
    main()