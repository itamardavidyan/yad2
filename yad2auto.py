from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
options.add_argument('--headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(executable_path=r'C:\\python\\yad2\drivers\\chromedriver.exe', chrome_options=options)

driver.get('http://www.yad2.co.il/')
driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0, 200)") 
driver.implicitly_wait(5)
# take screenshot
driver.get_screenshot_as_file('main-page.png')

# enter email
element = driver.find_element_by_css_selector('#login_email')
element.send_keys('itamardavidyan@gmail.com')

# enter password
element = driver.find_element_by_xpath("//*[@id=\"mockpass\"]/td/input")
element.click()
element = driver.find_element_by_xpath("//*[@id=\"Irealpass\"]")
element.send_keys('Yad2Pass')

# click login button
element = driver.find_element_by_xpath("//*[@id=\"mainIndex\"]/div[2]/div[4]/form/div/table/tbody/tr[4]/td/input")
element.click()

# take screenshot
driver.get_screenshot_as_file('login-page.png')

# move to AD
driver.get('https://my.yad2.co.il/newOrder/index.php?action=personalAreaFeed&CatID=3&SubCatID=0')

# take screenshot
driver.get_screenshot_as_file('ad-page.png')

# open ad
element = driver.find_element_by_xpath("//*[@id=\"feed\"]/tbody/tr[2]/td[9]/div")
element.click()

# take screenshot
driver.get_screenshot_as_file('after-open-ad.png')

# update ad
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to.default_content()
element = driver.find_element_by_xpath("//*[@id=\"order_form\"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div")
element.click()

# take screenshot
driver.get_screenshot_as_file('after-updtae-page.png')

