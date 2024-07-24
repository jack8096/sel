from selenium  import webdriver
from selenium.webdriver.firefox.service import Service

options = webdriver.FirefoxOptions()

driverService = Service(executable_path="/snap/bin/firefox.geckodriver")
driver = webdriver.Firefox(options = options, service= driverService)



driver.get("https:www.google.com")
driver.quit()
