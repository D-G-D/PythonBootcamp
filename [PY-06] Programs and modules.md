# [PY-06] Programs and modules

## The working directory

```
In [1]: %pwd
Out[1]: '/Users/username'
```

```
In [2]: %cd py_course
/Users/miguel/py_course
```

```
In [3]: %pwd
Out[3]: '/Users/miguel/py_course'
```

## Program 1

```
In [4]: print('\nHi, there!\nThis is the Python Course!')

Hi, there!
This is the Python Course!

```

```
In [5]: runfile('program1.py')

Hi, there!
This is the Python Course!
```

## input statements

```
In [6]: input('\nDo you know Python? (y/n) ')

Do you know Python? (y/n) y
Out[6]: 'y'
```

```
In [7]: int(input('\nWhat is your age? '))

What is your age? 25
Out[7]: 25
```

## Program 2

```
answer = input('\nDo you know Python? (y/n) ')

if answer == 'y':
    print('\nCool!!')
else:
    print('\nSorry about that.')
```

```
In [8]: runfile('program2.py')

Do you know Python? (y/n) n

Sorry about that.
```

## Modules

```
def has_zero(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return True
    else:
        return False
```

```
In [9]: import myfuncs
```

```
In [10]: myfuncs.has_zero(1, -2, 0)
Out[10]: True
```

```
In [11]: from myfuncs import has_zero
```

```
In [12]: has_zero(1, -2, 3)
Out[12]: False
```

## Homework

1. The first question of the homework of lecture PY-05 was concerned with calculating the body mass index (BMI), in numeric and categorical scales. Write a program thats asks the user his/her height and weight, specifying the units, and prints *Your BMI is ---, so you are classified as ---*.
