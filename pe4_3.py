#Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur dat hij of zij gewerkt heeft en dat daarna het salaris uitprint.

print('Wat is je uurloon?')
uurloon = input()

print('Hoeveel uur heb je gewerkt?')
uren = input()

salaris = float(uurloon) * float(uren)
print('\nUurloon: ' + str(uurloon) + '\nUren: ' + str(uren) + '\nSalaris: ' + str(salaris))