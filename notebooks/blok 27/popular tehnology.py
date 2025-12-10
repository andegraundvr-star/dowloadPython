import pandas as pd
from collections import Counter

# Данные из сообщения
data = """
Keras, Tensorflow, pytorch CV-моделями; создание автоматизаций с применением LLM; IT-кругозор, знание других стеков и языков программирования; 
Опыт использования трекеров (например github/gitlab/jira); Опыт работы с Git / Greenplum деревья решений, бустинги, лог.регрессия, 
различные методы кластеризации, ALS/SVD, методы NLP, нейросети для анализа транзакционных данных, текстовой аналитики, для создания эмбеддингов 
Agile/Scrum в Cфера (аналог Jira и Confluence), Gitlab+BitBucket+MLFlow RAG-системы Docker ML
Deep Learning
Python
Docker
ООП
Git
LLM
RAG
MySQL
Langchain
TensorFlow
Computer Vision
OpenCV
Нейронные сети
Python
PyTorch
Mathematical Programming
3D
С#
С++
Keras
Deep Learning
Git
Работа в команде
Bash
SQL
Исследовательский анализ данных
MLflow
Бизнес-анализ
Python
MLflow
Python
PostgreSQL
Django Framework
FastAPI
Нейронные сети
Python
Linux
GitHub
PostgreSQL
TensorFlow
PyTorch
Numpy
NLTK/SpaCy
Librosa/PyDub
LoRA
Python
OpenCV
Numpy
Знание основных нейросетевых архитектур
Нейронные сети
PyTorch
Git
Docker
Linux
Linux
Docker
Python
Linux
С++
ML
Нейросети
Python
OpenCV
ROS2
Robot Operating System
калибровка сенсоров
ADAS
Беспилотный транспорт
Техническое зрение
Python
SQL
Transformers
LLM
Standard NLP stack
Standard ML stack
Git
Vector databases(Postgres+pgvector
Разработка технических заданий
Нейронные сети
Цифровая трансформация
AI
Внутренние коммуникации
Групповое обучение
API
google cloud AI
SQL/NoSQL
BI-инструменты
"""

# Очистка и разделение данных
items = [item.strip() for item in data.replace('\n', ';').split(';') if item.strip()]
items = [item for item in items if item]  # Удаление пустых элементов

# Категоризация
categories = {
    'Языки программирования': ['Python', 'С#', 'С++', 'Bash', 'SQL'],
    'Фреймворки и библиотеки ML/DL': ['Keras', 'TensorFlow', 'PyTorch', 'OpenCV', 'Numpy',
                                      'NLTK/SpaCy', 'Librosa/PyDub', 'Transformers', 'Langchain',
                                      'MLflow', 'FastAPI', 'Django Framework'],
    'Инструменты и платформы': ['Docker', 'Git', 'GitHub', 'GitLab', 'Jira', 'BitBucket',
                                'MySQL', 'PostgreSQL', 'Greenplum', 'Vector databases(Postgres+pgvector',
                                'google cloud AI', 'BI-инструменты', 'MLflow', 'Cфера'],
    'Методы и алгоритмы ML': ['деревья решений', 'бустинги', 'лог.регрессия', 'методы кластеризации',
                              'ALS/SVD', 'методы NLP', 'нейросети', 'Deep Learning', 'Нейронные сети',
                              'Mathematical Programming', 'LoRA', 'Standard NLP stack', 'Standard ML stack',
                              'Computer Vision', 'RAG', 'LLM'],
    'Системы и ОС': ['Linux', 'ROS2', 'Robot Operating System', 'Docker'],
    'Предметные области': ['CV-моделями', 'текстовой аналитики', 'создание эмбеддингов',
                           'анализа транзакционных данных', '3D', 'калибровка сенсоров',
                           'ADAS', 'Беспилотный транспорт', 'Техническое зрение', 'AI',
                           'Цифровая трансформация'],
    'Процессы и методологии': ['Agile/Scrum', 'Работа в команде', 'Исследовательский анализ данных',
                               'Бизнес-анализ', 'Разработка технических заданий',
                               'Внутренние коммуникации', 'Групповое обучение'],
    'Навыки': ['IT-кругозор', 'ООП', 'API', 'SQL/NoSQL']
}

# Подсчет
counted_items = Counter(items)

# Создание DataFrame
df = pd.DataFrame.from_dict(counted_items, orient='index', columns=['Количество'])
df.index.name = 'Технология/Навык'

# Определение категорий для каждого элемента
def find_category(item):
    for category, items_in_category in categories.items():
        if item in items_in_category:
            return category
    return 'Другое'

df['Категория'] = df.index.map(find_category)

# Сортировка
df = df.sort_values(by=['Категория', 'Количество'], ascending=[True, False])

print("Подсчет технологий и навыков:")
print("=" * 50)
print(f"Всего уникальных элементов: {len(df)}")
print(f"Общее количество упоминаний: {df['Количество'].sum()}")
print("\n" + "=" * 50)

# Вывод по категориям
for category in sorted(df['Категория'].unique()):
    category_df = df[df['Категория'] == category]
    print(f"\n{category} ({len(category_df)} элементов):")
    print("-" * 40)
    for tech, count in category_df['Количество'].items():
        print(f"  {tech}: {count}")

# Топ-10 самых частых технологий
print("\n" + "=" * 50)
print("Топ-10 самых частых технологий:")
print("-" * 30)
for tech, count in df.nlargest(10, 'Количество').iterrows():
    print(f"{tech}: {count['Количество']} ({count['Категория']})")