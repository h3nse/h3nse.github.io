while(True): 
    talStr = input ("Hvilke tal?(Separer med mellemrum)")
    talStr = talStr.split()
    tal = []
    for i in talStr:
        try:
            i = float(i)
            tal.append(i)
        except:
            print("Nogle værdier er ikke korrekte tal, prøv igen")
            continue
    break

largestNumber = 0
for n in tal:
    if(n > largestNumber):
        largestNumber = n

print(f"Det største tal er {largestNumber}")