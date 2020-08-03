from locators import MainPageLocators, AddPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
	def __init__(self, driver):
		self.driver = driver

class MainPage(BasePage):

	def click_shop(self):
		self.driver.find_element(*MainPageLocators.SHOP).click()		

	def click_shopmenu(self):
		self.driver.find_element(*MainPageLocators.SHOPMENU).click()

	def click_signup(self):
		self.driver.find_element(*MainPageLocators.SIGNUP).click()

	def enter_fname(self):
		self.driver.find_element(*MainPageLocators.FIRSTNAME).send_keys("tester")

	def enter_lname(self):
		self.driver.find_element(*MainPageLocators.LASTNAME).send_keys("testing")

	def enter_email(self):
		self.driver.find_element(*MainPageLocators.EMAIL).send_keys("amata@gmail.com")

	def enter_newPassword(self):
		self.driver.find_element(*MainPageLocators.NEWPASSWORD).send_keys("Apassword1")

	def enter_verifyPassword(self):
		self.driver.find_element(*MainPageLocators.VERIFYPASSWORD).send_keys("Apassword1")

#SAVE ACCOUNT AND SECTION INFO data:
# 4. Navigate down and capture the section info for the following sections on the page (used for verification later)

# 5. save the account info and section info into an Excel sheet and logout

# 6. re-open the shop page and call the login info from the Excel sheet and log in the page

# 7. Verify the sections information are displayed



# ATTEMPTED TO FILL OUT FORM INSIDE IFRAME COMPONENT FOR SIGN UP FORM:
class AddPage(BasePage):

	def add_contact(self,data):
		try:
			element = WebDriverWait(self.driver, self.timeout).until(
				EC.visibility_of_element_located((AddPageLocators.FIRSTNAME))
				)
		except NoSuchElementException:
			print ("element not found")
		if data["firstName"]:
			self.driver.find_element(*AddPageLocators.FIRSTNAME).send_keys(data["firstName"])
		self.driver.find_element(*AddPageLocators.LASTNAME).send_keys(data["lastName"])
		self.driver.find_element(*AddPageLocators.EMAIL).send_keys(data["email"])
		# PASSWORD + VERIFY PASSWORD + DATE OF BIRTH + CREATE BTN

		try:
			self.driver.find_element(*MainPageLocators.LOADER)
			element = WebDriverWait(self.driver, self.timeout).until_not(
				EC.visibility_of_element_located((MainPageLocators.LOADER))
				)
		except NoSuchElementException:
			print ("loader not found")
