import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")
    # driver = webdriver.Edge()
    # objects and variables
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("headless")
        #service_obj = Service("Drivers/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=chrome_options)
    elif browser == "IE":
        service_obj = Service("/Users/DeySubha/Downloads/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://dev212832.service-now.com/now/nav/ui/classic/params/target/sc_cat_item_list.do%3Fsysparm_view%3D%26sysparm_first_row%3D1%26sysparm_query%3Dtype!%253Dbundle%255Esys_class_name!%253Dsc_cat_item_guide%255Etype!%253Dpackage%255Esys_class_name!%253Dsc_cat_item_content%255Epublished_refISEMPTY%255Ename%253DService%2520Category%2520Request%2520HP%2520Demo%26sysparm_nostack%3Dtrue")


    request.cls.driver = driver
    yield
    driver.close()
