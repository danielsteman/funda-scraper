import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

url = 'https://www.funda.nl/huur/amsterdam/0-1500/3+kamers/'
page = requests.get(url, timeout=(3.05, 27))
soup = BeautifulSoup(page.content, 'html.parser')

# chrome_options = Options()  
# chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(
    ChromeDriverManager().install(), 
    # options=chrome_options
)
driver.get(url)

# solve with explicit wait
time.sleep(2)

cookie_button_id = 'onetrust-accept-btn-handler'
cookie_button = driver.find_element_by_id(cookie_button_id)
cookie_button.click()

time.sleep(2)

print (driver.page_source)

# checkbox_class = 'recaptcha-checkbox-checkmark'
# checkbox = driver.find_element_by_class_name(checkbox_class)
# checkbox.click()

# result = driver.find_element_by_class_name

# driver.close()