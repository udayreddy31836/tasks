from behave import given, when, then
from selenium import webdriver

# Set up a Selenium WebDriver (you may need to configure this based on your project)
browser = webdriver.Chrome()

@given('I open the website "{url}"')
def step_open_website(context, url):
    context.browser.get(url)

@when('I click on the element with ID "{element_id}"')
def step_click_element_by_id(context, element_id):
    element = context.browser.find_element_by_id(element_id)
    element.click()

@when('I enter "{text}" into the input field with ID "{input_id}"')
def step_enter_text_into_input(context, text, input_id):
    input_element = context.browser.find_element_by_id(input_id)
    input_element.send_keys(text)

@then('I should see "{text}" on the page')
def step_should_see_text(context, text):
    page_source = context.browser.page_source
    assert text in page_source

@then('I should not see "{text}" on the page')
def step_should_not_see_text(context, text):
    page_source = context.browser.page_source
    assert text not in page_source
