from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
import time

class WikipediaPage(BasePage):
    BOTON_INGLES = (By.ID, "js-link-box-en")  
    SEARCH_BOX = (By.ID, "searchInput")
    DROPDOWN_IDIOMAS = (By.ID, "p-lang-btn")
    SEARCH_BOX_IDIOMAS = (By.XPATH, "//input[@placeholder='Buscar un idioma']")
    DROPDOWN_PRODUCTOS = (By.XPATH, "//button[@aria-controls='toc-Productos-sublist']//span[@class='vector-icon mw-ui-icon-wikimedia-expand']")
    BOTON_IPHONE_DROPDOWN = (By.XPATH, "//*[@id='toc-iPhone']")
    TITULO_IPHONE = (By.ID, "iPhone")
    SECCION_BALON_ORO = (By.ID, "Balón_de_Oro")
    MESSI_ENLACE = (By.XPATH, "//table[contains(@style, 'background: #f5faff')]/tbody/tr[td[b/a[text()='Balón de Oro']]]/td[b/a[text()='Lionel Messi']]//a")
    RADIO_BUTTON_MODO_OSCURO = (By. XPATH, "//label[@for='skin-client-pref-skin-theme-value-night']")
    BODY_ELEMENT = (By.TAG_NAME, "body")
    
    def navegar_wikipedia(self):
        self.navigate_to(
            "https://www.wikipedia.org/"
        )
    
    def click_boton_ingles(self):
        self.click(self.BOTON_INGLES)
    
    def buscar_y_enviar(self, text):
        search_box = self.type_text(self.SEARCH_BOX, text)
        search_box.send_keys(Keys.RETURN)
    
    def click_dropdown_idiomas(self):
        self.click(self.DROPDOWN_IDIOMAS)
    
    def escribir_idioma(self, text):
        idiomas_box = self.type_text(self.SEARCH_BOX_IDIOMAS, text)
        time.sleep(1)
        idiomas_box.send_keys(Keys.RETURN)
    
    def click_dropdown_productos(self):
        self.click(self.DROPDOWN_PRODUCTOS)
    
    def click_iphone_dropdown(self):
        self.click(self.BOTON_IPHONE_DROPDOWN)
    
    def scroll_seccion_balon_oro(self):
        self.scroll_down(self.SECCION_BALON_ORO)
    
    def mover_hacia_enlace(self):
        self.hover_element(self.MESSI_ENLACE)
        self.click(self.MESSI_ENLACE)
    
    def seleccionar_modo_oscuro(self):
        self.click(self.RADIO_BUTTON_MODO_OSCURO)