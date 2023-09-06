import os
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "iOS",
        "platformVersion": "15",
        "deviceName": "iPhone 13",

        # Set URL of the application under test
        "app": "bs://ff93298f86024b27db6aa0a4ad0bd89c336a4f14",

        "printPageSourceOnFindFailure": True,

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-5",
            "sessionName": "BStack second-one",

            # Set your access credentials
            "userName": os.getenv('BSTACK_USER'),
            "accessKey": os.getenv('BSTACK_KEY'),
        }
    })

    browser.config.driver = webdriver.Remote(
        'http://hub.browserstack.com/wd/hub',
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()


