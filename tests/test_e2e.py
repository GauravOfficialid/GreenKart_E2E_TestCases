from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e23(self):
        log = self.getLogger()
        productToAdd = "Samsung Note 8"
        homePage = HomePage(self.driver)  # connection to HomePage
        checkOutPage = homePage.ShopItems()
        print(self.driver.current_url)

        allProducts = checkOutPage.getCardTitles()
        log.info("Getting all the cad titles")
        allProductNames = []
        for productname in allProducts:
            allProductNames.append(productname.find_element(By.XPATH, 'div/h4').text)
            if productname.find_element(By.XPATH, 'div/h4').text == productToAdd:
                productname.find_element(*checkOutPage.getCardAddButton()).click()
                break

        log.info(allProductNames)
        print(allProductNames)

        checkOutPage.getCheckOutButton().click()

        confirmPage = checkOutPage.getSummaryPageCheckOutButton()
        log.info("Entering country name as ind")
        confirmPage.getSearchField().send_keys("ind")

        allSuggestion = confirmPage.getAllSuggestion()
        for suggestion in allSuggestion:
            if suggestion.text == "India":
                suggestion.click()
                break

        confirmPage.getCheckBox().click()

        confirmPage.getPurchanseButton().click()

        print(confirmPage.getAlertMessage().text)

        successMessage = confirmPage.getAlertMessage().text
        log.info(" Text Received from application is   :- " + successMessage)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)" in successMessage
