# Using the firefox browser navigate to https //www.google.com /
# enter the text Python in the search box, then send the Enter key.
# Get the Text from the Wikipedia brief on the right side and print the value in the console.



import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



def send_keys_to_element(element, *keys):
    element.send.keys(keys)




def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    element = send_keys_to_element(driver.find_element(By.TAG_NAME, "input"), "python")
    enterkey = send_keys_to_element()driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input').click()
    pythontext = driver.find_element((By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/p[2]')
    time.sleep(5)
    print(pythontext.text)


if __name__ == '__main__':
    main()


