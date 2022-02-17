#!/usr/bin/python
# -*- coding: utf-8 -*-

#=== Sokrates Auto Test =============================================
# Date    : 2022.02.17
# Program : login
# Author  : daniel
#====================================================================
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep
import logging

#====================================================================
# function :login
# Parameter :	
#	driver->must given

# Login
def login(driver,url="https://sokrates.teammodel.org/exhibition/tbavideo#/"):
	
	
	#driver = webdriver.Firefox()
	#url="https://sokrates.teammodel.org/exhibition/tbavideo#/"
	
	driver.get(url)
	
	# Login button	
	element = driver.find_element_by_xpath("//i[contains(@class,'ivu-icon-person')]")
	element.click()
	
	# Wait Page Load Finish
	WebDriverWait(driver, 60).until(visibility_of_element_located((By.ID, 'loginId')))
	
	# TMID input ID/PWD 
	element = driver.find_element_by_id('loginId')
	element.send_keys('user')
	
	element = driver.find_element_by_id('loginPassword')
	element.send_keys('pwd')
	
	element = driver.find_element_by_id('loginButton')
	element.click()
	
	# check login status
	#driver.find_element_by_xpath("//i[contains(@class,'ivu-icon-person')]").is_displayed()


if __name__== "__main__":
	#print("This is main function called")
	
	# Web Driver
	
	driver = webdriver.Firefox()
	#driver = webdriver.Chrome()

	driver.implicitly_wait(7)
	
	login(driver)
	
	#print("login finish " )
	logging.warning("login finish ")
	
	sleep(35)
	# Close Web Driver
	driver.quit()
