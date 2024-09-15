Hi, this is set of few scripts to help me menage file naming convention that is use full in my use case.
My use case:
- all white spaces must be replaced by underscore;
- after first occurrence of underscore in file name, there must be 3 digit number, between 001 and 999, for example: GoproFootage_002_some_description_of_the_file_content.mp4

Scripts overview:
- untended use is to copy scripts to specific folder where I keep my files and run them in specific order;
- folder should contain only files that I'm interested in to change theirs names;

1. SpaceToFloor.py
- changes all white spaces in file name, in all files, in folder from which it was lunched;
- changes only file name where first white space is detected after string of non white space characters, for example GoProFootage some description.mp4
- if in file name instead of white space, underscore is detected, script will skip this file

2. AddNum.py
- add numeration to every file where underscore is detected, GoproFootage_some_description.mp4 -> GoproFootage_002_some_description.mp4
- if no underscore is detected , file will be skipped
- checks all file names for existing numeration, if numeration is detected, script will add numeration only to files without it;
- if existing numeration is detected, scripts continues numeration further iterating it;
- user can provide optional parameter when running script from terminal to start numeration from different number than 1 or max value of existing numeration

3. DelNum.py
- deletes numeration for all files in the folder, used to undo changes done by AddNum.py

4. RepStr.py
- intended to use in terminal
- accepts 2 strings as parameters and changes file names in folder
- first string is to be searched for in all file names in folder
- if string is detected it wil replaced by the second string parameter

ToDo:
AddNum.py:
- add functionality to detect first string of characters before underscore as key and keep/add separate numeration to files with different names in the same folder
