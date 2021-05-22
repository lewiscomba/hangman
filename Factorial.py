import getopt, sys


#my comment 222

# Ask the user to enter the names of files to compare
number = input("Enter the a number: ")

while 1 == 1:
    if number != '':
        prod = 1
        for i in range(1,int(number)+1):
            prod *= i
        print('El numero factorial es: ', prod)
        number = input("Enter the a number: ")
    else:
        break