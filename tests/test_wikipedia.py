import pytest
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@allure.title("Cambiar el idioma a inglés de la página principal de Wikipedia")
@allure.epic("Validación de funcionalidades básicas de Wikipedia")
@allure.feature("Botón 'English'")
@allure.story("Al presionar el boton 'English' el idioma de la página cambia a inglés")
@allure.testcase("TC-001")
@pytest.mark.boton_ingles
def test_click_boton_ingles(wikipedia_page):
    with allure.step("Al navegar a Wikipedia y hacer click en el boton 'English'"):
        wikipedia_page.navegar_wikipedia()
        wikipedia_page.click_boton_ingles()
    
    with allure.step("Puedo verificar que el idioma de la página se cambio correctamente"):
        url_wikipedia_ingles = "https://en.wikipedia.org/wiki/Main_Page"
        assert wikipedia_page.driver.current_url == url_wikipedia_ingles, "La página no se cambió al inglés correctamente"


@allure.title("Buscar en la barra de búsqueda")
@allure.epic("Validación de funcionalidades básicas de Wikipedia")
@allure.feature("Barra búsqueda")
@allure.story("Al buscar en la barra de búsqueda, nos dirige hacia esa página")
@allure.testcase("TC-002")
@pytest.mark.busqueda
def test_buscar_cosas(wikipedia_page):
    with allure.step("Al navegar a Wikipedia y buscar 'Racing Club', valido que la búsqueda se haya realizado exitosamente"):
        wikipedia_page.navegar_wikipedia()
        wikipedia_page.buscar_y_enviar("Racing Club")
        assert "Racing Club" in wikipedia_page.driver.title, "La busqueda no se realizó correctamente"


@allure.title("Cambiar el idioma de una página")
@allure.epic("Validación de funcionalidades básicas de Wikipedia")
@allure.feature("Cambio idioma")
@allure.story("Al acceder a una página y cambiar el idioma de la misma, esta deberia cargarse nuevamente en el idioma seleccionado")
@allure.testcase("TC-003")
@pytest.mark.cambio_idioma  
def test_cambiar_idioma(wikipedia_page):
    with allure.step("Al navegar a Wikipedia y buscar 'Milán', valido que la búsqueda se haya realizado exitosamente"):
        wikipedia_page.navegar_wikipedia()
        wikipedia_page.buscar_y_enviar("Milán")
        assert "Milán" in wikipedia_page.driver.title, "La busqueda no se realizó correctamente"
    
    with allure.step("Selecciono el boton de 'idiomas'"):
        wikipedia_page.click_dropdown_idiomas()
    with allure.step("Escribo en la barra de busqueda 'Italiano' y presiono Enter"):
        wikipedia_page.escribir_idioma("Italiano")
    
    with allure.step("Puedo verificar que la página se cambio de idioma a italiano"):
        assert "it.wikipedia.org" in wikipedia_page.driver.current_url, "El cambio de idioma no se realizó correctamente"
        assert "Milano" in wikipedia_page.driver.title, "El cambio de idioma no se realizó correctamente"


@allure.title("Utilizar dropdown de contenidos")
@allure.epic("Validación de funcionalidades básicas de Wikipedia")
@allure.feature("Dropdown contenidos")
@allure.story("Al utilzar el dropdown lateral, validar que nos redireccione a la parte de la página que seleccionamos")
@allure.testcase("TC-004")
@pytest.mark.dropdown_lateral
def test_dropdown_contenidos(wikipedia_page):
    wikipedia_page.driver.maximize_window()
    
    with allure.step("Al navegar a Wikipedia y buscar 'Apple', valido que la búsqueda se haya realizado exitosamente"):
        wikipedia_page.navegar_wikipedia()
        wikipedia_page.buscar_y_enviar("Apple")
        assert "Apple" in wikipedia_page.driver.title, "La busqueda no se realizó correctamente"
    
    with allure.step("Hago click en el dropdown 'Productos'"):
        wikipedia_page.click_dropdown_productos()
    
    with allure.step("Hago click cobre 'iPhone'"):
        wikipedia_page.click_iphone_dropdown()
    
    with allure.step("Puedo verificar que me redireccionó a la seccion que yo seleccioné"):
        titulo_producto = wikipedia_page.wait_for_element(wikipedia_page.TITULO_IPHONE)
        titulo_real = titulo_producto.text
        titulo_esperado = "iPhone"
        
        assert titulo_real == titulo_esperado, f"Se esperaba '{titulo_esperado}', pero se encontró '{titulo_real}'"


@allure.title("Utilizar un enlace dentro de una página")
@allure.epic("Validación de funcionalidades básicas de Wikipedia")
@allure.feature("Enlace dentro de página")
@allure.story("Al utilizar el enlace, validar que nos redireccione a la página correspondiente")
@allure.testcase("TC-005")
@pytest.mark.enlace
def test_valdiar_enlace(wikipedia_page):
    with allure.step("Al navegar a Wikipedia y buscar 'Mundial 2022', valido que la búsqueda se haya realizado exitosamente"):
        wikipedia_page.navegar_wikipedia()
        wikipedia_page.buscar_y_enviar("Mundial 2022")
    
    with allure.step("Hago scroll hasta la seccion 'Balón de Oro'"):
        wikipedia_page.scroll_seccion_balon_oro()
    
    with allure.step("Muevo el puntero hacia el enlace y hago click"):
        wikipedia_page.mover_hacia_enlace()
    
    with allure.step("Puedo verificar que el enlace me redirecciona a la página correspondiente"):
        titulo_esperado = "Lionel Messi"
        assert titulo_esperado in wikipedia_page.driver.title, f"El titulo de la pagina es incorrecto: {wikipedia_page.driver.title}"


@allure.title("Cambiar a modo oscuro")
@allure.epic("Validación de funcionalidades básicas de Wikipedia")
@allure.feature("Botón modo oscuro")
@allure.story("Al utilizar el botón de 'modo oscuro' que se cargue la página con el nuevo estilo")
@allure.testcase("TC-006")
@pytest.mark.modo_oscuro 
def test_cambiar_modo_oscuro(wikipedia_page):
    wikipedia_page.driver.maximize_window()
    
    with allure.step("Al navegar a Wikipedia y buscar 'Pirámides de Egipto', valido que la búsqueda se haya realizado exitosamente"):
        wikipedia_page.navegar_wikipedia()
        wikipedia_page.buscar_y_enviar("Pirámides de Egipto")
    
    with allure.step("Selecciono el modo oscuro"):
        wikipedia_page.seleccionar_modo_oscuro()
    
    with allure.step("Puedo verificar que se cambio a modo oscuro correctamente"):
        body_element = wikipedia_page.wait_for_element(wikipedia_page.BODY_ELEMENT)
        background_color = body_element.value_of_css_property("background-color")
        
        assert background_color == "rgba(32, 33, 34, 1)", f"El color de fondo no cambió correctamente: {background_color}"