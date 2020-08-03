import pytest
import requests
import json
import page
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

@pytest.mark.ui
class TestCreateEntry(object):

	def test_ui_shop(self,selenium):
		driver = selenium
		driver.refresh()
		main_page = page.MainPage(driver)
		time.sleep(10)
		main_page.click_shop()
		time.sleep(3)
		main_page.click_shopmenu()
		time.sleep(3)
		main_page.click_signup()
		time.sleep(3)
		WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name='disneyid-iframe']")))
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-secondary.ng-isolate-scope"))).click()
		time.sleep(3)
		main_page.enter_fname()
		time.sleep(3)
		main_page.enter_lname()
		time.sleep(3)
		main_page.enter_email()
		time.sleep(3)
		main_page.enter_newPassword()
		time.sleep(3)
		main_page.enter_verifyPassword()
		time.sleep(3)
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='dateOfBirth']"))).send_keys("11291982")
		time.sleep(3)
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='did-ui-view']/div/section/section/form/section[7]/div/button"))).click()
		time.sleep(3)

#SAVE ACCOUNT AND SECTION INFO data:
# 4. Navigate down and capture the section info for the following sections on the page (used for verification later)

# 5. save the account info and section info into an Excel sheet and logout

# 6. re-open the shop page and call the login info from the Excel sheet and log in the page

# 7. Verify the sections information are displayed

		#Sign Out
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "xpath=//a[contains(.,'Sign Out')]"))).click()
		time.sleep(3)


# ATTEMPTED TO FILL OUT FORM INSIDE IFRAME COMPONENT FOR SIGN UP FORM:
		# add_page = page.AddPage(driver)
		# WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[ng-model='vm.model.firstName']")))
		# add_page.add_contact(pytest.data)
		# full_name = pytest.data["firstName"] + " " + pytest.data["lastName"]
		# assert pytest.data["firstName"] in driver.page_source, "Contact not ccreated"
		
