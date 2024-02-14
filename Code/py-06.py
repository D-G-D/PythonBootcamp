## [PY-06] Programs and modules ##

# The working directory #
%pwd
%cd py_course
%pwd

# Alternative using Python Functions
import os
os.getcwd()
os.chdir('C:\\Users\\dirkg\\OneDrive\\Professional\\Python')
os.chdir(r'C:\Users\dirkg\OneDrive\Professional\Python')

# Program 1 #
print('\nHi, there!\nThis is the Python Course!')

runfile('program1.py')

# input statements #
input('\nDo you know Python? (y/n) ')
int(input('\nWhat is your age? '))

# Program 2 #
answer = input('\nDo you know Python? (y/n) ')

if answer == 'y':
    print('\nCool!!')
else:
    print('\nSorry about that.')
    
runfile('program2.py')

# Modules #
month_list = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']

def convert(date):
    year = date[:4]
    month_no = int(date[5:7])
    month = month_list[month_no - 1]
    day = str(int(date[8:]))
    return month + ' ' + day + ', ' + year

import datestuff
datestuff.convert('1954-04-30')

from datestuff import convert
convert('1954-04-30')
