import time

from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage
from src.pages.sku_list_page import ListSkusPage


class TestSkuPage:
    def testViewSkuList(self, safari_driver):

        link = "https://admin.dev.halterranch.com/signin"
        loginPage = LoginPage(safari_driver, link)
        loginPage.open()
        loginPage.logIn("admin@halterranch.com", "click_here_to_obtain_good_adm1n_password_EXE")
        time.sleep(1)

        basePage = BasePage(safari_driver, link)
        basePage.openNavOption("Product Management","SKUs")
        time.sleep(1)

        listPage = ListSkusPage(safari_driver, link)
        listPage.verifySkuListShown()