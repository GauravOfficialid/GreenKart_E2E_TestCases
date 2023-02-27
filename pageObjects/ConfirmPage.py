from selenium.webdriver.common.by import By


class ConfirmPage:
    searchField = (By.XPATH, '//input[@id="country"]')
    allSuggestion = (By.CSS_SELECTOR, ".suggestions ul li")
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    # self.driver.find_element(By.XPATH, '//input[@value="Purchase"]').click()
    purchaseButton = (By.XPATH, '//input[@value="Purchase"]')

    # self.driver.find_element(By.XPATH, "//*[contains(@class,'alert')]")
    alertMessage = (By.XPATH, "//*[contains(@class,'alert')]")

    def __init__(self, driver):
        self.driver = driver
        # self.driver.find_element(By.XPATH, '//input[@id="country"]').send_keys("ind")

    def getSearchField(self):
        return self.driver.find_element(*ConfirmPage.searchField)

    def getAllSuggestion(self):
        return self.driver.find_elements(*ConfirmPage.allSuggestion)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchanseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)
    def getAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alertMessage)