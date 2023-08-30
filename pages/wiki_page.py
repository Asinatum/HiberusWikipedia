from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
import time


class WikiSearch(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def page_scrollTo(self):
        scroll_amount = 3000
        self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(4)
