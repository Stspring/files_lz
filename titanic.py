import pandas as pd
import matplotlib.pyplot as plt
file_path = 'titanic.parquet'  
# Чтение файла .parquet
df = pd.read_parquet(file_path)
# Выводим первые строки набора данных, чтобы увидеть его структуру
print(df.head())
# Сохранение данных в формате .csv
csv_output_path = 'titanic.csv'
df.to_csv(csv_output_path, index=False, encoding='utf-8')
print(f'Файл сохранен как: {csv_output_path}')
csv_file_path = 'titanic.csv'  
# Чтение данных из файла .csv
df = pd.read_csv(csv_file_path)
# Группируем данные по классу билета и считаем количество выживших и не выживших
survival_counts = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
# Вычисляем проценты выживания для каждого класса
survival_percentage = survival_counts.div(survival_counts.sum(axis=1), axis=0) * 100
# Создаем гистограмму
survival_percentage.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'],
                     figsize=(10, 6))
# Настраиваем заголовок и метки
plt.title('Выживаемость пассажиров Титаника')
plt.xlabel('Класс билета')
plt.xticks(rotation=0)
plt.legend(['Не выжили', 'Выжили'])
# Настройка оси Y на проценты
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))
plt.ylim(0, 100)
# Отображаем гистограмму
plt.tight_layout()
plt.show()