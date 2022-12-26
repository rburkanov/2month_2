vowels = ["a", "e", "i", "o", "u", "у", "е", "ё", "а", "о", "э", "я", "и", "ю", "ыВЫ"]
consonants = ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m",
              "й", "ц", "к", "н", "г", "ш", "щ", "з", "х", "ф", "в", "п", "р", "л", "д", "ж", "ч", "с", "м", "т", "б"]

amount_of_vowels = 0
amount_of_consonants = 0
letters = 0

while True:
    word = input('Введите слово:').lower()
    if word == 'exit' or word == 'выход':
        print('program finished')
        break
    for i in word:
        if i.isalpha():
            letters = letters + 1
    for char in word:
        if char in vowels:
            amount_of_vowels = amount_of_vowels + 1
        elif char in consonants:
            amount_of_consonants = amount_of_consonants + 1
    print('Количество гласных: ', amount_of_vowels)
    print('Количество согласных: ', amount_of_consonants)
    print('Количество букв: ', letters)
    print(f'Гласные = {round(amount_of_vowels / len(word) * 100, 2)}%', f'Согласные = {round(amount_of_consonants / len(word) * 100, 2)}%', sep='\n')