from selenium.webdriver.common.by import By


class SwitchToSoftwareTesting:

    def  __int__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.title = driver.find_element(By.TAG_NAME, 'h1')
