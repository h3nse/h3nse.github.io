while(True): 
    talStr = input ("Hvilke tal?(Separer med mellemrum)")
    tal = []
    try:
        talStr = talStr.split()
    except:
        print("værdierne er ikke formuleret korrekt... Prøv igen")
        continue
    try:
        for i in talStr:
            i = float(i)
            tal.append(i)
    except:
        print("Nogle værdier er ikke korrekte tal, prøv igen")
        continue
    else:
        break
    

largestNumber = tal[0]
for n in tal:
    if(n > largestNumber):
        largestNumber = n

smallestNumber = tal[0]
for n in tal:
    if(n < smallestNumber):
        smallestNumber = n

print(f"Det største tal er {largestNumber} og det mindste tal er {smallestNumber}")