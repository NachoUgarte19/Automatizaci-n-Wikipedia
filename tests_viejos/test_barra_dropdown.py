import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://es.wikipedia.org/wiki/Apple#")
    yield driver
    driver.quit() 

def test_barra_dropdown(browser):
    wait = WebDriverWait(browser, 10)
    dropdown_productos = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-controls='toc-Productos-sublist']//span[@class='vector-icon mw-ui-icon-wikimedia-expand']")))
    dropdown_productos.click()
    
    boton_seleccionado = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='toc-iPhone']")))
    boton_seleccionado.click()
    
    titulo_producto = wait.until(EC.presence_of_element_located((By.ID, "iPhone")))
    titulo_real = titulo_producto.text
    titulo_esperado = "iPhone"
    
    assert titulo_real == titulo_esperado, f"Se esperaba '{titulo_esperado}', pero se encontró '{titulo_real}'"
    
    url_actual = browser.current_url
    assert "#iPhone" in url_actual, f"La URL no contiene '#iPhone'. URL actual: {url_actual}"