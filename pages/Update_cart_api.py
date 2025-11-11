import json
import requests
import allure
from constants import API1_url, API2_url, bearer_token


@allure.description("Тестирование обновления корзины на сайте Читай-город.")
class UpdateCartAPI:
    """
    Класс для работы с API обновления корзины на сайте Читай-город.

    Атрибуты:
        url (str): URL для работы с корзиной.
        headers (dict): Заголовки запроса, включая авторизацию.
    """

    url = API1_url   # URL для получения информации о корзине
    url_2 = API2_url  # URL для обновления корзины

    def __init__(self, url: str):
        """
        Инициализация класса UpdateCartAPI.

        :param url: URL, используемый для работы с корзиной.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',  # Тип содержимого — JSON
            'Authorization': bearer_token,       # Авторизационный токен
            'User-Agent': 'Google Chrome/142.0 (Windows NT 10.0; Win64; x64)'
        }

    @allure.step("Обновление содержимого корзины")
    def update_cart(self, items: dict) -> tuple[int, str]:
        """
        Отправляет PUT-запрос для редактирования корзины.

        :param items: Словарь с товарами и их количеством для обновления корзины.
                      Пример формата:
                      {
                          "items": [
                              {"id": 1, "quantity": 2},
                              {"id": 2, "quantity": 1}
                          ]
                      }
        :return: Кортеж (статус-код, текст ответа от сервера).
        """
        response = requests.put(
            self.url_2,
            headers=self.headers,
            data=json.dumps(items),
        )
        return response.status_code, response.text