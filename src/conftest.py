import pytest
from selenium import webdriver

@pytest.fixture
def safari_driver():
    # Set up Safari driver
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    # Clean up driver
    driver.quit()