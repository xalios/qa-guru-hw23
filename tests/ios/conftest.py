import os
import allure
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selene import browser
from config import settings

from helpers.attachments import add_screenshot


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
            "userName": settings.bstack_user,
            "accessKey": settings.bstack_key,
        }
    })

    browser.config.driver = webdriver.Remote(
        settings.bstack_url,
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    with allure.step('Test resources: '):
        add_screenshot(browser)

    yield

    browser.quit()
