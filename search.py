from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

path = r'C:\Users\a.ciccarello\Documents\Prove\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=path)

driver.get("https://www.escapefromtarkov.com/preorder-page")
price_official = driver.find_element_by_xpath("//*[@id='preorder_standard']/div[1]/div[3]/div[1]/div[1]/span[@itemprop='price']").text
driver.get("https://www.instant-gaming.com/it/2360-comprare-gioco-otherplatform-escape-from-tarkov-beta/")
price_ig = driver.find_element_by_xpath("//*[@id='ig-product-main-panel']/div[2]/div[2]/div[2]/div/div[3]").text
driver.quit()


def prices():
    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.get("https://www.escapefromtarkov.com/preorder-page")
    price_official = driver.find_element_by_xpath("//*[@id='preorder_standard']/div[1]/div[3]/div[1]/div[1]/span[@itemprop='price']").text
    driver.get("https://www.instant-gaming.com/it/2360-comprare-gioco-otherplatform-escape-from-tarkov-beta/")
    price_ig = driver.find_element_by_xpath("//*[@id='ig-product-main-panel']/div[2]/div[2]/div[2]/div/div[3]").text
    driver.quit()
    return ("price offical site " + price_official + " \nprice instant gaming "+ price_ig)

def check_ig():
    driver = webdriver.Chrome(options=options, executable_path=path)
    global price_ig
    driver.get("https://www.instant-gaming.com/it/2360-comprare-gioco-otherplatform-escape-from-tarkov-beta/")
    price_ig1 = driver.find_element_by_xpath("//*[@id='ig-product-main-panel']/div[2]/div[2]/div[2]/div/div[3]").text
    driver.quit()
    if price_ig1 != price_ig:
        stringa = "Prezzo sito Instant Gaming cambiato! Nuovo prezzo: "+price_ig1 +" vecchio prezzo: "+ price_ig
        price_ig = price_ig1
        return(stringa)
    else:
        return("")

def check_of():
    driver = webdriver.Chrome(options=options, executable_path=path)
    global price_official
    driver.get("https://www.escapefromtarkov.com/preorder-page")
    price_official1 = driver.find_element_by_xpath("//*[@id='preorder_standard']/div[1]/div[3]/div[1]/div[1]/span[@itemprop='price']").text
    driver.quit()
    if price_official1 != price_official:
        stringa = "Prezzo sito ufficiale cambiato! Nuovo prezzo: "+price_official1 +" vecchio prezzo: "+ price_official
        price_official = price_official1
        return(stringa)
    else:
        return("")


def period():
    global price_ig
    global price_official
    return ("price offical site " + price_official + " \nprice instant gaming "+ price_ig)
