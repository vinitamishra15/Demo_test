import time
import pytest
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from GITDemo.Util.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class TestDemoApp(BaseClass):

    def testApp(self):
        self.driver.find_element(By.XPATH,"//input[@name='user_name']").send_keys("admin")
        self.driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("tt!rSy25Y^SK")
        self.driver.find_element(By.XPATH, "//button[@name='not_important']").click()
        time.sleep(3)
        self.driver.get("https://dev212832.service-now.com/com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=f7d636d447601210acd2a22f316d43c9")
        self.driver.find_element(By.XPATH,"//span[@class='input-group-btn']/a[@id='lookup.IO:632a361c47601210acd2a22f316d434a']").click()
        handle1 = self.driver.window_handles
        self.driver.switch_to.window(handle1[1])
        self.driver.find_element(By.XPATH,"//a[text()='HR']").click()
        self.driver.switch_to.window(handle1[0])
        self.driver.find_element(By.XPATH,"//span/a[@id='lookup.IO:a10e729047a01210acd2a22f316d4371']").click()
        handle2 = self.driver.window_handles
        self.driver.switch_to.window(handle2[1])
        self.driver.find_element(By.XPATH,"//td[@name='name']/div/div/div/input").send_keys("Roger Seid")
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        self.driver.find_element(By.XPATH,"//a[text()='Roger Seid']").click()
        self.driver.switch_to.window(handle2[0])
        self.driver.find_element(By.XPATH,"//div/textarea[@name='IO:4ede721447a01210acd2a22f316d43d5']").send_keys("TestApp Automation")
        self.driver.find_element(By.XPATH,"//button[@name='submit_button']").click()
        time.sleep(5)