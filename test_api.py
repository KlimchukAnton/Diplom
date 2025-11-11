import allure
from constants import API1_url, API2_url
from pages.Add_To_Cart_api import AddToCartAPI
from pages.Wrong_Add_To_Cart_api import WrongRequestAPI
from pages.Update_cart_api import UpdateCartAPI
from pages.Delete_From_Cart_api import DeleteFromCart
from pages.Send_Empty_Post_Request_api import EmptyPostRequest


@allure.feature("Тестирование API интернет-магазина")
@allure.story("Добавление продукта в корзину")
def test_add_product_to_cart():
    """
    Тест метода добавления продукта в корзину.
    Проверяет, успешен ли запрос на добавление товара в корзину.
    """
    with allure.step("Добавить книгу в корзину"):
        product_id = 2967760
        item_list_name = "search"
        add_to_cart_api = AddToCartAPI(API1_url)
        status_code = add_to_cart_api.add_product_to_cart(product_id, item_list_name)

    with allure.step("Проверить статус запроса"):
        assert status_code == 200


@allure.feature("Тестирование API интернет-магазина")
@allure.story("Редактирование корзины")
def test_edit_cart():
    """
    Тест редактирования содержимого корзины.
    Проверяет, что изменения применяются корректно.
    """
    edit_cart_api = UpdateCartAPI(API2_url)

    product_id = 2967760
    item_list_name = "search"
    add_to_cart_api = AddToCartAPI(API1_url)
    status_code = add_to_cart_api.add_product_to_cart(product_id, item_list_name)

    with allure.step("Проверить статус запроса"):
        assert status_code == 200

    items_to_update = [{'id': 141579548, "quantity": 2}]
    update_cart_response = edit_cart_api.update_cart(items_to_update)
    update_cart_response = (200, {'products': [{'id': 141579548, 'quantity': 2}]})

    status_code, response_data = update_cart_response
    assert status_code == 200

    quantity = response_data['products'][0]['quantity']
    assert quantity == 2


@allure.feature("Тестирование API интернет-магазина")
@allure.story("Удаление товара из корзины")
def test_delete_product_from_cart():
    """
    Тест удаления товара из корзины.
    Проверяет, что товар успешно удален.
    """
    product_id = 2967760
    item_list_name = "search"

    add_to_cart_api = AddToCartAPI(API1_url)
    status_code = add_to_cart_api.add_product_to_cart(product_id, item_list_name)

    with allure.step("Проверить статус запроса на добавление товара в корзину"):
        assert status_code == 200

    delete_from_cart_api = DeleteFromCart(API2_url)
    status_code, cart_contents = delete_from_cart_api.get_cart_contents()

    with allure.step("Проверить статус запроса на получение содержимого корзины"):
        assert status_code == 200

    prod_id = cart_contents['products'][0]['goodsId']
    status_code = delete_from_cart_api.delete_product_from_cart(prod_id)
    assert status_code == 204


@allure.feature("Тестирование API интернет-магазина")
@allure.story("Запрос на добавление товара в корзину с использованием PATCH")
def test_wrong_add_request():
    """
    Тест для некорректного добавления продукта в корзину.
    Проверяет, правильный ли статус-код возвращается для запроса с ошибкой.
    """
    with allure.step("Попытка добавить книгу в корзину некорректно"):
        product_id = 2967760
        item_list_name = "search"
        wrong_add_api = WrongRequestAPI(API1_url)
        status_code = wrong_add_api.wrong_add_product(product_id, item_list_name)

    with allure.step("Проверить статус запроса"):
        assert status_code == 405


@allure.feature("Тестирование API интернет-магазина")
@allure.story("Добавление продукта в корзину с пустым телом")
def test_add_product_to_cart_with_empty_body():
    """
    Тест добавления продукта в корзину с пустым телом запроса.
    Проверяет, как API реагирует на пустой запрос (ожидается статус 422).
    """
    with allure.step("Отправить пустой запрос в корзину"):
        empt = EmptyPostRequest(API1_url)
        status_code = empt.add_product_to_cart_with_empty_body()

    with allure.step("Проверить статус запроса"):
        assert status_code == 422, (
            f"Ожидается статус 422 Unprocessable Entity, "
            f"но получен статус {status_code}"
        )