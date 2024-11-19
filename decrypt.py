from cryptography.fernet import Fernet
from generateKey import generateKey
import os

#Ф-ция дешифрования
def decrypt(file_path: str, password: str) -> str:


    if not password:
        raise ValueError('Введён пустой пароль. Попробуйте ещё раз')


    if not os.path.exists(file_path):
        raise ValueError("Файл не существует. Попробуйте ещё раз.")


    # Генерируем ключ
    key = generateKey (password)
    # С помощью ключа создаём шаблон шифрования
    fernet = Fernet(key)

    # Читаем содержимое файла
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Дешифруем данные с откладкой на ошибку шифрования
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("Ошибка при дешифровании")
        return

    # Записываем расшифрованные данные в новый файл
    decrypted_file_path = file_path.replace('.encrypted', '')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    os.remove(file_path)
    print(f"Файл успешно расшифрован в '{decrypted_file_path}'.")