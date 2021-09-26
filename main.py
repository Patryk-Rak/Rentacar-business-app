def anagrams(word, words):

    sorted_word = sorted(word)
    str2 = ''.join(str(e) for e in sorted_word)
    sorted_words = []
    result = []

    for element in words:
        sorted_element = sorted(element)
        str1 = ''.join(str(e) for e in sorted_element)
        sorted_words.append(str1)

    for element2 in sorted_words:
        if element2 in str2:
            result.append(element2)

    return result


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(sorted("cba"))