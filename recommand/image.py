import time
import urllib.parse

from webdriver_manager.chrome import ChromeDriverManager # 자동으로 크롬드라이버(가상브라우저) 파일을 다운로드해주는 라이브러리
from selenium.webdriver.chrome.service import Service # 다운로드된 크롬드라이버 파일을 연결하기 위해 활용
from selenium.webdriver.chrome.options import Options # Selenium header 변경

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import warnings

def scrape(query):
    warnings.filterwarnings("ignore") # 불필요한 Warning 메시지를 꺼줍니다.

    service = Service(executable_path=ChromeDriverManager().install())

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    driver.get(f"https://yandex.com/images/search?text={str(urllib.parse.quote_plus('wine ' + query))}&iorient=square")

    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'serp-item__link').click()

    result = str(driver.find_element(By.CLASS_NAME, 'MMImage-Origin').get_attribute('src'))

    driver.close()
    driver.quit()

    return result
