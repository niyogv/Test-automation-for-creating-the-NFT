import pyautogui
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Test_qamarket:

    @pytest.fixture()
    def test_invoke(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.wait=WebDriverWait(self.driver,10)
        self.driver.get('https://qamarket.moiverse.io/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        user=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[2]/div/div/input')
        user.send_keys('niyog28jan')
        password=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[3]/div/div/input')
        password.send_keys('Test@123')
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(10)
        yield
        self.driver.quit()

    def test_Minting_nft(self,test_invoke):
        self.driver.find_element_by_link_text('Create').click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@aria-label='Dropdown select']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@aria-label='Dropdown select']/div[3]/div[14]").click()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys('/Users/aicumen-dev/Downloads/images.jpeg')
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/input').send_keys('Selenium')
        self.driver.find_element_by_xpath("//select[@class='styles_categoryDropdown__3ZYjl']/option[2]").click()
        self.driver.find_element_by_xpath("//textarea[@placeholder='Description']").send_keys('jpeg format')
        self.driver.find_element_by_xpath("//input[@placeholder='Supply']").send_keys('10')
        self.driver.find_element_by_xpath("//input[@placeholder='Royalty']").send_keys('4')
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[4]/div[2]/div[2]').click()
        time.sleep(60)
        self.driver.find_element_by_xpath("//div[@class='styles_account__3MgT6 styles_menuLink__17kgw']").click()
        self.driver.find_element_by_xpath("//ul[@class='MuiList-root MuiMenu-list styles_menuList__33Jfh MuiList-padding']/div[1]").click()
        time.sleep(2)
        print(self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[1]').text)
        print(self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[3]').text)