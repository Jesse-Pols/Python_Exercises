def menu():
    chosen_option = int(input("1: Ik wil weten hoeveel kluizen er nog vrij zijn\n"
                              "2: Ik wil een nieuwe kluis\n"
                              "3: Ik wil even iets uit mijn kluis halen\n"
                              "4: Ik geef mijn kluis terug\n"
                              "5: Ik wil stoppen\n"))
    if chosen_option == 1:
        print(toon_aantal_kluizen_vrij())
    if chosen_option == 2:
        print(nieuwe_kluis())
    if chosen_option == 3:
        print(kluis_openen())
    if chosen_option == 4:
        print(kluis_teruggeven())
    if chosen_option == 5:
        exit()
    if chosen_option not in range(1, 6):
        print("Deze optie bestaat niet.\nKies alstublieft een andere optie.")
        menu()

    return_to_menu = int(input("1: Ik wil terug naar het menu\n"
                               "2: Ik wil stoppen\n"))
    if return_to_menu == 1:
        menu()
    else:
        exit()


def toon_aantal_kluizen_vrij():
    used_lockers = sum(1 for line in open("kluizen.txt"))
    if used_lockers >= 12:
        return "Er zijn geen kluizen meer vrij."
    else:
        return "Er zijn nog {} kluizen vrij.".format(12 - used_lockers)


def nieuwe_kluis(kluis_code=None):
    if sum(1 for line in open("kluizen.txt")) < 12:
        locker_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        with open("kluizen.txt", "r") as f:
            for x in f.readlines():
                locker_nr = x.split(';')[0]
                locker_list.remove(int(locker_nr))

        if not kluis_code:
            kluis_code = input("Voer een code in voor de kluis:\n")
        with open('kluizen.txt', 'a') as f:
            f.write("{};{}\n".format(locker_list[0], kluis_code))
            return 'Je hebt kluis {} gekregen.'.format(locker_list[0])
    else:
        return "Er zijn geen kluizen meer vrij."


def kluis_openen(kluis_nr=None, kluis_code=None):
    if not kluis_nr:
        kluis_nr = input("Kluisnummer:\n")
    if not kluis_code:
        kluis_code = input("Code:\n")

    with open('kluizen.txt', 'r') as f:
        for x in f.readlines():
            locker = x.split(';')
            if locker[0] == kluis_nr and locker[1] == kluis_code + "\n":
                return 'Je hebt toegang tot je kluis.'

    return "We hebben geen kluis kunnen vinden met dit nummer en deze code."


def kluis_teruggeven(kluis_nr=None, kluis_code=None):
    if not kluis_nr:
        kluis_nr = input("Kluisnummer:\n")
    if not kluis_code:
        kluis_code = input("Code:\n")

    return_value = 'We hebben geen kluis kunnen vinden met dit nummer en deze code.'

    with open('kluizen.txt', 'r') as f:
        lines = f.readlines()
    with open('kluizen.txt', 'w') as w:
        for line in lines:
            if line != "{};{}\n".format(kluis_nr, kluis_code):
                w.write(line)
            else:
                return_value = 'De kluis is geleegd en beschikbaar voor anderen.'
    return return_value


# Als het bestand niet bestaat wordt het automatisch aangemaakt
try:
    open('kluizen.txt', 'x').close()
except:
    pass


# Welke functie te testen: 0 = Script van voren af aan runnen, 1 = Kluizen checken, 2 = Een kluis claimen, 3 = Kluis openen, 4 = Kluis teruggeven
# Welke kluis te checken/aan te vragen
# Welke code in te voeren/ stellen
def tester(functie, kluis_nr=None, kluis_code=None):
    if functie == 0:
        menu()
    if functie == 1:
        return toon_aantal_kluizen_vrij()
    if functie == 2:
        return nieuwe_kluis(kluis_code)
    if functie == 3:
        return kluis_openen(kluis_nr, kluis_code)
    if functie == 4:
        return kluis_teruggeven(kluis_nr, kluis_code)


##############################################
# Zorg dat kluizen.txt leeg of verwijdert is #
##############################################

print(tester(1, "", "") == "Er zijn nog 12 kluizen vrij.")
print(tester(2, "", "sample") == "Je hebt kluis 1 gekregen.")
# kluizen.txt
# 1;sample

print(tester(3, "1", "sample") == "Je hebt toegang tot je kluis.")
print(tester(3, "1", "sampel") == "We hebben geen kluis kunnen vinden met dit nummer en deze code.")
print(tester(3, "2", "sample") == "We hebben geen kluis kunnen vinden met dit nummer en deze code.")
print(tester(1, "", "")        == "Er zijn nog 11 kluizen vrij.")
print(tester(2, "", "s@mple2.0") == "Je hebt kluis 2 gekregen.")
# kluizen.txt
# 1;sample
# 2;sample2

print(tester(1, "", "")        == "Er zijn nog 10 kluizen vrij.")
print(tester(4, "1", "sample") == "De kluis is geleegd en beschikbaar voor anderen.")
# kluizen.txt
# 2;sample2

print(tester(1, "", "")         == "Er zijn nog 11 kluizen vrij.")
print(tester(4, "2", "s@mple2.0") == "De kluis is geleegd en beschikbaar voor anderen.")
# kluizen.txt

# Om het programma van voren af aan te runnen:
print('\nHet hele programma:')
print(tester(0, "", ""))
