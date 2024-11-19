import hashlib
import base64

#Ф-ция создания ключа на основе пароля
def generateKey(password: str) -> bytes:
    # Генерируем ключ на основе пароля
    password_bytes = password.encode()
    key = hashlib.sha256(password_bytes).digest()  # Хешируем пароль
    return base64.urlsafe_b64encode(key)  # Кодируем в base64