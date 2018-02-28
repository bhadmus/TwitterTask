from selenium import webdriver
import time

browser = webdriver.Chrome(r'C:\Users\Ademola Bhadmus\Documents\FeedbackHub\drivers\chromedriver.exe')
browser.get('http://www.twitter.com/')
browser.maximize_window()
time.sleep(4)
# steps to login using the login button option
browser.find_element_by_css_selector('a.StaticLoggedOutHomePage-input').click()
time.sleep(3)
browser.find_element_by_css_selector('.js-username-field').send_keys('b@gmail.com')
browser.find_element_by_css_selector('.js-password-field').send_keys('Password')
browser.find_element_by_css_selector('button.submit').click()
time.sleep(3)
# steps to post a tweet
browser.find_element_by_css_selector('#global-new-tweet-button').click()
browser.find_element_by_xpath('/html/body/div[33]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]').send_keys('This tweet was sent with automation using python. Final test of test case one.')
browser.find_element_by_xpath('/html/body/div[33]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/span/button[2]').click()
time.sleep(5)
# steps to logout
browser.find_element_by_css_selector('#user-dropdown-toggle').click()
time.sleep(2)
browser.find_element_by_css_selector('#signout-button').click()
time.sleep(5)
browser.close()
