from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SHOP = (By.CSS_SELECTOR, '.bar-dropdown-link.bar-dropdown-1')
    SHOPMENU = (By.CSS_SELECTOR, '.navbar-toggler.d-lg-none')
    SIGNUP = (By.CSS_SELECTOR, '.icon-container.signin-or-signup__user-icon')
    FIRSTNAME = (By.CSS_SELECTOR, '*[ng-model="vm.model.firstName"]')
    LASTNAME = (By.CSS_SELECTOR, '*[ng-model="vm.model.lastName"]')    
    EMAIL = (By.CSS_SELECTOR, '*[ng-model="model.profile.email"]')
    NEWPASSWORD = (By.CSS_SELECTOR, '*[ng-model="vm.newPassword"]')
    VERIFYPASSWORD = (By.CSS_SELECTOR, '*[ng-model="vm.verifyPassword"]')

    #TODO:
#SAVE ACCOUNT AND SECTION INFO data:
# 4. Navigate down and capture the section info for the following sections on the page (used for verification later)

# 5. save the account info and section info into an Excel sheet and logout

# 6. re-open the shop page and call the login info from the Excel sheet and log in the page

# 7. Verify the sections information are displayed


class AddPageLocators(object):
    FIRSTNAME = (By.CSS_SELECTOR, '*[ng-model="vm.model.firstName"]')
    LASTNAME = (By.CSS_SELECTOR, 'input[ng-model="vm.contact.lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[ng-model="vm.contact.email"]')

    # PASSWORD + VERIFY PASSWORD + DATE OF BIRTH + CREATE BTN 
