import json
import requests
import allure
from constants import API1_url, API2_url, bearer_token


@allure.description("Тестирование добавления товара в корзину с некорректными параметрами.")
class WrongRequestAPI:
    """
    Класс для тестирования некорректных запросов к API добавления товара
    в корзину на сайте Читай-город.
    """

    url = API1_url
    url_2 = API2_url

    def __init__(self, url: str):
        """
        Инициализация класса WrongRequestAPI.

        :param url: URL API для выполнения запросов.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': bearer_token,
            'User-Agent': 'Google Chrome/142.0 (Windows NT 10.0; Win64; x64)'
        }

    def wrong_add_product(self, product_id: int, item_list_name: str) -> int:
        """
        Отправляет некорректный запрос для добавления товара в корзину
        с указанным product_id и именем списка товаров.

        :param product_id: Идентификатор товара, который нужно добавить в корзину.
        :param item_list_name: Название списка товаров.
        :return: Статус-код ответа от API.
        """
        payload = {
            "id": product_id,
            "adData": {
                "item_list_name": item_list_name,
            },
        }

        response = requests.patch(
            self.url,
            headers=self.headers,
            data=json.dumps(payload),
        )
        return response.status_code
