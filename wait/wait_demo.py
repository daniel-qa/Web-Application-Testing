from selenium import webdriver
driver = webdriver.Firefox()

driver.implicitly_wait(30)  # 隐性等待，最长等30秒
driver.get('https://your.url')
print driver.current_url
driver.quit()


# 顯示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.expected_conditions import element_to_be_clickable 

# 直接抓取 element
element=WebDriverWait(driver,30).until(element_to_be_clickable((By.ID,'q1A')))
element.click()

element =WebDriverWait(driver, 60).until(visibility_of_element_located((By.CSS_SELECTOR, ".my-sokrates-menu")))
element.click()

# 等待结果加载
WebDriverWait(driver, 60).until(visibility_of_element_located((By.ID, 'grView')))

driver.get('https://www.baidu.com/')
baidu_input = (By.ID, 'kw')
WebDriverWait(driver,10).until(visibility_of_element_located(baidu_input))



