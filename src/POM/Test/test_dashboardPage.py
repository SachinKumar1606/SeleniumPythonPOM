from src.POM.Pages.loginPage import LoginPage
from src.POM.Test.base_test import BaseTest
from src.POM.Pages.dashboardPage import DashboardPage


class TestDashboardPage(BaseTest):

    def test_verifyCountOfProductsOnDashboardPage(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.countOfItems("6")

    def test_verifyProductIsAddedToCart(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.addProductToCart("Sauce Labs Bolt T-Shirt")
        self.dashboardPage.verifyProductAddToCart("1")

    def test_verifyMultipleProductIsAddedToCart(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.addProductToCart("Sauce Labs Bolt T-Shirt")
        self.dashboardPage.addProductToCart("Sauce Labs Bike Light")
        self.dashboardPage.addProductToCart("Sauce Labs Fleece Jacket")
        self.dashboardPage.verifyProductAddToCart("3")

    def test_verifyProductIsAddedToCartAndRemove(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.addProductToCart("Sauce Labs Bike Light")
        self.dashboardPage.addProductToCart("Sauce Labs Fleece Jacket")
        self.dashboardPage.verifyProductAddToCart("2")
        self.dashboardPage.removeProductFromCart("Sauce Labs Bike Light")
        self.dashboardPage.verifyProductAddToCart("1")

    def test_verifyFilterFunctionllityFromAtoZ(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.selectFilterDropDownValue("Name (A to Z)")
        self.dashboardPage.verifySortedListAtoZ()

    def test_verifyFilterFunctionllityFromZtoA(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.selectFilterDropDownValue("Name (Z to A)")
        self.dashboardPage.verifySortedListZtoA()

    def test_verifyFilterFunctionllityForPrizeLowToHigh(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.selectFilterDropDownValue("Price (low to high)")
        self.dashboardPage.verifySortedListPrizeLowToHigh()

    def test_verifyFilterFunctionllityForPrizeHighToLow(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.selectFilterDropDownValue("Price (high to low)")
        self.dashboardPage.verifySortedListPrizeHighToLow()
