from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage
# Self.driver.find_elements(By.XPATH, '//app-card/div')

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, '//app-card/div')
    # find_element(By.XPATH, 'div[2]/button')
    cardAddButton = (By.CSS_SELECTOR, ".card-footer button")
    checkOutButton = (By.XPATH, "//li/a[contains(.,'Checkout ')]")
    # self.driver.find_element(By.XPATH, "//td/button[contains(.,'Checkout ')]").click()
    summaryPageCheckOutButton = (By.XPATH, "//td/button[contains(.,'Checkout ')]")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardAddButton(self):
        return CheckoutPage.cardAddButton

    def getCheckOutButton(self):
        # self.driver.find_element(By.XPATH, "//li/a[contains(.,'Checkout ')]").click()
        return self.driver.find_element(*CheckoutPage.checkOutButton)

    def getSummaryPageCheckOutButton(self):
        self.driver.find_element(*CheckoutPage.summaryPageCheckOutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


