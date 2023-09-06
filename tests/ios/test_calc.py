import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_sum():
    with allure.step('Open tab'):
        browser.element((AppiumBy.NAME, "3")).click()
        browser.element((AppiumBy.NAME, "+")).click()
        browser.element((AppiumBy.NAME, "2")).click()
        browser.element((AppiumBy.NAME, "=")).click()

    with allure.step('Verify content found'):
        result = browser.element((AppiumBy.NAME, "numberField"))
        result.should(have.text('5'))
