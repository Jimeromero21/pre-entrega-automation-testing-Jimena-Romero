from utils.helpers import login_helper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_01_login(driver):
    login_helper(driver)

    assert "/inventory.html" in driver.current_url,"ERROR: No redirigio al inventatio"

def test_02_validar_titulo_ventana(driver):
    login_helper(driver)
    page_title = driver.title
    assert page_title == "Swag Labs" , f"ERROR: Titulo de ventana esperado: Swag Labs, obtenido {page_title}"


def test_03_validar_titulo_pagina(driver):
    login_helper(driver)
    section_title = driver.find_element (By.CLASS_NAME,"title").text

    assert section_title == "Products", f"ERROR: Titulo de la pagina esperado: 'Products', obtenido {section_title}"

def test_04_productos_visibles (driver):
    login_helper (driver)
    inventory_list = driver.find_elements (By.CLASS_NAME, "inventory_list")

    assert len (inventory_list) > 0, f"ERROR: No se encontraron productos visibles"


def test_05_validar_un_producto(driver):
    login_helper (driver)
    inventory_item_name  = driver.find_element (By.CLASS_NAME, "inventory_item_name").text

    assert inventory_item_name == "Sauce Labs Backpack", f"ERROR: Nombre del producto esperado 'Sauce Labs Backpack', obtenido {inventory_item_name}"

def test_06_validar_interfaz (driver):
    login_helper (driver)
    menu_button = driver.find_element (By.ID, "react-burger-menu-btn")
    filtro = driver.find_element (By.CLASS_NAME, "product_sort_container")

    assert menu_button.is_displayed(), f"ERROR: Menu no esta visible"
    assert filtro.is_displayed(), f"ERROR: Filtro no esta visible"

def test_07_crear_item(driver):
    login_helper(driver)

    wait = WebDriverWait(driver, 10)

    primer_item = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    boton_agregar = primer_item.find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    wait.until(
        lambda driver: primer_item.find_element(
            By.TAG_NAME, "button"
        ).text.capitalize() == "Remove"
    )

    boton_remove = primer_item.find_element(By.TAG_NAME, "button")

    assert boton_remove.text.capitalize() == "Remove", \
        "ERROR: El boton no cambio a Remove"

def test_08_verificar_contador_carrito (driver):
    login_helper(driver)
    primer_item = driver.find_elements (By.CLASS_NAME, "inventory_item")[0]
    boton_agregar = primer_item.find_element (By.TAG_NAME, "Button")
    boton_agregar.click ()
    contador_carrito = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text

    assert contador_carrito == "1" ,f'ERROR: Se esperaba 1 , obtuvo {contador_carrito}'


def test_09_navegar_carrito (driver):
    login_helper(driver)
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    assert "/cart.html" in driver.current_url , "ERROR: No se redirigió a /cart.html"

def test_10_comprobar_producto_en_el_carrito (driver):
    login_helper(driver)
    primer_item = driver.find_elements (By.CLASS_NAME, "inventory_item")[0]
    boton_agregar = primer_item.find_element (By.TAG_NAME, "Button")
    boton_agregar.click ()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    producto_carrito= driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert producto_carrito == "Sauce Labs Backpack", f"ERROR: No se encontro producto con el nombre 'Sauce Labs Backpack', obtenido {producto_carrito}"



