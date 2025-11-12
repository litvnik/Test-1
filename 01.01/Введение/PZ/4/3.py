import string
text = input("Введите текст: ")

translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator)
words = cleaned_text.lower().split()

freq_dict = {}
for word in words:
    if word:  # игнорируем пустые строки (на случай нескольких пробелов)
        freq_dict[word] = freq_dict.get(word, 0) + 1
print("Частотный словарь:")
print(freq_dict)