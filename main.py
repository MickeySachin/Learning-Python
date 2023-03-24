# 20th March 2023
# Sachin

'''
# *********************************************************************** String formatting
var = 'Python environment'
print(f'You are working on {var} !')  # Formatted string
print('First name = {fname}, rollno = {rn}'.format(fname = 'Deshraj', rn = 33))  # String formatting using format() 


# *********************************************************************** List
names = ['sachin', 'soham', 'saurabh']
print(names)
nameLength = names.__len__()
print(names[1])
print(names[-1:])

def fuck(s):
    print(s, "is fucked up!")  # comma inserts a space in output stream

for i in range(nameLength):  # range( 0 to n-1 )
    fuck(names[i])
    if(i == (nameLength-1)):
        print("Everyone's fuck fucka fuck fuck!!!")

print()
ls1 = [3, 5, 6, 'Sachin']

ls1Copy = ls1  # both the lists refer to same memory location thus changes reflects in both lists
ls1Copy.append("Desu")
print("Lists after append() -")
print(ls1)
print(ls1Copy)

ls1SecondCopy = ls1.copy()  # copy() creates separate list thus refers to separate memory location 
ls1SecondCopy.append('soham')
print("\nLists after copy() -")
print(ls1)
print(ls1SecondCopy)


# *********************************************************************** List comprehension
listA = [i * i for i in range(1, 10)]
print(listA)


# *********************************************************************** Lambda functions
evenNo = lambda x : x % 2 == 0

for i in range(1, 11):
    print(f'{i} is an even number - {evenNo(i)}')


points = [(1, 3), (3,2), (4, -2), (-1, 9)]

sortedPoints = sorted(points, key= lambda x : x[1])  # sorts the list w.r.t 'y-coordinate' of 'points' (x, y)
print(f'points = {points}')  
print(f'sortedPoints = {sortedPoints}')  


# *********************************************************************** 2d list(matrix)
matrix = [
    [2, 4, 5],
    [4, 5, 8]
]
matrixRows = 2
matrixColumns = 3
colCount = 0

print('Matrix = ')

for row in matrix:
    for item in row:
        print(item, end="   ")
        colCount += 1

        if colCount == matrixColumns:
            print()

            
# *********************************************************************** Unpacking - for tuples and lists
coord = (1, 3, 5)
x, y, z = coord
print(f"Coordinates = ({x}, {y}, {z})")


# *********************************************************************** Dictionaries
digit = {
    "1" : 'One',
    '2' : "Two",
    "3" : 'Three'
}

digit['4'] = 'Four'

print(digit.get('5', 'Five'))  # 5 key isn't added to dict 'digit'

print(digit['1'])

for i in range(1, 6):
    print(digit['{i}'.format(i = i)])


# *********************************************************************** Phone number into words
digit = {
    "0" : 'Zero',
    "1" : 'One',
    '2' : "Two",
    "3" : 'Three',
    "4" : 'Four',
    "5" : 'Five',
    "6" : 'Six',
    "7" : 'Seven',
    "8" : 'Eight',
    "9" : 'Nine'
}

pNo = input("Enter your number = ")
output = ''
for i in pNo:
    # print(digit['{i}'.format(i = i)], end=' ')
    output += digit.get(i, "!") + " "

print(output)


# *********************************************************************** Exception handling
try:
    num1 = int (input('Enter a number = '))
    num2 = int (input('Enter another number = '))
    div = num1 // num2
    print(f'{num1} // {num2} = {div}')

except ZeroDivisionError:
    print("Dividing by zero!")

except ValueError:
    print("Values must be numeral!")


# *********************************************************************** Class
class stu:
    # id, name, rollno = '', '', ''

    # def __init__(self):
    #     self.id = int(input("Enter Student Id = "))
    #     self.name = input("Enter Studnet Name = ")
    #     self.rollno = int(input("Enter Student Rollno = "))

    def __init__(self):
        self.id = []
        self.name = []
        self.rollno = []
        self.countEntries = 0

    def getData(self):
        flag = 1

        while flag != 0:
            self.id.append(input("Enter Student Id = "))
            self.name.append(input("Enter Student Name = "))
            self.rollno.append(input("Enter Student Rollno = "))
            flag = int(input("Enter 1 to add new detail while 0 to exit = "))
            self.countEntries += 1


    def printColumnHeading(self):
        print("Id - Name - Rollno")


    def printData(self, count):
        count = self.countEntries

        for i in range(count):
            print(f' {self.id[i]} - {self.name[i]} - {self.rollno[i]}')



s1 = stu()

s1.getData()
s1.printColumnHeading()
s1.printData(s1.countEntries)


# *********************************************************************** Modules
import module1
from module1 import stuMethods
from module1 import basicOperations


# module1.stuMethods.getData()  # when entire 'module1' is imported
# stuMethods.getData()  # when only 'stuMethods' is imported 

print(basicOperations.addition(3, 6))
print(basicOperations.subtraction(3, 6))
print(basicOperations.multiplication(3, 6))
print(basicOperations.division(3, 6))


# *********************************************************************** Random module
import random

print("Use of random() - ", end="")
for i in range(4):
    print(random.random(), end=', ')  # random() returns random floating values between 0 and 1

print()

print("Use of randint() - ", end="")
for i in range(4):
    print(random.randint(5, 10), end=', ')  # randint(start, stop) returns random integer values 

print()
players = ['sachin', 'desu', 'saurabh', 'soham']
print("{x}'s turn!".format(x= random.choice(players)))  # choice(listName) returns a random element from specified list


# *********************************************************************** Directories and files
from pathlib import Path

# Absolute Path - Containing complete path including root
# Relative path - Sepcifying file name

path1 = Path()  # Current directory
path1 = Path('module1.py')
print(f'Path specified by path1 variable exists or not? - {path1.exists()}')

path1 = Path('test')
path1.mkdir()
if path1.exists():  # mkdir() to create directory  
    print('Directory created successfully!')

path1.rmdir()
if not path1.exists():  # mrdir() to remove directory
    print('Directory removed successfully!')

path1 = Path('test.py')
# path1 = Path('test.py').unlink()  # unlink() deletes file

path1 = Path()
print("List of all files and directories in current directory = ")
for file in path1.glob('*'):  # glob(arg) used to traverse in a directory - (* - means everything under current directory, *.ext - specific extension files)
    print(file)

'''


