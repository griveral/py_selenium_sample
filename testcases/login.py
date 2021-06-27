# Author: Giovanni Riveral
# version: 0.1
# Description: This test case covers
#     1. wrong credential 
#     2. successful login and landing page check

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

sleep_time = 1
def create_session():
    driver = webdriver.Chrome()
    driver.get('http://localhost:4200/login')
    username = driver.find_element_by_id('mat-input-0')
    password = driver.find_element_by_id('mat-input-1')
    login_btn = driver.find_element_by_xpath('/html/body/app-root/div/app-login-page/div/mat-card/mat-card-actions/button')

    # expected_url = 'http://localhost:4200/nav/home'
    # expected_title = 'Task Manager'

    username.send_keys('user')
    password.send_keys('user')
    # print('create session nabnab')
    time.sleep(sleep_time)
    login_btn.click()
    
    return driver

def wrong_credential():
    driver = webdriver.Chrome()
    driver.get('http://localhost:4200/login')
    username = driver.find_element_by_id('mat-input-0')
    password = driver.find_element_by_id('mat-input-1')
    login_btn = driver.find_element_by_xpath('/html/body/app-root/div/app-login-page/div/mat-card/mat-card-actions/button')
    username.send_keys('Gwapo')
    password.send_keys('user')
    login_btn.click()

    auth_failed_text = driver.find_element_by_id('mat-error-0').text
    # print(auth_failed_text)
    
    time.sleep(sleep_time)
    driver.close()

    if (auth_failed_text == "Wrong Credentials!"):
        # print('PASS')
        return 0    
    else:
        # print('FAILED')
        return 1

def landing_page():
    driver = webdriver.Chrome()
    driver.get('http://localhost:4200/login')
    username = driver.find_element_by_id('mat-input-0')
    password = driver.find_element_by_id('mat-input-1')
    login_btn = driver.find_element_by_xpath('/html/body/app-root/div/app-login-page/div/mat-card/mat-card-actions/button')

    expected_url = 'http://localhost:4200/nav/home'
    expected_title = 'Task Manager'

    username.send_keys('user')
    password.send_keys('user')
    time.sleep(sleep_time)
    login_btn.click()

    actual_url = driver.current_url
    actual_title = driver.title
    print('Actual url: {}'.format(actual_url))
    print('Page title: {}'.format(actual_title))
    time.sleep(1)
    driver.close()

    if (actual_url == expected_url) and (actual_title == expected_title):
        # print('Landing page - PASSED')
        return 0
    else:
        # print('Landing page - FAILED')
        return 1

if __name__ == "__main__":
    wc = wrong_credential()
    lp = landing_page()
    if (wc == 0):
        print('Wrong credential PASSED')
    else:
        print('Wrong credential FAILED')

    if (lp == 0):
        print('Landing Page PASSED')
    else:
        print('Landing Page - FAILED')
    
    
    
    