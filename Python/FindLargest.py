inputCheck = True
while(inputCheck): 
    talStr = input ("Hvilke tal?(Separer med mellemrum)")
    talStr = talStr.split()
    tal = []
    for i in talStr:
        try:
            i = float(i)
            tal.append(i)
            inputCheck = False
        except:
            print("Nogle værdier er ikke korrekte tal, prøv igen")
            break
    

largestNumber = tal[1]
for n in tal:
    if(n > largestNumber):
        largestNumber = n

smallestNumber = tal[1]
for n in tal:
    if(n < smallestNumber):
        smallestNumber = n

print(f"Det største tal er {largestNumber} og det mindste tal er {smallestNumber}")