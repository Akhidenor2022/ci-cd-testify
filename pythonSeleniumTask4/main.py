#Navigate to the website https://www.facebook.com/
#Find the email box and enter an email value
#Find the password box and enter a password value
#Find the Login button and click it




import  time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_key_to_element(element, keys):
    element.send_keys(keys)



    def main():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.facebook.com/")
        send_key_to_element(driver.find_element(By.NAME, "email"), "qaremita@gmail.com")
        send_key_to_element(driver.find_element(By.NAME, "password"), "Password12@")
        driver.find_element((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button').click)


        time.sleep(10)


    if  __name__ == '__main__':
        main()



