import sys

#Program veksler fra DKK til Euro med en kommision på 2% eller 0.5, hvadend der er højest
while(True): 
    kroner = input ("Hvor mange kroner?")
    try:
        kroner = float(kroner)
        break
    except:
        print("Det er ikke en korrekt værdi, prøv igen")

euro = kroner * 0.13

if(euro/50 < 0.5):
    kommision = 0.5
else:
    kommision = euro/50

euroTilbage = euro - euro/50
print(f"Du får {euroTilbage} euro tilbage")

