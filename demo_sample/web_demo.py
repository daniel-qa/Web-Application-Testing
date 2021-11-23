import time
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://google.com"
driver.get(url)
time.sleep(5)
driver.close()



# with webdriver.Firefox() as driver:
#	driver.get("http://baidu.com")
#	sleep(5)
	
