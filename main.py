
import sys
from encrypt import encrypt
from decrypt import decrypt
import getpass





def main():

    choice = int(input("Выберите действие:\n 1. Зашифровать файл.\n 2. Расшифровать файл. \n 3. Выйти из системы.\n"))

    if choice == 1:

        file_path = input("Введите путь до файла: ")

        password = getpass.getpass("Введите пароль: ")

        encrypt(file_path, password)


    elif choice == 2:
        file_path = input("Введите путь до файла: ")

        password = getpass.getpass("Введите пароль: ")

        decrypt(file_path, password)

    elif choice == 3:
        sys.exit()

main()
