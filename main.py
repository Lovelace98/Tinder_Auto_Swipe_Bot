from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

options = Options()
service = Service()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version="116.0.5845.141").install(), options=options))

#Where to input your log in details
FB_EMAIL = "Where to enter your email"
FB_PASSWORD = "Where to enter your password"

#Grabs tinder's homepage
driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

#Clicks on the facebook log in option
sleep(2)
fb_login = driver.find_element(By.XPATH ,'//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)

#Create switces to switch between windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#This block of code finds and fills in the log in details
email = driver.find_element(By.XPATH,'//*[@id="email"]')
password = driver.find_element(By.XPATH,'//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

#This block switches to the tinder page
driver.switch_to.window(base_window)
print(driver.title)

#Clicks on accepts cookies and clicks on allow location button
sleep(5)
allow_location_button = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#this swipes through tinder 99 times because tinder allows 100 swipes per day
for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, 
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR ,".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()