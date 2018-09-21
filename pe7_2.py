with open('kaartnummers.txt') as f:
    for x in f.readlines():
        print(x[8:-1] + ' heeft kaartnummer: ' + x[:6])
# Het bestand sluit automatisch na gebruik