from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constant
import time


def auto_click(email, password):
    options = webdriver.ChromeOptions()
    options.binary_location = constant.CHROMELOCATION
    options.add_argument("--headless")
    options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(
        executable_path=constant.CHROMEDRIVER, chrome_options=options
    )

    ITEMS = [
        "https://my.yad2.co.il/newOrder/index.php?action=personalAreaViewDetails&CatID=3&SubCatID=0&OrderID=36970528",
        "https://my.yad2.co.il/newOrder/index.php?action=personalAreaViewDetails&CatID=3&SubCatID=0&OrderID=37257498"
    ]
    connect(driver, email, password)

    update_ad(driver, ITEMS[0])


def connect(driver, email, password):
    driver.get("http://www.yad2.co.il/")
    driver.implicitly_wait(2)

    # enter email
    try:
        element = driver.find_element_by_css_selector("#login_email")
        element.send_keys(email)
    except Exception as e:
        save_error(driver, "enter email", str(e))

    # enter password
    try:
        element = driver.find_element_by_xpath('//*[@id="mockpass"]/td/input')
        element.click()
        element = driver.find_element_by_xpath('//*[@id="Irealpass"]')
        element.send_keys(password)
    except Exception as e:
        save_error(driver, "enter password", str(e))

    # click login button
    try:
        element = driver.find_element_by_xpath(
            '//*[@id="mainIndex"]/div[2]/div[4]/form/div/table/tbody/tr[4]/td/input'
        )
        element.click()
    except Exception as e:
        save_error(driver, "click login button", str(e))


def update_ad(driver, item):
    # move to AD
    try:
        driver.get(item)
    except Exception as e:
        save_error(driver, "move to AD", str(e))

    # update ad
    try:
        element = driver.find_element_by_xpath('//*[@id="bounceRatingOrderBtn"]')
        element.click()
        driver.implicitly_wait(2)
    except Exception as e:
        save_error(driver, "update ad", str(e))

    # take screenshot
    timeStr = time.strftime("%d-%m-%Y") + "-" + time.strftime("%H-%M-%S")
    driver.get_screenshot_as_file("./screenshots/after-updtae-page-" + timeStr + ".png")


def save_error(driver, name, valueError):
    timeStr = time.strftime("%d-%m-%Y") + "-" + time.strftime("%H-%M-%S")
    path = "./errors/" + name + "-" + timeStr
    driver.get_screenshot_as_file(path + ".png")
    error_file = open(path + ".txt", "w")

    error_file.write(valueError)

    error_file.close()
