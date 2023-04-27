import time

from src.pages.login_page import LoginPage

class TestLoginPage:
    def testValidLogin(self, safari_driver):

        link = "https://admin.dev.halterranch.com/signin"
        loginPage = LoginPage(safari_driver, link)
        loginPage.open()
        loginPage.logIn("admin@halterranch.com", "click_here_to_obtain_good_adm1n_password_EXE")

    def testInvalidLogin(self, safari_driver):

        link = "https://admin.dev.halterranch.com/signin"
        loginPage = LoginPage(safari_driver, link)
        loginPage.open()
        loginPage.logIn("wrongMail@halterranch.com", "click_here_to_obtain_good_adm1n_password_EXE")
        time.sleep(10)

        loginPage.assertErrorMsgPresent()

