from lib2to3.pgen2.token import NEWLINE
from msilib.schema import tables
from math import *


def counting():

    #Input validation
    while(True):
        countFromStr = input('What number should I count from?')
        countToStr = input('What  number should I count to?')
        try:
            countFrom = int(countFromStr)
            countTo = int(countToStr)
        except:
            print('Invalid input, please try again with a whole number...')
            continue
        break

    #Find difference
    if(countFrom < countTo):
        change = 1
    elif(countFrom > countTo):
        change = -1
    else:
        print('There is no difference between the numbers')
        return

    print(f"Counting from {countFrom} to {countTo}...")
    difference = abs(countFrom - countTo)
        
    #Count in range(difference)
    for i in range(difference + 1):
        print(countFrom + i*change)

    return

def TriangularNumbers():

    #Input validation
    while(True):
        numberStr = input('Which number would you like to find the triangular number for?\n')
        try:
            number = int(numberStr)
        except:
            print('Incorrect input, please try again with a whole number...')
            continue

        if(number < 0):
            print('Incorrect input, please try again with a positive number...')
            continue
        break
    
    #Add i after each iteration and print
    result = 0
    for i in range(number + 1):
        result = result + i
    print('The result is',result)

    return

def Tables():

    #Input validation
    while(True):
        tableStr = input('Which table would you like to see?(type 0 for all tables from 1-10)\n')
        try:
            table = int(tableStr)
        except:
            print('Incorrect input, please try again with a whole number...')
            continue

        if(table < 0):
            print('Incorrect input, please try again with a positive number...')
            continue
        break
    
    #Print all tables from 1-10 (Challenge to make in 1 loop)
    if(table == 0):
        x = 1
        i = 0
        print('table of 1')
        while(True):
            if(i == 10):
                i = 0
                x += 1
                if(x == 11):
                    break
                print('Table of',x)
            i += 1
            print(i*x)

    #Print any table you choose
    else:    
        print('Printing table of',table)
        for i in range(table, table*11, table):
            print(i)

        return

def SecondDegreePolynomialEquation():
    a = 3
    b = 6
    c = 9

    #Input validation
    while(True):
        xStr = input('Which value should x be?(type 0 for all values from 1-10, and then 10-100 stepping by 10)\n')
        try:
            x = int(xStr)
        except:
            print('Incorrect input, please try again with a whole number...')
            continue
        break
    
    #Print for x value 1-10 and 10-100 stepping by 10
    if(x == 0):
        while(True):
            print(f'{a}*{x}^2 + {6}*{x} + {9} =',a*x*x + b*x + c)            
            if(x >= 10):
                x += 10
                if(x > 100):
                    break
                continue
            x += 1

    #Print for any x value you choose
    else:    
        print('Printing with x value of',x)
        print(f'{a}*{x}^2 + {6}*{x} + {9} =',a*x*x + b*x + c)            

    return

#Input verification
Running = True
while(Running):

    #Ask for input
    print('Which program would you like to run?', '1. Counting', '2. Triangular numbers', '3. tables', '4. 2. degree polynomial equation', sep='\n')
    programStr = input('')

    #Try convert input to int, else retry
    try:
        program = float(programStr)
    except:
        print("Incorrect input, please try again...") 
        continue

    #Check which number was picked. if none, retry
    match program:
        case 1:
            counting()
        case 2:
            TriangularNumbers()
        case 3:
            Tables()
        case 4:
            SecondDegreePolynomialEquation()
        case _:
            print("Incorrect input, please try again...")
            continue

    #Ask to try again
    while(True):
        tryAgain = input('Thank you for trying my program, would you like to try another?(y/n)').upper()
        if(tryAgain == 'Y'):
            break
        elif(tryAgain == 'N'):
            Running = False
            break
        else:
            print('That is not a valid response, try again...')
            continue