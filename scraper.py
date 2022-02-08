import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options = chrome_options) 
  return driver
  

if __name__ == "__main__":
  
  instagram_url = "https://www.instagram.com/"

  driver = get_driver()
  login_instagram = "div"
  tag_login_instagram = driver.find_elements(By.TAG_NAME,login_instagram)
  print(f'found  {len(tag_login_instagram)}')
  
  
  

