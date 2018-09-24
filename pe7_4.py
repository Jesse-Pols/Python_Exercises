import sys

def Menu():
    i = int(input('Kies een optie:\n1. Nieuwe naam toevoegen\n2. Huidige lijst inzien\n3. Sluiten\n'))
    if i == 1:
        NewName()
    if i == 2:
        ReadNames()
    if i == 3:
        sys.exit(0)
    if i != 1 or i != 2 or i != 3:
        print('\nDeze optie bestaat niet.')
        Menu()

def NewName():
    new_name = input('Welke naam wilt u toevoegen?\n')
    with open('hardlopers.txt', 'a') as f:
        f.write(new_name + '\n')
        print('{} succesvol toegevoegd.\n'.format(new_name))
    Menu()

def ReadNames():
    try:
        with open('hardlopers.txt', 'r') as f:
            print(f.read())
    except:
        print('Het bestand bestaat niet.\n')
    Menu()


Menu()