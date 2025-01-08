import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params=["Italiano", "Inglés", "Francés"])
def idioma_a_buscar(request):
    return request.param

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://es.wikipedia.org/wiki/Mil%C3%A1n")
    yield driver
    driver.quit() 

def test_cambiar_idioma(browser, idioma_a_buscar):
    boton_idiomas = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "p-lang-btn"))
    )
    boton_idiomas.click()
 
    barra_busqueda = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Buscar un idioma']"))
    )
    barra_busqueda.clear()
    barra_busqueda.send_keys(idioma_a_buscar)
    
    # Usar el idioma específico en el atributo `lang`
    idioma_code = {"Italiano": "it", "Inglés": "en", "Francés": "fr"}
    boton_idioma = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[@lang='{idioma_code[idioma_a_buscar]}']"))
    )
    boton_idioma.click()
    
    # Validar el título tras el cambio de idioma
    titulo_cambiado = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='mw-page-title-main']"))
    ).text
    
    # Diccionario con los títulos esperados para cada idioma
    titulos_esperados = {
        "Italiano": "Milano",
        "Inglés": "Milan",
        "Francés": "Milan"
    }
    
    assert titulos_esperados[idioma_a_buscar] == titulo_cambiado, (
        f"El idioma no se cambió correctamente para '{idioma_a_buscar}'. "
        f"Título esperado: '{titulos_esperados[idioma_a_buscar]}', Título obtenido: '{titulo_cambiado}'"
    )
    print(f"El idioma se cambió correctamente a '{idioma_a_buscar}'.")

