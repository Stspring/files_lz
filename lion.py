from collections import Counter
import docx
import re
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'lion.docx'  

# Открываем документ
doc = docx.Document(file_path)
text = []
# Извлекаем текст из каждого абзаца в список
for paragraph in doc.paragraphs:
    text.append(paragraph.text)
# Объединяем все тексты 
full_text = ' '.join(text)
# Удаляем знаки препинания и разбиваем текст на слова
words = re.findall(r'\b\w+\b', full_text.lower())
# Подсчитываем частоту слов
word_count = Counter(words)
# Общее количество слов
total_words = sum(word_count.values())
# Создаем DataFrame из результатов
df_words = pd.DataFrame(word_count.items(), columns=['Слово', 'Частота'])
# Рассчитываем процент встречаемости слов
df_words['Процент'] = (df_words['Частота'] / total_words) * 100
print(df_words)
# Сохранение результатов в CSV файл (по желанию)
output_file_words = 'word_frequency.csv'
df_words.to_csv(output_file_words, index=False, encoding='utf-8')
print(f'Результаты частоты слов сохранены в файл: {output_file_words}')
# Удаляем все, кроме букв русского алфавита, и преобразуем текст в нижний регистр
letters = re.findall(r'[а-яА-ЯёЁ]', full_text.lower())
# Подсчитываем частоту букв
letter_count = Counter(letters)
# Создаем DataFrame из результатов
df_letters = pd.DataFrame(letter_count.items(), columns=['Буква', 'Частота'])
# Рассчитываем процент встречаемости букв
total_letters = sum(letter_count.values())
df_letters['Процент'] = (df_letters['Частота'] / total_letters) * 100
# Построение гистограммы для частоты букв
plt.figure(figsize=(10, 6))
plt.bar(df_letters['Буква'], df_letters['Частота'], color='orange')
plt.title('Частота встречаемости букв')
plt.xlabel('Буквы')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.grid(axis='y')
# Отображаем гистограмму для букв
plt.tight_layout()
plt.show()