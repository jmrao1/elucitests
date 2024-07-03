import time
from behave import *
from selenium import webdriver


@given('the learning Elucidat page is displayed')
def elucidatPage(context):
    context.driver = webdriver.Chrome()


@when('the start button clicked')
def startButton(context):
    context.driver.get("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")
    time.sleep(5)
    start = context.driver.find_element("xpath", '//*[@id="pa_5c9126fe3b767_p15577f075e9-button__text"]')
    start.click()


@then('the label text to be matched with "{phrase}"')
def labelText(context, phrase):
    time.sleep(5)
    find_truth = context.driver.find_element("xpath", '//*[@id="pa_5c9126fe3f4fb_p15511bbebad-pageTitle"]/strong')
    truth_text = find_truth.text
    assert truth_text == phrase
    context.driver.close()
