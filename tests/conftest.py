import pytest
from selenium import webdriver


# @pytest.fixture(params=["firefox", "chrome"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        my_driver = webdriver.Firefox(options=options)
    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("-headless")
        my_driver = webdriver.Chrome(options=options)
    else:
        raise TypeError(f"Expected 'firefox' or 'chrome', but received {browser}")
    
    # my_driver.implicitly_wait(10)

    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="browser to execute tests (chrome or firefox)"
    )