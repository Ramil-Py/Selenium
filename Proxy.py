from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

options = Options()
service = Service(executable_path=ChromeDriverManager().install())
# proxy = '151.106.39.34'
options.add_argument("--proxy-server=207.55.243.42")
driver = webdriver.Chrome(options=options, service=service)
driver.get("https://2ip.ru")
time.sleep(20)
