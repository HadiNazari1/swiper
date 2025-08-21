from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = "nabi.orfani@yahoo.com"
FB_PASSWORD = "23454455"  

service = Service(r"C:\Developers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)

driver.get("https://tinder.com")


wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q1862456778"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a/div[2]/div[2]/div'))).click()


wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q134075702"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div'))).click()


wait.until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[1])

# Enter Facebook login
email = wait.until(EC.presence_of_element_located((By.ID, "email")))
password = driver.find_element(By.ID, "pass")

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder
driver.switch_to.window(driver.window_handles[0])

# Handle popups
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Allow")]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not interested")]'))).click()
except:
    pass

# Like loop
for n in range(100):
    sleep(2)
    try:
        like_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Like"]')))
        like_button.click()
        print(f"Liked {n+1}")
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
