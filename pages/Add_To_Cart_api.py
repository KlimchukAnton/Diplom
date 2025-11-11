import json
import requests
import allure
from constants import API1_url, bearer_token


@allure.description("Тестирование добавления товара в корзину на сайте Читай-город.")
class AddToCartAPI:
    """Класс для работы с API добавления товара в корзину."""

    url = API1_url  # URL для добавления товара в корзину

    def __init__(self, url: str):
        """
        Создает новый объект для работы с API.

        :param url: URL для добавления товара в корзину.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',  # Установка типа контента
            'Authorization': bearer_token,       # Установка токена для авторизации
            'User-Agent': 'Google Chrome/142.0 (Windows NT 10.0; Win64; x64)'
        }

    def add_product_to_cart(self, product_id: int, item_list_name: str) -> int:
        """
        Добавляет товар в корзину и возвращает статус-код ответа.

        :param product_id: ID товара для добавления.
        :param item_list_name: Имя списка, к которому принадлежит товар.
        :return: Статус-код ответа от сервера (например, 200 для успешного добавления).
        """
        payload = {
            "id": product_id,
            "adData": {
                "item_list_name": item_list_name,
            },
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            data=json.dumps(payload),
        )
        return response.status_code