with open('kaartnummers.txt') as f:
    data = f.readlines()
    regels = len(data)
    hoogste_nummer = max(data)[:6]
    hoogste_nummer_regel = data.index(max(data)) + 1

print('Deze file telt {} regels.'.format(regels))
print('Het grootste kaartnummer is: {} en dat staat op regel {}.'.format(hoogste_nummer, hoogste_nummer_regel))

