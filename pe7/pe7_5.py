def gemiddelde():
    sentence = input('Voer een willekeurige zin in:\n')
    words = sentence.split(" ")
    total_length = 0
    for x in words:
        total_length += len(x)
    return total_length / len(words)

print(gemiddelde())