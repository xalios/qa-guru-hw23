import os
import allure
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv
from selene import browser
from helpers.attachments import add_screenshot


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-5",
            "sessionName": "BStack first_test",

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

    with allure.step('Test resources: '):
        add_screenshot(browser)

    browser.quit()
