#Сисадмин
import os
path_way = os.path.abspath('admin.bat')
real_way = os.path.realpath('admin.bat')
start = r"C:\Users\user0907\AppData\Local"
rel_way = os.path.relpath('admin.bat', start)

print(f"\nотносительный путь путь к файлу: {rel_way}")
print(f"\nабсолютный путь к файлу: {path_way}")
print(f"\nканонический путь путь к файлу: {real_way}")

