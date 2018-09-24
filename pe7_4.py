import sys
import datetime

def Menu():
    i = int(input('Kies een optie:\n1. Nieuwe naam toevoegen\n2. Huidige lijst inzien\n3. Bestand legen\n4. Sluiten\n'))
    if i == 1:
        NewName()
    if i == 2:
        ReadNames()
    if i == 3:
        ClearFile()
    if i == 4:
        sys.exit(0)
    if i != 1 or i != 2 or i != 3 or i != 4:
        print('\nDeze optie bestaat niet.')
        Menu()

def NewName():
    #Current time & date
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %T, ")

    new_name = input('Welke naam wilt u toevoegen?\n')
    with open('hardlopers.txt', 'a') as f:
        f.write('{}{}\n'.format(s, new_name))
        print('{} succesvol toegevoegd.\n'.format(new_name))
    Menu()

def ReadNames():
    try:
        with open('hardlopers.txt', 'r') as f:
            print(f.read())
    except:
        print('Het bestand bestaat niet.\n')
    Menu()

def ClearFile():
    open('hardlopers.txt', 'w').close()
    print('Bestand geleegd.\n')
    Menu()

Menu()