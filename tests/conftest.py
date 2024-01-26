import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://todomvc.com/examples/emberjs/todomvc/dist/"
    browser.config.timeout = 2.0
    #browser.config.driver_name = "firefox"
    #browser.config.driver_options = webdriver.FirefoxOptions()
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    #browser.config.driver_options = driver_options
    browser.config.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()),
                                             options=driver_options)

    yield

    browser.quit()
