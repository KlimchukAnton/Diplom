import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.description("Тестирование добавления товара в корзину на сайте Читай-город.")
class AddToCart:
    """Класс для добавления книги в корзину."""

    def __init__(self, book_title: str):
        """
        Создает объект для добавления книги в корзину.

        :param book_title: Название книги для добавления в корзину.
        """
        self.book_title = book_title

    def search_by_title(self, driver: webdriver.Chrome, book_title: str) -> None:
        """
        Ищет книгу по названию и добавляет её в корзину.

        :param driver: Экземпляр драйвера Selenium.
        :param book_title: Название книги для поиска.
        :return: None.
        """
        # Ввод названия книги в строку поиска
        search_input = driver.find_element(By.NAME, "search")
        search_input.send_keys(book_title)

        # Клик по кнопке поиска
        search_button = driver.find_element(By.CSS_SELECTOR, 
                                            "button[aria-label='Найти']")
        search_button.click()

        # Клик по кнопке "Купить"
        buy_button = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, 
                                         "button[aria-label='false']")))
        buy_button.click()

        # Открытие корзины
        cart_icon = driver.find_element(By.CSS_SELECTOR, 
                                        "button[aria-label='Корзина']")
        cart_icon.click()
 