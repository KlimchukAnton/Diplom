import requests
import allure
from constants import API1_url, bearer_token


@allure.description("Тестирование отправки пустого запроса к API.")
class EmptyPostRequest:
    """
    Класс для работы с API интернет-магазина.
    Этот класс предназначен для отправки запросов к API, связанных с добавлением
    продуктов в корзину.
    """

    url = API1_url

    def __init__(self, url: str):
        """
        Создает объект для работы с корзиной.

        :param url: URL для добавления товара в корзину.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',  # Указываем, что отправляем JSON
            'Authorization': bearer_token,       # Токен для авторизации
            'User-Agent': 'Google Chrome/142.0 (Windows NT 10.0; Win64; x64)'
        }

    def add_product_to_cart_with_empty_body(self) -> int:
        """
        Отправляет POST-запрос с пустым телом для добавления продукта в корзину.

        :return: Статус-код ответа от сервера (int).
                 Ожидается, что в случае пустого тела запроса сервер вернет код 422.
        """
        response = requests.post(self.url, json={}, headers=self.headers)
        return response.status_code