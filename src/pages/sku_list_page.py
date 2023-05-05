import time

from .base_page import BasePage
from .locators import ListSkuLocators as LSL
class ListSkusPage(BasePage):

    def verifySkuListShown(self):
        gridName = self.browser.find_element(*LSL.gridName)
        # Assert that the element is present
        assert gridName is not None, "Element not found"

        grid = self.browser.find_element(*LSL.grid)
        # Assert that the element is present
        assert gridName is not None, "Element not found"