def NewList(old_list):
    new_list = []
    for x in old_list:
        if len(x) == 4:
            new_list.append(x)
    return new_list

old_list = eval(input("Geef een lijst met minimaal 10 strings: \n"))
print('De nieuw-gemaakte lijst met alle vier-letter strings is:' + str(NewList(old_list)))