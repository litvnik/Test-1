VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

input_str = input("Введите слова через пробел: ")
words = input_str.split()

if not words:
    print("Список слов пуст.")
else:
    word_vowel_count = {}
    for word in words:
        count = sum(1 for char in word if char in VOWELS)
        word_vowel_count[word] = count
    max_vowels = max(word_vowel_count.values())
    words_with_max_vowels = [word for word, count in word_vowel_count.items() if count == max_vowels]
    
    print("\nСловарь {слово: количество гласных}:")
    print(word_vowel_count)
    print(f"\nМаксимальное количество гласных: {max_vowels}")
    print("Слова с максимальным количеством гласных:")
    print(words_with_max_vowels)