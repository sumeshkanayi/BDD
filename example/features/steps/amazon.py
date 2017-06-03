from lettuce import step, world
from selenium.webdriver.common.keys import Keys
import time

@step("I'm on Amazon Home page")
def step_impl(step):
    world.browser.get("http://www.amazon.co.uk")

@step("I search for Software Testing")
def step_impl(step):
    element = world.browser.find_element_by_id("twotabsearchtextbox")
    element.send_keys("Software Testing")
    element.send_keys(Keys.RETURN)

@step("the browser title should have software testing")
def step_impl(step):
    time.sleep(2)
    assert "Amazon.co.uk: Software Testing" == world.browser.title