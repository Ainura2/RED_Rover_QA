import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import Actions
import pytest


options = Options()
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def test_women():
    driver.get('https://magento.softwaretestingboard.com/')
    sale_button = driver.find_element(By.XPATH, "//*[@id='store.menu']//*[text()='Sale']/parent::a")
    sale_button.click()
    assert driver.title == "Sale"

    women_button = driver.find_element(By.XPATH, "//*[@id='maincontent']//*[text()='Shop Women’s Deals']")
    women_button.click()
    assert driver.title == "Women Sale"
    driver.get_screenshot_as_file("tr.png")
    driver.close()


def test_right():
    driver.get('https://magento.softwaretestingboard.com/')
    sale_button = driver.find_element(By.XPATH, "//*[@id='store.menu']//*[text()='Sale']/parent::a")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL)
    action.click(on_element=sale_button)

    action.perform()

    driver.switch_to.window(driver.window_handles[1])
    assert driver.title == "Sale"

    # driver.save_screenshot("tr2.png")
    driver.close()