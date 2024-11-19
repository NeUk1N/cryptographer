from cryptography.fernet import Fernet
from generateKey import generateKey
import os


def encrypt(file_path: str, password: str) -> str:
    
    if not password:
        raise ValueError('Введён пустой пароль. Попробуйте ещё раз')  
    
    if not os.path.exists(file_path):
        raise ValueError("Файл не существует. Попробуйте ещё раз.")
    
    # Генерируем ключ
    key = generateKey(password)
    # С помощью ключа создаём шаблон шифрования
    fernet = Fernet(key)

    # Читаем содержимое файла
    with open(file_path, 'rb') as file:
        file_data = file.read()
  

    # Шифруем данные
    try:
        encrypted_data = fernet.encrypt(file_data)
    except Exception as e:
        print('Ошибка при шифровании')

    # Записываем зашифрованные данные в новый файл
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    # Удаляем оригинальный файл
    os.remove(file_path)

    # Выводим успех
    print(f"Файл успешно зашифрован в '{file_path}.encrypted'.")