import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_google_page(self):
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()

    def screenshot(self, archivo):
        self.driver.save_screenshot(archivo)
