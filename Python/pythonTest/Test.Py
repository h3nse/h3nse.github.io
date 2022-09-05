userName = input('Hvad er dit navn? ')
userAge = input('Hvor gammel er du? ')
userHeight = input('Hvor høj er du? ')
userHeight = int(userHeight)

if userHeight <= 170:
    (isTall := "lav")
else:
    (isTall := "høj")


print(f'Hej {userName} du er {userAge} år gammel og er {isTall}')