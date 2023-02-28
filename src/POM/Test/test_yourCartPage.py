from src.POM.Pages.loginPage import LoginPage
from src.POM.Pages.yourCartPage import YourCartPage
from src.POM.Test.base_test import BaseTest
from src.POM.Pages.dashboardPage import DashboardPage


class TestYourCartPage(BaseTest):

    def test_verifyProductIsAddedToCartAndVerifyProductName(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.yourCartPage = YourCartPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.addProductToCart("Sauce Labs Bolt T-Shirt")
        self.dashboardPage.verifyProductAddToCart("1")
        self.dashboardPage.navigateToCartPage()
        self.yourCartPage.verifyAddedProductName("Sauce Labs Bolt T-Shirt")

    def test_verifyProductDescriptionForTheProductAddedToCart(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.yourCartPage = YourCartPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        self.dashboardPage.addProductToCart("Sauce Labs Bolt T-Shirt")
        self.dashboardPage.verifyProductAddToCart("1")
        productDesc = self.dashboardPage.getProductDescription("Sauce Labs Bolt T-Shirt")
        self.dashboardPage.navigateToCartPage()
        self.yourCartPage.verifyAddedProductName("Sauce Labs Bolt T-Shirt")
        self.yourCartPage.verifyAddedProductDescription(productDesc)
