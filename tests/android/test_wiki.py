import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_article_page_error():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selenium')
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).element_by(
            have.text("software")).click()

    with allure.step('Verify content found'):
        result = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_text'))
        result.should(have.text("An error occurred"))


