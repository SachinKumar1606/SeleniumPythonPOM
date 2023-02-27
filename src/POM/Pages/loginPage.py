from selenium.webdriver.common.by import By

from src.POM.Pages.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    userNameInput = By.XPATH, "//input[@data-test='username']"
    passwordInput = By.XPATH, "//input[@data-test='password']"
    loginButton = By.XPATH, "//input[@data-test='login-button']"
    dashboardProduct = By.XPATH, "//div/span[text()='Products']"
    errorMsg = By.XPATH, "//div/h3"

    def login(self, username, password):
        self.do_send_keys(self.userNameInput, username)
        self.do_send_keys(self.passwordInput, password)
        self.do_click(self.loginButton)

    def verifyUserIsLogin(self):
        visible = self.is_visible(self.dashboardProduct)
        assert visible

    def verifyUserIsNotAbleToLogin(self):
        errorText = self.get_element_text(self.errorMsg)
        assert "Epic sadface: Sorry, this user has been locked out." in errorText
