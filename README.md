# Automatización QA - SauceDemo

## Descripción

Este proyecto corresponde a una práctica de automatización de pruebas funcionales utilizando **Python, Pytest y Selenium WebDriver**.

El objetivo es automatizar el proceso de inicio de sesión en la página **SauceDemo**, utilizando una estructura organizada mediante tests, funciones auxiliares y fixtures de Pytest.

## Tecnologías utilizadas

* Python 3.14.7
* Pytest 9.1.1
* Selenium WebDriver
* Webdriver Manager
* Google Chrome
* Git / GitHub

## Estructura del proyecto

```text
pre-entrega-automation-testing-Jimena-Romero/
│
├── tests/
│   ├── __init__.py
│   └── Test_saucedemo.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── conftest.py
│
└── README.md
```

### `tests/`

Contiene los casos de prueba automatizados.

El archivo `Test_saucedemo.py` contiene la prueba correspondiente al inicio de sesión.

### `utils/`

Contiene funciones auxiliares que pueden ser reutilizadas por diferentes pruebas.

El archivo `helpers.py` contiene la función:

```python
login_helper(driver)
```

Esta función se encarga de:

1. Acceder a SauceDemo.
2. Completar el usuario.
3. Completar la contraseña.
4. Presionar el botón de login.

### `conftest.py`

Contiene la fixture de Pytest encargada de crear y cerrar el navegador.

La fixture:

```python
@pytest.fixture
def driver():
```

crea una instancia de Chrome mediante Selenium y `ChromeDriverManager`.

Al finalizar la prueba, el navegador se cierra mediante:

```python
driver.quit()
```

## 🌐 Sitio utilizado

La automatización se realiza sobre:

**SauceDemo**

```text
https://www.saucedemo.com/
```

## Datos utilizados para el login

Para la prueba se utilizan las credenciales de usuario de prueba de SauceDemo:

```text
Usuario: standard_user
Contraseña: secret_sauce
```

##  Prueba automatizada

El test utiliza la fixture `driver` proporcionada por `conftest.py` y llama a la función auxiliar `login_helper()`.

Ejemplo:

```python
from utils.helpers import login_helper


def test_login(driver):
    login_helper(driver)
```

De esta manera, la lógica de navegación y login queda separada del caso de prueba.

##  Ejecución de las pruebas

Desde la carpeta raíz del proyecto:

```powershell
pytest
```

Para obtener información más detallada:

```powershell
pytest -v
```

El parámetro `-v` permite visualizar el nombre de cada prueba y su resultado.

## Resultado esperado

Al ejecutar:

```powershell
pytest -v
```

se espera obtener un resultado similar a:

```text
collected 1 item

tests/Test_saucedemo.py::test_login PASSED
```
##  Dependencias

Las principales dependencias utilizadas en el proyecto son:

```text
pytest
selenium
webdriver-manager
```

Pueden instalarse mediante:

```powershell
pip install pytest selenium webdriver-manager
```

## Objetivo de la práctica

El proyecto busca aplicar conceptos fundamentales de automatización QA:

* Creación de pruebas automatizadas.
* Uso de Selenium WebDriver.
* Uso de Pytest.
* Fixtures.
* Funciones reutilizables.
* Separación entre casos de prueba y funciones auxiliares.
* Organización de un proyecto de automatizacion.
