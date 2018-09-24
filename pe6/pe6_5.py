def kwadraten_som(grondgetallen):
    result = 0
    for x in grondgetallen:
        if x > 0:
            result = result + (x ** 2)

    return result


print(kwadraten_som([4, 5, 3, -81]))