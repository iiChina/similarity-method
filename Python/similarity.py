string1 = input()
string2 = input()


def ArrayStrings(text):
    array = [text[i:i+2] for i in range(len(text) - 1)]

    return array


def word_letter_pairs(s):
    all_pairs = []

    # Tokenize the string and put the tokens/words into an array
    words = s.split()

    # Para cada palavra
    for word in words:
        # Encontre os pares de caracteres
        pairs_in_word = ArrayStrings(word)

        # Adicione os pares à lista de todos os pares
        all_pairs.extend(pairs_in_word)

    return all_pairs


def compareStrings(text1, text2):
    texts1 = word_letter_pairs(text1.upper())
    texts2 = word_letter_pairs(text2.upper())

    intersection = 0
    cont = 0
    union = len(texts1) + len(texts2)

    for i in texts1:
        for n in texts2:
            if i == n:
                intersection += 1
                del texts2[cont]

                break

    return ((2 * intersection) / union) * 100


print(compareStrings(string1, string2))
