from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constant
import time

count = 0


def auto_click(email, password):
    options = webdriver.ChromeOptions()
    options.binary_location = constant.CHROMELOCATION
    options.add_argument("--headless")
    options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(
        executable_path=constant.CHROMEDRIVER, chrome_options=options
    )

    driver.get("http://www.yad2.co.il/")
    driver.implicitly_wait(2)
    driver.execute_script("window.scrollTo(0, 200)")
    # driver.implicitly_wait(2)
    # # take screenshot
    # driver.get_screenshot_as_file("main-page.png")

    # enter email
    try:
        element = driver.find_element_by_css_selector("#login_email")
    except ValueError:
        save_error(driver, "#login_email", ValueError)



    element.send_keys(email)

    # enter password
    element = driver.find_element_by_xpath('//*[@id="mockpass"]/td/input')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="Irealpass"]')
    element.send_keys(password)

    # click login button
    element = driver.find_element_by_xpath(
        '//*[@id="mainIndex"]/div[2]/div[4]/form/div/table/tbody/tr[4]/td/input'
    )
    element.click()

    # take screenshot
    # driver.get_screenshot_as_file("login-page.png")

    # move to AD
    driver.get(
        "https://my.yad2.co.il/newOrder/index.php?action=personalAreaFeed&CatID=3&SubCatID=0"
    )

    # take screenshot
    # driver.get_screenshot_as_file("ad-page.png")

    # open ad
    element = driver.find_element_by_xpath('//*[@id="feed"]/tbody/tr[2]/td[9]/div')
    element.click()

    # take screenshot
    # driver.get_screenshot_as_file("after-open-ad.png")

    # update ad
    iframes = driver.find_elements_by_tag_name("iframe")
    print("<--- iframes --->")
    print(iframes)
    driver.switch_to.frame(iframes[5])
    element = driver.find_element_by_xpath('//*[@id="bounceRatingOrderBtn"]/span')
    element.click()
    driver.implicitly_wait(1)

    driver.switch_to.default_content()
    driver.execute_script("window.scrollTo(0, 200)")
    driver.implicitly_wait(1)

    # take screenshot
    timeStr = time.strftime("%d-%m-%Y") + "-" + time.strftime("%H-%M-%S")
    print(timeStr)
    driver.get_screenshot_as_file("./screenshots/after-updtae-page-" + timeStr + ".png")
    driver.implicitly_wait(1)


def save_error(driver, name, valueError):
    timeStr = time.strftime("%d-%m-%Y") + "-" + time.strftime("%H-%M-%S")
    path = "./errors/" + name + "-" + timeStr
    driver.get_screenshot_as_file(path + ".png")
    error_file = open(path + ".text", "x")
    error_file = open(path,'w')

    error_file.write(valueError)

    error_file.close()