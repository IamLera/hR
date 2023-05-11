import pytest
from selenium import webdriver

from src.api.services.requests.login_reg import LoginReq


@pytest.fixture
def safari_driver():
    # Set up Safari driver
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    # Clean up driver
    driver.quit()

@pytest.fixture
def api_login():
    email = "admin@halterranch.com"
    pswrd = "click_here_to_obtain_good_adm1n_password_EXE"

    lR = LoginReq(email, pswrd)
    lR.login()