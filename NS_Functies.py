def standaardtarief(afstandKM):
    prijs = 0

    if afstandKM >= 50:
        prijs += 15.00
        for x in range(afstandKM - 50):
            prijs += 0.60
    if afstandKM > 0 and afstandKM < 50:
        for x in range(afstandKM):
            prijs += 0.80

    return round(prijs, 2)

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardtarief(afstandKM)
    print("\nStandaard tarief: \n€ " + str(prijs))

    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            prijs -= prijs * 0.35
            print("Met 35% korting: ")
        else:
            prijs -= prijs * 0.40
            print("Met 40% korting: ")
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs -= prijs * 0.30
            print("Met 30% korting: ")
        else:
            print("Met 0% korting: ")

    return round(prijs, 2)

def Test(leeftijd, weekendrit, afstand):
    print('\n--- Nieuwe test-situatie ---')
    print('Afstand = ' + str(afstand) + ' km')
    print('Leeftijd = ' + str(leeftijd) + ' jaar oud')
    print('Weekend = ' + str(weekendrit))

    print("€ " + str(ritprijs(leeftijd, weekendrit, afstand)))

# De leeftijd, of het weekend is en het aantal kilometers:
Test(18, True, 15)
Test(20, True, 52)
Test(25, False, 15)
Test(40, False, 70)
Test(12, True, 100)
Test(8, False, 5)
Test(69, True, 80)
Test(80, False, 2)


## afstandKM = int(input("Afstand in kilometers: "))
## leeftijd = int(input("Leeftijd: "))
## weekendrit = str(input("Weekend (Ja / Nee): ")).lower()
## if weekendrit == "ja":
##     weekendrit = True
## else:
##     weekendrit = False

## print("€ " + str(ritprijs(leeftijd, weekendrit, afstandKM)))