import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params=["Italiano"])
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
    boton_idiomas = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "p-lang-btn"))
    )
    boton_idiomas.click()
 
    barra_busqueda = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Buscar un idioma']"))
    )
    barra_busqueda.clear()
    barra_busqueda.send_keys(idioma_a_buscar)
    
    boton_italiano = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@lang='it']"))
    )
    boton_italiano.click()

    titulo_italiano = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='mw-page-title-main']"))
    ).text
    
    titulo_esperado = "Milano"
    assert titulo_esperado == titulo_italiano, (
    f"El idioma no se cambió correctamente. Título esperado: '{titulo_esperado}', "
    f"Título obtenido: '{titulo_italiano}'"
    )
    