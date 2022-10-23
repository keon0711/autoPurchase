import time
from datetime import datetime

import pause as pause
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_url = 'https://accounts.nike.com/lookup?client_id=4fd2d5e7db76e0f85a6bb56721bd51df&redirect_uri=https://www.nike.com/auth/login&response_type=code&scope=openid%20nike.digital%20profile%20email%20phone%20flow%20country&state=eadebc8d611e4ffaa0b731b6b4ce9331&code_challenge=xFH1Ql6sMRcRQ42n7uL4fi0hUrhUsb_gD-IcfhoGOP4&code_challenge_method=S256'
product_url = 'https://www.nike.com/kr/launch/t/air-max-1-hangul-day'
my_id = 'thisismyid'
my_pw = 'thisismypw'


start_year = 2019
start_month = 2
start_date = 27
start_hour = 20
start_min = 0

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get(login_url)

try:
    # 클릭할 수 있을 때까지 기다리다가 id와 pw를 입력 후 버튼 클릭
    id_elem = wait.until(EC.element_to_be_clickable((By.ID, "userID")))
    pass_elem = driver.find_element_by_id("userPW")

    id_elem.send_keys(my_id)
    pass_elem.send_keys(my_pw)

    login_elem = driver.find_element_by_id("loginBtn")
    login_elem.click()

except:
    pass

# 지정한 시간까지 기다리다가 제품 구매 페이지 로드
pause.until(datetime(start_year, start_month, start_date, start_hour, start_min, 00))
driver.get(product_url)

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'ncss-btn-primary-dark')))
driver.find_element_by_xpath("//button [contains(text(), '260')]") # 사이즈 선택
driver.find_element(By.CLASS_NAME, "ncss-btn-primary-dark") # 구매버튼 클릭

WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-md')))
driver.find_element(By.CLASS_NAME, "btn-md") # 결제 버튼 클릭
driver.find_element(By.ID, "KakaoPay") # 결제수단 선택
driver.find_element(By.CLASS_NAME, "btn-md") # 주문하기 버튼 클릭