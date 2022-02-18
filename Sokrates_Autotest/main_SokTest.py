#!/usr/bin/python
# -*- coding: utf-8 -*-

#=== Sokrates Auto Test =============================================
# Date    : 2022.02.17
# Program : main sok test
# Author  : daniel
#====================================================================
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep
from login import login
from sort_vedio import sort_vedio
from play_vedio import play_vedio
from add_evaluate import add_evaluate
from upload_vedio import upload_vedio
from edit_tbas import edit_tbas
from video_share import video_share
from my_public_comment import my_public_comment

class TestSok(unittest.TestCase):

	def setUp(self): # 每個測試初始化
	
		# login
		driver = webdriver.Firefox()
		#driver = webdriver.Chrome()
		driver.implicitly_wait(7)
		self.driver = driver
		url="https://sokrates.teammodel.org/"
		self.url = url
		login(driver,url)
		
	def tearDown(self): # 每個測試結束
		self.driver.quit()
		sleep(1)
		
	def sort_vedio(self): #要測試的功能, 名稱需test開頭
		sort_vedio(self.driver)
		
	def test_play_vedio(self): 
		play_vedio(self.driver)
		
	def test_add_evaluate(self):
		add_evaluate(self.driver)
		
	def upload_vedio(self):
		upload_vedio(self.driver)
		
	def edit_tbas(self):
		edit_tbas(self.driver)
	
	def video_share(self):
		video_share(self.driver,self.url)
	
	def my_public_comment(self):
		my_public_comment(self.driver,self.url)	
    
if __name__ == "__main__":
	unittest.main()

