titleGraphic = "= = = FIZZBUZZ = = ="
playingGame = True

def FizzOrBuzz(number):
    output = ''
    
    if number % 3 == 0:
        output = 'F'
    
    if number % 5 == 0:
        output = output + 'B'
    
    return output

def FizzBuzz(n):
    finalOutput = FizzOrBuzz(n)
    if not finalOutput:
        return str(n)
    else:
        return finalOutput

def CheckInputCorrectness(userInput, currentNumber):
    if FizzBuzz(currentNumber) == userInput.upper():
        return True
    else:
        return False

def GM1(titleGraphic):
    currentNumber = 1
    while True:
        print(titleGraphic, 'Start counting! (F = fizz | B = buzz | FB = fizzbuzz)', sep='\n')
        userInput = input()

        if CheckInputCorrectness(userInput, currentNumber):
            currentNumber = currentNumber + 1
            continue
        else:
            print('Wrong answer! better luck next time')
            break

def GM2(titleGraphic):
    currentNumber = 1
    print(titleGraphic, 'Start counting, Ill say the next number! (F = fizz | B = buzz | FB = fizzbuzz)', sep='\n')
    while True:
        userInput = input()

        if CheckInputCorrectness(userInput, currentNumber):
            currentNumber = currentNumber + 1
        else:
            print('Wrong answer! better luck next time')
            break
        
        print(titleGraphic, 'Start counting, Ill say the next number! (F = fizz | B = buzz | FB = fizzbuzz)', sep='\n')
        print(FizzBuzz(currentNumber))
        currentNumber = currentNumber + 1

while playingGame:
    while True:
        print('How would you like to play?...', titleGraphic, '1. Count for yourself or with a friend', '2. Count against the computer', sep='\n')
        gameSelect = input()
        
        if gameSelect == '1':
            GM1(titleGraphic)
            break
        elif gameSelect == '2':
            GM2(titleGraphic)
            break
        else:
            print('That is not a valid response, please try again...')
            continue
    while True:
        print('Thank You For Playing...', titleGraphic, 'Would you like to play again? (y/n)', sep='\n')
        playAgain = input()

        if playAgain.lower() == 'y':
            break
        elif playAgain.lower() == 'n':
            playingGame = False
            break
        else:
            print('That is not a valid response, please try again...')
            continue