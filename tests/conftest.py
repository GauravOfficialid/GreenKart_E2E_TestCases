import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def Setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    # Firefox
    elif browser_name == "firefox":
        service_obj = Service("C:\WebDrivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    # Microsoft Edge
    elif browser_name == "IE":
        service_obj = Service("C:\WebDrivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver
    yield
    driver.close()
