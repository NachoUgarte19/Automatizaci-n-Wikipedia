import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2022")
    yield driver
    driver.quit() 

def test_validar_enlace(browser):
    
    balon_oro_seccion = browser.find_element(By.ID, "Balón_de_Oro")
    actions = ActionChains(browser)
    actions.move_to_element(balon_oro_seccion).perform()
    
    messi_enlace = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
        By.XPATH, 
        "//table[contains(@style, 'background: #f5faff')]/tbody/tr[td[b/a[text()='Balón de Oro']]]/td[b/a[text()='Lionel Messi']]//a"
    )))
    actions.move_to_element(messi_enlace).perform()
    messi_enlace.click()

    WebDriverWait(browser, 5).until(EC.title_contains("Lionel Messi"))
    assert "Lionel Messi" in browser.title, f"El titulo de la pagina es incorrecto: {browser.title}"
    
    
    
    
    