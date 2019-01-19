from selenium import webdriver
path = "./chromedriver.exe"

# Headless Mode 옵션 추가
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")


def weather_crawling(input_location):   # input_location: 유저가 입력한 지역
    driver = webdriver.Chrome(path, chrome_options=options)
    driver.get('http://www.google.com')
    # driver.implicitly_wait(2)
    searchbox = driver.find_element_by_name("q")
    searchbox.send_keys(input_location + "날씨")

    searchbox.submit()
    # driver.implicitly_wait(3)
    degree = driver.find_element_by_id("wob_tm").text   # 현재 기온
    location = driver.find_element_by_id("wob_loc").text    # 지역
    high = driver.find_element_by_xpath('//*[@id="wob_dp"]/div[1]/div[3]/div[1]/span[1]').text  # 최고 기온
    low = driver.find_element_by_xpath('//*[@id="wob_dp"]/div[1]/div[3]/div[2]/span[1]').text   # 최저 기온
    rain = driver.find_element_by_id("wob_pp").text     # 강수확률
    driver.close()
    # 출력 메세지
    output = "지금 " + location + "의 기온은 " + degree + "도, 최저/최고 기온은 " + low + "/" + high + "도 이고, 강수확률은 " + rain + " 입니다."
    if int(rain[0]) > 50:
        output = output + "\n우산을 챙기시는게 좋을 거에요."
    return output


#slack_message = "지금 " + location + "은 " + degree + "입니다"
#slack_notify(slack_message, '#random', username="날씨봇")
