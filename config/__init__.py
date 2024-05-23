from selenium import webdriver


def browser_cookie():
    driver = webdriver.Chrome()
    # 打开网页
    driver.get("https://www.douyin.com")
    # 获取浏览器cookie
    cookies = driver.get_cookies()

    for c in cookies:
        print(c)

    print("=======")
    print(driver.get_cookie("ttwid"))
    print("=======")
    driver.quit()
