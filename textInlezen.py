file_name = 'kaartnummers.txt'
with open(file_name) as f:
    data = f.readlines()

print(data)
namen = data[0]
