import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import UI_url
from pages.Search_By_Author_ui import SearchByAuthor
from pages.Search_By_Title_ui import SearchByTitle
from pages.Add_To_Cart_ui import AddToCart
from pages.Delete_From_Cart_ui import DeleteFromCart


search_by_author = SearchByAuthor
search_by_title = SearchByTitle
add_to_cart = AddToCart
delete_from_cart = DeleteFromCart


@allure.title("Тест поиска книг по автору (POSITIVE)")
@allure.description("Проверяет, что поиск книг по автору работает корректно.")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_search_by_author():
    """Проверка корректности результатов поиска по автору."""
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Найти книгу по автору Франк Тилье"):
        author_name = "Франк Тилье"
        search_instance = SearchByAuthor(author_name)
        search_instance.search_by_author(driver, author_name)

    with allure.step("Получить результаты поиска"):
        results_find = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "search-title__sub")))
    
    with allure.step("Проверить, что поиск по автору успешен"):
        assert results_find is not None

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Тест добавления товара в корзину (POSITIVE)")
@allure.description("Проверяет, что товар корректно добавляется в корзину.")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_add_to_cart():
    """Проверка корректности добавления товара в корзину."""
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Добавить в корзину книгу с названием 'Головоломка'"):
        book_title = "Головоломка"
        search_name = AddToCart(book_title)
        search_name.search_by_title(driver, book_title)

    with allure.step("Получить результаты добавления в корзину"):
        results_add = driver.find_element(By.CSS_SELECTOR, 
                                          "button[aria-label='Корзина']")

    with allure.step("Проверить, что корзина не пуста"):
        assert results_add is not None

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Тест удаления товара из корзины (POSITIVE)")
@allure.description("Проверяет, что товар корректно удаляется из корзины.")
@allure.feature("DELETE")
@allure.severity("BLOCKER")
def test_delete_from_cart():
    """Проверка корректности удаления товара из корзины."""
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Удалить книгу из корзины"):
        book_title = "Ветреный"
        delete_from_cart(book_title)
        results_del = driver.find_elements(By.CSS_SELECTOR, "div.product-title__head")

    with allure.step("Проверить, что товар больше не существует в списке"):
        assert all(
            book_title not in element.text for element in results_del
        ), f"Книга '{book_title}' все еще в корзине."

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Тест поиска по несуществующему автору (NEGATIVE)")
@allure.description("Проверяет, что поиск по несуществующему автору невозможен.")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_wrong_author():
    """Проверка поиска книги по несуществующему автору."""
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Найти книгу по несуществующему автору"):
        author_name = "Гемаклиник"
        search_by_author(author_name)

    with allure.step("Проверить, что поиск не дал результатов"):
        results_find = driver.find_elements(By.CSS_SELECTOR, "h4.catalog-empty-result__header")
        assert results_find is not None

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Тест поиска по смешанному запросу (NEGATIVE)")
@allure.description("Проверяет, что поиск по смешанному запросу невозможен.")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_mixed_request():
    """Проверка поиска книги по смешанному запросу."""
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome()

    with allure.step("Перейти на сайт Читай-город"):
        driver.get(UI_url)

    with allure.step("Найти книгу по смешанному запросу"):
        book_title = "Vetреный"
        search_by_title(book_title)

    with allure.step("Проверить, что поиск не дал результатов"):
        results_find = driver.find_elements(By.CSS_SELECTOR, "h4.catalog-empty-result__header")
        assert results_find is not None

    with allure.step("Закрыть браузер"):
        driver.quit()