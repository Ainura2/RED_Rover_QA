from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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
