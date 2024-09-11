import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from GITDemo.Util.BaseClass import BaseClass
from selenium.webdriver.common.by import By

class TestNewCountry(BaseClass):

    def testCreateRecord(self):
        self.driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("admin")
        self.driver.find_element(By.XPATH, "//input[@name='user_password']").send_keys("tt!rSy25Y^SK")
        self.driver.find_element(By.XPATH, "//button[@name='not_important']").click()
        time.sleep(2)
        self.driver.get("https://dev212832.service-now.com/com.glideapp.servicecatalog_cat_item_view.do?v=1&sysparm_id=6a02369c47201210acd2a22f316d434d")
        self.driver.find_element(By.XPATH,"//div/input[@name='IO:129276dc47201210acd2a22f316d430b']").send_keys("India")
        self.driver.find_element(By.XPATH,"//div/textarea").send_keys("New Check Automation")
        self.driver.find_element(By.XPATH,"//button[@name='oi_order_now_button']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[text()='submit a request to create new counrty record.']").click()
        scrolldown = self.driver.find_element(By.XPATH,"//span[text()='Catalog Tasks']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scrolldown)
        self.driver.find_element(By.XPATH,"//span[@class='tabs2_tab']/span[@class='tab_caption_text']").click()
        self.driver.find_element(By.XPATH,"//td/a[@class='linked formlink']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span/button[@id='approve']").click()
        print(self.driver.find_element(By.XPATH,"//div[@class='outputmsg_text']").text)
        time.sleep(3)
        self.driver.refresh()
        scrolldown = self.driver.find_element(By.XPATH,"//span[contains(text(),'Catalog Tasks')]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scrolldown)
        time.sleep(3)