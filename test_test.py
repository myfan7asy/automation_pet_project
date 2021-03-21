from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
page_url = "http://selenium1py.pythonanywhere.com/en-gb/basket/"


def test_open_p(url, path=""):
    driver.get(url + path)


test_open_p("http://selenium1py.pythonanywhere.com/en-gb/basket/")
