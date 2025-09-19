#Содержимое
import os

def in_direct(project):
    print(f"\nСодержимое директории {project}")
    try:
        for i in os.listdir(project):
            path = os.path.join(project, i)
            print(f"   {path}")

    except FileNotFoundError:
        print(f"  Ошибка: директория не найдена")
base_dir = r"C:\Root\RemoteFolders\user0907"
python_basic = os.path.join(base_dir, 'companyfrontdesc1')#r"C:\Root\RemoteFolders\user0907\companyfrontdesc1"
print(f"Содержимое каталога {python_basic}")
dirname = in_direct(python_basic)

print(f"Текущая рабочая директория: {os.getcwd()}")
print(os.access(python_basic, os.R_OK))
print(f"Существует: {os.path.exists(python_basic)}")
print(f"Это директория: {os.path.isdir(python_basic)}")
print(f"Это файл: {os.path.isfile(python_basic)}")
print(f"Право на чтение (R_OK): {os.access(python_basic, os.R_OK)}")
print(f"Право на запись (W_OK): {os.access(python_basic, os.W_OK)}")
print(f"Право на выполнение (X_OK): {os.access(python_basic, os.X_OK)}")
false_way = os.path.abspath('companyfrontdesc1')
print('false_way', false_way)
