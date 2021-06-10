#!/usr/bin/python
# -*- coding: utf-8 -*-

#===  Auto Test =====================================================
# Date    : 2021.06.10
# Program : play_vedio
# Author  : daniel
#====================================================================
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep
from login import login
#====================================================================
# function :play_vedio
# Parameter :	
#	driver->must given

# Switch new windows , (限用只有兩個 Windows 的情況)
def switch_new_windows(driver,before_window_handle ):
	
	nowhandle = before_window_handle
	#記住點擊後窗口
	nowhandle2 = driver.current_window_handle
	
	if( nowhandle == nowhandle2 ):
		#print("current windows is still the same")
		
		#獲得所有窗口
		allhandles = driver.window_handles
		#循環判斷窗口是否為當前窗口
		
		#print('allhandles len : ' + str(len(allhandles)))
		
		# 換成新的視窗
		for handle in allhandles:
			if( handle != nowhandle):
				#print('swith to new windows!')
				driver.switch_to_window(handle)
				#print('Already switch new window!')
	else:
		print("current windows is new windows")

# play_vedio
def play_vedio(driver):
    
    # MyVedio
    print('MyVedio')    
    
    element = driver.find_element_by_xpath("//a[@href='#/myMovie']")
    element.click()
    
    # Locate ivu-icon-android-menu element
    element = driver.find_element_by_xpath("//i[contains(@class,'ivu-icon-android-menu')]")
    element.click()
    
    # click vedio img
    print('Click Vedio Img')    
    elements = driver.find_elements_by_xpath("//img[contains(@src,'/storage/tba/')]")
    elements[0].click()  
    
    # click vedio button
    print('Click Vedio Button')
    elements = driver.find_elements_by_xpath("//button[contains(@class,'ivu-btn-primary')]")
    elements[0].click()
    
    
    #記住現在窗口
    nowhandle = driver.current_window_handle				
    # 切換成新分頁
    switch_new_windows(driver,nowhandle)
    
    if(1):
        # Play vedio
        print('Play Vedio')
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID , "tbaplayer_video_player_html5_api")))
        element.click()        
        sleep(10)
        # Pause
        element.click()
        
        # Get Play Time        
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME , "vjs-current-time-display")))
        sec = element.text
        print(sec )
        #判斷是否有播放
        assert(sec !="00:00")
    
    return
    
if __name__== "__main__":
    print ("This is main function called")    
      
    # Web Driver    
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    
    # Set Implicitly Wait Time
    driver.implicitly_wait(7)
    
    # Login
    login(driver)	
    print("login finish " )
    
    # Play Vedio
    play_vedio(driver)
    
    # Close Web Driver
    driver.quit()
    

