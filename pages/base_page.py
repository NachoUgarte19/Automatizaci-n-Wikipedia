from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)
    
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_condition(self, condition, timeout=10):
        WebDriverWait(self.driver, timeout).until(condition)

    def click(self, locator):
        self.wait_for_element(locator).click()
    
    def type_text(self, locator, text):
        elemento = self.wait_for_element(locator)
        elemento.clear()
        elemento.send_keys(text)
        return elemento
    
    def select_from_dropdown_by_visible_text(self, locator, text):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)
    
    def selec_from_dropdown_by_index(self, locator, index):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)
        
    def select_element(self, locator):
        elemento = self.wait_for_element(locator)
        if not elemento.is_selected():
            elemento.click()
    
    def unselect_checkbox(self, locator):
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()
    
    def scroll_down(self, locator):
        elemento = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(elemento).perform() # Probar con scroll
    
    def hover_element(self, locator):
        elemento = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(elemento).perform()