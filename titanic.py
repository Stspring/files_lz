#библиотека для работы с таблицами и анализа данных.
import pandas as pd

#нужна для построения гистограммы
import matplotlib.pyplot as plt

#указываем путь к файлу из которого будем брать данные
file_path = 'titanic.parquet'  

#читаем файл .parquet и загружаем его в таблицу
df = pd.read_parquet(file_path)

#выводим первые строки таблицы, чтобы увидеть её структуру
print(df.head())

#переводим данные в CSV
csv_output_path = 'titanic.csv'

 #сохраняем
df.to_csv(csv_output_path, index=False, encoding='utf-8')  

#вывожу сообщение о том что файл успешно сохранен
print(f'Файл сохранен как: {csv_output_path}')                 

#указываем путь к файлу
csv_file_path = 'titanic.csv' 
                   
#загружаем данных из файла csv для анализа в таблице
df = pd.read_csv(csv_file_path)

#группируем данные по столбцам(класс билета и выжил или не выжил)
#считаем количество людей в каждой группе
#преобразуем таблицу так чтобы столбцы показывали выжил ли человек(1 - да, 0 - нет)
survival_counts = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

#вычисляем проценты выживания для каждого класса
survival_percentage = survival_counts.div(survival_counts.sum(axis=1), axis=0) * 100

#создаем гистограмму(задаю цвета(карасный - не выжил, зеленый - выжил),размеры
survival_percentage.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'],  figsize=(10, 6))

plt.title('Выживаемость пассажиров Титаника')       #названия заголовка гистограммы
plt.xlabel('Класс билета')                          #названия столбцов диограммы(подписи по Х)
plt.xticks(rotation=0)                              #убираю наклон по оси Х
plt.legend(['Не выжили', 'Выжили'])                 #легенда

#настройка оси Y на проценты в графике
#plt.gca() использую для создания оси для этого графика
#дальше задается формат с помощью lamda(она будет значением метки(то есть к числу доваляется знак процента)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))

#задаю придел по У( чтобы проценты отображались от 0 до 100)
plt.ylim(0, 100)

#отображаем гистограмму
plt.tight_layout()
plt.show()