from selenium import webdriver

from slckbot import slack_notify

path = "./chromedriver.exe"

# Headless Mode 옵션 추가
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(path, chrome_options=options)
driver.get('http://www.google.com')
driver.implicitly_wait(2)
searchbox = driver.find_element_by_name("q")
searchbox.send_keys("날씨")

searchbox.submit()
driver.implicitly_wait(3)
degree = driver.find_element_by_id("wob_tm").text
location = driver.find_element_by_id("wob_loc").text
print("지금", location, "은", degree, "도 입니다.")

slack_message = "지금 " + location + "은 " + degree + "입니다"
slack_notify(slack_message, '#random', username="날씨봇")
