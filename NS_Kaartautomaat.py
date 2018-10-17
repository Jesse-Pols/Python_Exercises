
def inlezen_beginstation(stations, tester, beginstation=None):
    if not beginstation:
        beginstation = input('Wat is je beginstation?\n').title()

    if beginstation not in stations:
        if not tester:
            print('Dit station is geen onderdeel van het traject.')
            return inlezen_beginstation(stations, tester)
        return 'Beginstation bestaat niet.'
    return beginstation

def inlezen_eindstation(stations, tester, beginstation, eindstation = None):
    if not eindstation:
        eindstation = input('Wat is je eindstation?\n').title()
    if eindstation not in stations:
        if not tester:
            print('De trein komt niet in {}.'.format(eindstation))
            return inlezen_eindstation(stations, tester, beginstation)
        return 'Eindstation bestaat niet.'

    if stations.index(eindstation) < stations.index(beginstation):
        if not tester:
            print('De trein komt niet meer langs {}.'.format(eindstation))
            return inlezen_eindstation(stations, tester, beginstation)
        return 'Eindstation ligt voor beginstation.'
    return eindstation

def omroepen_reis(stations, tester, beginstation, eindstation):
    index_beginstation = stations.index(beginstation) + 1
    index_eindstation = stations.index(eindstation) + 1
    afstand = index_eindstation - index_beginstation
    kosten = afstand * 5

    if not tester:
        print('Het beginstation {} is het {}e station in het traject.\n'
            'Het eindstation {} is het {}e station in het traject.\n'
            'De afstand bedraagt {} stations.\n'
            'De prijs van het kaartje is {} euro.'.format(beginstation, index_beginstation, eindstation, index_eindstation, afstand, kosten))

        print('\nJe stapt in de trein in: {}'.format(beginstation))
        for x in range(index_beginstation, index_eindstation - 1):
            print(' - {}'.format(stations[x]))
        print('Je stapt uit in: {}'.format(eindstation))
    return [index_beginstation, index_eindstation, afstand, kosten]

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'S-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def Run(stations, tester=False, beginstation = None, eindstation = None):
    beginstation = inlezen_beginstation(stations, tester, beginstation)
    if beginstation == 'Beginstation bestaat niet.':
        return beginstation
    if beginstation == 'Maastricht':
        print('Dit is het eindstation, u kunt niet verder reizen.')
        return

    eindstation = inlezen_eindstation(stations, tester, beginstation, eindstation)
    if eindstation == 'Eindstation bestaat niet.' or eindstation == 'Eindstation ligt voor beginstation.':
        return eindstation
    if eindstation != beginstation:
        omgeroepen_data = omroepen_reis (stations, tester, beginstation, eindstation)
    else:
        print("Het beginstation is het zelfde als het eindstation.\nKaartje is € 0,-.")
        return

    return '{} = {}e station, {} = {}e station, afstand = {}, kosten = €{},-.'.format(beginstation, omgeroepen_data[0], eindstation, omgeroepen_data[1], omgeroepen_data[2], omgeroepen_data[3])

# Run(stations, tester, beginstation, eindstation)
# tester bepaalt of de print statements afgedrukt worden, True is niet, leeglaten of False is wel
print(Run(stations, True, 'Alkmaar', 'Zaandam') == 'Alkmaar = 3e station, Zaandam = 5e station, afstand = 2, kosten = €10,-.')
print(Run(stations, True, 'Alkmaar', 'Amsterdam Centraal') == 'Alkmaar = 3e station, Amsterdam Centraal = 7e station, afstand = 4, kosten = €20,-.')
print(Run(stations, True, 'Schagen', 'Maastricht') == 'Schagen = 1e station, Maastricht = 15e station, afstand = 14, kosten = €70,-.')
print(Run(stations, True, 'Schagen', '\'S-Hertogenbosch') == 'Schagen = 1e station, \'S-Hertogenbosch = 10e station, afstand = 9, kosten = €45,-.')
print(Run(stations, True, 'Zaandam', 'Alkmaar') == 'Eindstation ligt voor beginstation.')
print(Run(stations, True, 'Zandaam', 'Alkmaar') == 'Beginstation bestaat niet.')
print(Run(stations, True, 'Zaandam', 'Utregt') == 'Eindstation bestaat niet.')
print(Run(stations, True, 'Overal', 'Nergens') == 'Beginstation bestaat niet.')
# Het eindstation wordt niet gecheckt als het beginstation niet bestaat.
print('\nNormale output:')
Run(stations, False, 'Alkmaar', 'Amsterdam Centraal')

# Run(stations) hoeft niet geprint te worden omdat de return waarde alleen uitmaakt bij het testen.
print('\nHet programma normaal runnen:')
Run(stations)