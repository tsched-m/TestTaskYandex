import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser) -> None:
    """ Функция для считывания параметров командной строки pytest """

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nЗапуск CHROME для тестов...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nЗапуск FIREFOX для тестов")
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        print("\nЗапуск EDGE для тестов")
        browser = webdriver.Edge()
    else:
        raise pytest.UsageError("--browser_name должно быть chrome, firefox или edge")

    yield browser

    print("\nЗакрытие браузера...")
    browser.quit()
