def seizoen(maand):
    if 3 <= int(maand) <= 5:
        print('Lente')
    if 6 <= int(maand) <= 8:
        print('Zomer')
    if 9 <= int(maand) <= 11:
        print('Herfst')
    if 1 <= int(maand) <= 2 or int(maand) == 12:
        print('Winter')

maand = int(input('Voer een maandnummer in\n'))
seizoen(maand)