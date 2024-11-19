import pytest
from encrypt import encrypt

def test_with_empy_password():
    password = ""
    file_path = "D:/Work/Python/cryptographer/123.txt"


    with open(file_path, 'w') as f:
        f.write("Test data")


    with pytest.raises(ValueError, match = 'Введён пустой пароль. Попробуйте ещё раз'):
        encrypt(file_path, password)
    

def test_file_not_exists():
    password = "1234"
    file_path = "D:\\Work\\Python\\cryptographer\\fail.txt" 


    with pytest.raises(ValueError, match = "Файл не существует. Попробуйте ещё раз."):
        encrypt(file_path, password)