from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.google_page import SearchGoogle
from pages.wiki_page import WikiSearch
# from base.base_driver import BaseDriver


@given('Estoy en la home page de google')
def step_01_precondición(context):
    service = Service(executable_path=r"C:\python\TestFrameworkDemo\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    context.driver = driver
    context.wait = wait
    sg = SearchGoogle(context.driver, context.wait)
    sg.open_google_page()


@when('Busco la palabra "automatizacion"')
def step_02_googlesearch(context):
    sg = SearchGoogle(context.driver, context.wait)
    sg.google_word()


@then('Debería poder ver los resultados de la búsqueda')
def step_03_googleresults(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "search")))


@when('Clickeo en el link de wikipedia/automatización')
def step_04_wikiclick(context):
    sg = SearchGoogle(context.driver, context.wait)
    sg.wiki_search()


@then('Debería poder ver la página de wikipedia')
def step_05_wikidisplays(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Automatización']")))


@when('Hago un scroll hacía abajo')
def step_06_scroll(context):
    sw = WikiSearch(context.driver, context.wait)
    sw.page_scrollTo()


@then('Hago un screenshot sobre la fecha requerída')
def step_07_screenshot(context):
    sw = WikiSearch(context.driver, context.wait)
    sw.screenshot("Automatización_primer_registro.png")
