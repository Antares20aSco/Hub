from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, invalid_key
import os

pf = PetFriends()


def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа с недействительными email и паролем возвращает статус 403"""
    status, result = pf.get_api_key(email, password)
    assert status == 404


def test_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем что запрос всех питомцев с недействительным api ключом возвращает статус 403"""

    auth_key = invalid_key
    status = pf.get_list_of_pets(auth_key, filter)

    assert status == 403


def test_add_new_pet_with_invalid_data(name='Ленерис', animal_type='лис', age='', pet_photo=''):
    """Проверяем, позволяет ли система добавить питомца с невалидными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца с пустыми полями данных
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_new_pet_with_invalid_key(name='Альтаир', animal_type='кот', age='1', pet_photo='images/batcat.jpg'):
    """Проверяем, позволяет ли система добавить питомца с корректными
    данными но недействительным api ключом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Сохраняем в переменую auth_key неверный ключ api
    auth_key = invalid_key

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403


def test_add_new_pet_without_photo_with_valid_data(name='Санни', animal_type='лиса', age='3'):
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца без фото
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_add_self_pet_photo(pet_photo='images/fox.jpg'):
    """Проверяем возможность добавления фото к информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем добавить фото к информации о питомце
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, pet_photo)

        # Проверяем что статус ответа = 200 и фото питомца соответствует заданому
        assert status == 200
        assert result['pet_photo'] == pet_photo
    else:
        # если спиcок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_delete_not_self_pet():
    """Проверяем возможность удаления чужого питомца"""

    # Получаем ключ auth_key и запрашиваем список всех питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, " ")

    # Проверяем - если список питомцев пустой, то выкидываем исключение с текстом об отсутствии питомцев

    if len(pets['pets']) == 0:
        raise Exception("There is no pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список питомцев
    _, pets = pf.get_list_of_pets(auth_key, " ")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in pets.values()


def test_delete_self_pet_with_invalid_key():
    """Проверяем возможность удаления питомца с недействительным api ключом"""

    # Сохраняем в переменую auth_key неверный ключ api и запрашиваем список своих питомцев
    auth_key = invalid_key
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Запрашиваем выполнение удаления питомца
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "1", "images/batcat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 403
    assert status == 403


def test_add_new_pet_without_photo_with_invalid_data(name='Санни', animal_type='', age=''):
    """Проверяем можно ли добавить питомца без фото с частично пустыми полями данных"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца без фото с пустыми полями данных
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_new_pet_without_photo_with_invalid_key(name='Санни', animal_type='лиса', age='3'):
    """Проверяем что можно добавить питомца без фото с неверным ключом api"""

    # Сохраняем в переменую auth_key неверный ключ api
    auth_key = invalid_key

    # Добавляем питомца без фото
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403
