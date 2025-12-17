import re  # Импортируем модуль для работы с регулярными выражениями

class TextAnalyzer: #Класс для анализа текста, принимает строку и предоставляет методы для её анализа
    def __init__(self, text): # Конструктор класса: сохраняем исходный текст
        self.text = text

    def count_words(self):
        # Метод для подсчёта количества слов в тексте
        # Используем регулярное выражение для извлечения слов (только буквы и цифры)
        words = re.findall(r'\b\w+\b', self.text)
        return len(words) # Возвращаем количество найденных слов

    def longest_word(self):
        # Метод для поиска самого длинного слова
        words = re.findall(r'\b\w+\b', self.text) # Извлекаем все слова
        if not words: # Если слов нет, возвращаем пустую строку
            return ""
        # Находим слово с максимальной длиной с помощью функции max()
        return max(words, key=len)

    def replace_word(self, old_word, new_word):
        # Метод для замены всех вхождений слова old_word на new_job
        # Используем регулярное выражение с флагом \b (границы слова), чтобы не заменять части слов
        pattern = r'\b' + re.escape(old_word) + r'\b'
        self.text = re.sub(pattern, new_word, self.text)
        return self.text # Возвращаем обновлённый текст