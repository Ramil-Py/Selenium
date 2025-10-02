from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time, os

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://kabinet.unec.edu.az/az/eresults")
time.sleep(2)
locator_year = (By.XPATH, '//select[@name="eyear"]')
select_year = Select(driver.find_element(*locator_year))
select_year.select_by_value('1000044')

locator_term = (By.XPATH, '//select[@name="term"]')
select_term = Select(driver.find_element(*locator_year))
for option in select_term.options:
    print(option.get_attribute('value'), option.text)