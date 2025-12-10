#Корень диска
import os
import sys

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
python_basic_dev = os.path.join(script_dir)

root_dir = os.path.splitdrive(script_dir)[0]

print(f"Текущая директория скрипта: {script_dir}")
print(f"Корень директории скрипта: {root_dir}")