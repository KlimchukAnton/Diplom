import json
import requests
import allure
from constants import API1_url, API2_url, bearer_token


@allure.title("Класс для удаления товара из корзины")
class DeleteFromCart:
    """Класс для работы с API удаления товаров из корзины."""

    url = API1_url  # URL для удаления товаров
    url_2 = API2_url  # URL для получения содержимого корзины

    @allure.step("Инициализация класса DeleteFromCart")
    def __init__(self, url: str):
        """
        Создает объект для работы с корзиной.

        :param url: URL для удаления товара из корзины.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',  # Указываем, что отправляем JSON
            'Authorization': bearer_token,       # Токен для авторизации
            'User-Agent': 'Google Chrome/142.0 (Windows NT 10.0; Win64; x64)'
        }

    @allure.step("Получение содержимого корзины")
    def get_cart_contents(self) -> tuple[int, dict]:
        """
        Получает содержимое корзины.

        :return: Кортеж (статус-код, содержимое корзины в формате JSON).
        """
        response = requests.get(self.url_2, headers=self.headers)
        return response.status_code, response.json()

    @allure.step("Удаление товара из корзины")
    def delete_product_from_cart(self, prod_id: dict) -> int:
        """
        Удаляет товар из корзины.

        :param prod_id: Словарь с ID товара, который нужно удалить.
        :return: Статус-код ответа от сервера.
        """
        response = requests.delete(
            self.url_2,
            headers=self.headers,
            data=json.dumps(prod_id),
        )
        return response.status_code
