import time
import urllib.parse

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from django.conf import settings

def scrape(query):

    driver = settings.SDRIVER

    print(query)

    # driver.get(f"https://yandex.com/images/search?text={str(urllib.parse.quote_plus('wine ' + query))}&iorient=square")
    # driver.get(f"https://www.google.co.kr/search?q={str(urllib.parse.quote_plus(query))}&tbm=isch&hl=ko&tbs=itp:clipart")
    # driver.get(f"https://www.bing.com/images/search?view=detailV2&expw=500&q={str(urllib.parse.quote_plus(query))}&selectedIndex=0")
    driver.get(f"https://www.bing.com/images/search?view=detailV2&expw=500&q={query}&selectedIndex=0")

    # time.sleep(2)

    # driver.find_elements(By.CLASS_NAME, 'serp-item__link')[0].click()
    # driver.find_elements(By.CLASS_NAME, 'islib')[0].click()

    time.sleep(1)

    # result = str(driver.find_element(By.CLASS_NAME, 'MMImage-Origin').get_attribute('src'))
    # result = str(driver.find_element(By.CSS_SELECTOR, 'c-wiz a[role=link] img').get_attribute('src'))
    result = str(driver.find_element(By.CSS_SELECTOR, '#mainImageViewer .imgContainer img').get_attribute('src'))

    # driver.close()
    # driver.quit()

    return result

    # driver.get(query)
    #
    # card = driver.find_element(By.CLASS_NAME, 'default-wine-card')
    #
    # ahref = card.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    #
    # isrc = str(card.find_element(By.CSS_SELECTOR, 'figure').get_attribute('style')).split('//', 1)[1]
    #
    # return 'https://www.vivino.com'+ahref, isrc
