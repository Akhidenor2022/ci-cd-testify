import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
def print_element_attributes(element):
    print("Class:", element.get_attribute.text)



    def main():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://academy.testifyltd.com/")
        testify_limited_link:WebElement = driver.find_element(By.LINK_TEXT, "testify")
        print_element_attributes(testify_limited_link)



        if  __name__  ==  '__main__':
            main()

