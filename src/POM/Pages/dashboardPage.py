from selenium.webdriver.common.by import By

from src.POM.Pages.basePage import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    inventoryList = By.XPATH, "//div[@class='inventory_item']"
    inventoryPageSideMenu = By.XPATH, "//div[@class='bm-burger-button']/button"
    addToCartButton = "//div[contains(text(), '{productName}')]/ancestor::div[@class='inventory_item_description']/div/button"
    removeFromCartButton = "//div[contains(text(), '{productName}')]/ancestor::div[@class='inventory_item_description']/div/button"
    cartCount = By.XPATH, "//div/a/span"
    filterDropDown = By.XPATH, "//span[@class='select_container']"
    filterDropDownValue = "//select/option[contains(text(),'{filName}')]"
    selectedFilter = "//span[contains(text(),'{selectedFilterName}')]"
    elementsName = "(//div/a/div)"
    elementsPrize = "(//div[@class='pricebar']/div)"
    cartLink = By.XPATH, "//a[@class='shopping_cart_link']"
    productDescription = "//div[contains(text(), '{productName}')]/ancestor::div[@class='inventory_item_label']/div"

    def countOfItems(self, eleCount):
        count = self.get_count(self.inventoryList)
        assert eleCount in str(count)

    def addProductToCart(self, product):
        productToAdd = By.XPATH, self.addToCartButton.format(productName=product)
        self.do_click(productToAdd)

    def verifyProductAddToCart(self, noOfProducts):
        cartCount = self.get_element_text(self.cartCount)
        assert cartCount in cartCount

    def selectFilterDropDownValue(self, filterName):
        filterToSelect = By.XPATH, self.filterDropDownValue.format(filName=filterName)
        self.do_click(self.filterDropDown)
        self.do_click(filterToSelect)
        selectedFilter = By.XPATH, self.selectedFilter.format(selectedFilterName=filterName)
        isFilterSelected = self.is_visible(selectedFilter)
        assert isFilterSelected

    def removeProductFromCart(self, product):
        productToRemove = By.XPATH, self.addToCartButton.format(productName=product)
        self.do_click(productToRemove)

    def verifySortedListAtoZ(self):
        allElementsName = self.get_elements_list((By.XPATH, self.elementsName))
        sortedElementList = sorted(allElementsName)
        assert allElementsName == sortedElementList

    def verifySortedListZtoA(self):
        allElementsName = self.get_elements_list((By.XPATH, self.elementsName))
        sortedElementList = sorted(allElementsName, reverse=True)
        assert allElementsName == sortedElementList

    def verifySortedListPrizeLowToHigh(self):
        allElementsName = self.get_elements_list((By.XPATH, self.elementsPrize))
        elementListOriginal = []
        for item in allElementsName:
            elementListOriginal.append(item.replace("$", ''))
        sortedElementList = sorted(elementListOriginal, key=lambda x: float(x))
        assert sortedElementList == elementListOriginal

    def verifySortedListPrizeHighToLow(self):
        allElementsName = self.get_elements_list((By.XPATH, self.elementsPrize))
        elementListOriginal = []
        for item in allElementsName:
            elementListOriginal.append(item.replace("$", ''))
        sortedElementList = sorted(elementListOriginal, key=lambda x: float(x), reverse=True)
        assert sortedElementList == elementListOriginal

    def navigateToCartPage(self):
        self.do_click(self.cartLink)

    def getProductDescription(self, product):
        productDescription = By.XPATH, self.productDescription.format(productName=product)
        productDescriptionText = self.get_element_text(productDescription)
        return productDescriptionText
