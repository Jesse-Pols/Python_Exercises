leeftijd = int(input("Geef je leeftijd: "))
paspoort = input("Nederlands paspoort (Ja / Nee): ").lower()

if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Je mag niet stemmen!")