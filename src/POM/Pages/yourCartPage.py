from selenium.webdriver.common.by import By

from src.POM.Pages.basePage import BasePage


class YourCartPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    itemName = By.XPATH, "//div[@class='inventory_item_name']"
    itemDescription = By.XPATH, "//div[@class='inventory_item_desc']"
    continueShoppingButton = "//button[@data-test='continue-shopping']"
    checkoutButton = "//button[@data-test='checkout']"
    checkoutButtonCount = "//span[@class='shopping_cart_badge']"
    itemCount = "//div[@class='cart_item']"

    def verifyAddedProductName(self, productName):
        addedIemName = self.get_element_text(self.itemName)
        assert productName in addedIemName

    def verifyAddedProductDescription(self, productDescription):
        addedItemDesc = self.get_element_text(self.itemDescription)
        assert productDescription in addedItemDesc
