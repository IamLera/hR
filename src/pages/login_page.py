from .base_page import BasePage
from .locators import LoginPageLocators as LPL
class LoginPage(BasePage):

    # registers a user

    def logIn(self, email, password):
        self.browser.find_element(*LPL.emailField).send_keys(email)  # enters a random email
        self.browser.find_element(*LPL.passwordField).send_keys(password)  # enters a random password
        self.browser.find_element(*LPL.loginBtn).click()  # clicks the "Register" button

    def assertErrorMsgPresent(self):
        errorMsg = self.browser.find_element(*LPL.errorMsg)
        # Assert that the element is present
        assert errorMsg is not None, "Element not found"
        assert errorMsg.text == "Wrong email or password", "wrong message provided - "+ errorMsg.text
