from lettuce import *
from selenium import webdriver
@before.all
def starting():
    print "Hello starting test case"
    world.browser=webdriver.Chrome()


@after.all
def closeEverything(total):
    print "Total %d of %d scenarios passed " %(total.scenarios_ran,total.scenarios_passed)
    world.browser.quit()



