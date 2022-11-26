#Create a page object model for this page https://academy.testifyltd.com/courses/test-automation-simplified
#Create another object model for this page https://academy.testifyltd.com/courses/switch-to-software-testing
#The web elements in each of your object models should not be more than 5.


class TestAutomationSimplified:



import time
from pythonSel_TAS import TestAutomationSimplified
from pythonSel_STST import SwitchToSoftwareTesting
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
    test_automation_simplified = TestAutomationSimplified(driver)
    switch_software_testing = SwitchToSoftwareTesting(driver)
    print(test_automation_simplified)
    print(switch_software_testing)


if  __name__ == '__main__':
    main()