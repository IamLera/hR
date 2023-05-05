import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from .locators import LoginPageLocators as LPL
import math


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    # waits for an element to disappear

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # checks the presence of an element

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # checks the absence of an element

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # goes to the test_login page.

    def go_to_login_page(self):
        link = self.browser.find_element(*LPL.LOGIN_LINK)  # find a test_login link
        link.click()  # goes to test_login link

    # gets a link

    def open(self):
        self.browser.get(self.url)

    def openNavOption(self, option, suboption):
       # self.browser.find_element(By.CSS_SELECTOR, f'nav div span:contains("{option}")').findfirst().click()
        self.browser.find_elements(By.XPATH, f"//button/span/span[contains(text(), '{option}')]")[0].click()
        time.sleep(1)
        self.browser.find_elements(By.XPATH, f"//div[contains(@class,'mantine-NavLink-children')]/a/span/span[contains(text(), '{suboption}')]")[0].click()

