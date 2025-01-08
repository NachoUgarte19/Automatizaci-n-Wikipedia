import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params=["Racing Club"])
def termino_de_busqueda(request):
    return request.param

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.wikipedia.org/")
    yield driver
    driver.quit()

def test_buscar_cosas(browser, termino_de_busqueda):
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(termino_de_busqueda + Keys.RETURN)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "firstHeading"))
    )
    
    texto_titulo = browser.find_element(By.ID, "firstHeading").text
    assert texto_titulo == termino_de_busqueda, f"Se esperaba '{termino_de_busqueda}' pero se encontró '{texto_titulo}'"
