#Craigslist Scraper with Python and Selenium

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraiglistScraper(object):
	#constructor -->
	def __init__(self, location, postal , max_price, radius):
		self.location = location
		self.postal = postal
		self.max_price = max_price
		self.radius = radius

		self.url = f"https://{location}.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}"


#search_distance=5&postal=94201&max_price=500

	def test(self):
		print(self.url)

location = 'sfbay'
postal = '94201'
radius = '5'
max_price = '1000'

scraper = CraiglistScraper(location,postal,max_price,radius)

scraper.test()