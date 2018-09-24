#Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt heeft en dat daarna het salaris uitprint.

def Input_Output():
    uurloon = input('Wat is je uurloon?')
    uren = input('Hoeveel uur heb je gewerkt?')

    salaris = float(uurloon) * float(uren)
    print('\nUurloon: ' + str(uurloon) + '\nUren: ' + str(uren) + '\nSalaris: ' + str(salaris))

# Input_Output()