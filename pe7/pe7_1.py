def Convert(temperatuur):
    return temperatuur * 1.8 + 32

def table():
    print('{:>5}  {:>5}'.format('F', 'C'))
    for x in range(-30, 50, 10):
        print('{:>5}  {:>5}'.format(str(Convert(x)), str(x)))

table()