from text_processing.text_analyzer import TextAnalyzer # Импортируем класс TextAnalyzer из модуля text_analyzer
from text_processing.text_transformer import to_uppercase, to_lowercase, remove_stop_words, transform_words # Импортируем функции из модуля text_transformer

sample_text = "В лесу родилась ёлочка, в лесу она росла. Зимой и летом стройная, зелёная была" # Исходный русскоязычный текст для анализа
analyzer = TextAnalyzer(sample_text) # Создаём объект класса TextAnalyzer, передавая ему текст

# Выводим исходный текст
print("Исходный текст:")
print(analyzer.text)

print("\nКоличество слов:", analyzer.count_words()) # Выводим количество слов в тексте
print("\nСамое длинное слово:", analyzer.longest_word()) # Выводим самое длинное слово в тексте

# Заменяем слово "ёлочка" на "сосенка" (с учётом регистра и границ слова)
print("\nТекст после замены 'ёлочка' на 'сосенка':")
new_text = analyzer.replace_word("ёлочка", "сосенка")
print(new_text)

updated_analyzer = TextAnalyzer(new_text) # Создаём новый анализатор с обновлённым текстом (чтобы не терять результат замены)

# Преобразуем текст в верхний регистр
print("\nТекст в верхнем регистре:")
print(to_uppercase(updated_analyzer.text))

# Преобразуем текст в нижний регистр
print("\nТекст в нижнем регистре:")
print(to_lowercase(updated_analyzer.text))

# Удаляем часто употребляемые русские слова (стоп-слова)
print("\nТекст без стоп-слов:")
print(remove_stop_words(updated_analyzer.text))

# Применяем lambda-функцию через transform_words: делаем каждое слово с заглавной буквы
print("\nКаждое слово с заглавной буквы (с использованием lambda и map):")
capitalized_text = transform_words(updated_analyzer.text, lambda word: word.capitalize())
print(capitalized_text)