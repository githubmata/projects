# -*- coding: utf8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException, TimeoutException


pytest.app = "https://www.disney.com/" 
# pytest.data = { "firstName": "tester", "lastName": "testing", "email address":"test1@yahoo.com"

load_timeout = 60

def pytest_addoption(parser):
	parser.addoption("--browser", action="store", default="chrome", help="Browser for test")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def driver(request, browser):
	if "chrome" in browser.lower():
		caps = webdriver.DesiredCapabilities.CHROME.copy()
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--ignore-certificate-errors')
		caps['acceptInsecureCerts'] = True
		b = webdriver.Chrome(desired_capabilities = caps, options=chrome_options)
	request.addfinalizer(lambda *args: b.quit())
	return b

@pytest.fixture()
def selenium(request, driver):
	try:
		driver.set_page_load_timeout(load_timeout)
		driver.implicitly_wait(5)
		driver.get(pytest.app)
	except TimeoutException:
		print ("browser load timeout")
	return driver