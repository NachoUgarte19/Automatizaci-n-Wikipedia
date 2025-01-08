import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.wikipedia.org/")
    yield driver
    driver.quit() 

def test_validar_boton_english(browser):
    boton_english = browser.find_element(By.ID, "js-link-box-en")
    time.sleep(3)
    # Extraer el elemento por herencia
    texto_real = boton_english.find_element(By.TAG_NAME, "strong").text
    texto_esperado = "English"
    assert texto_esperado in texto_real, f"El texto encontrado fue: {texto_real}"
    time.sleep(3)

