#Craigslist Scraper with Python and Selenium

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

#chromedriver = 'D:/Projects/LOG/Python/00_INSTALLs/chromedriver.exe'
chromedriver = 'C:\\Users\\Hanokri2\\Documents\\Python\\chromedriver.exe'
#browser = webdriver.Chrome(chromedriver)
class AlbeeScraper(object):
	#constructor -->
	def __init__(self, dij, tipus , megye, meret):
		self.dij = dij
		self.tipus = tipus
		self.megye = megye
		self.meret = meret

		#self.url = f"https://{location}.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}"

		self.url1 = f"https://www.alberlet.hu/kiado_alberlet/berleti-dij:{dij}/ingatlan-tipus:{tipus}/megye:{megye}/meret:{meret}/szoba:1-2/limit:24"

#https://www.alberlet.hu/kiado_alberlet/
#berleti-dij:0-120-ezer-ft/
#ingatlan-tipus:lakas/
#megye:budapest/
#meret:40-65-m2/
#szoba:1-2/
#limit:24
#//*[@id="breadcrumbs"]
#search_distance=5&postal=94201&max_price=500

		#self.driver = webdriver.Firefox()
		self.driver = webdriver.Chrome(chromedriver)
		self.delay = 4 

	def load_albeeList_url(self):
		self.driver.get(self.url1)
		try:
			wait = WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, "breadcrumbs")))

			print("betoltott az oldal")
		except TimeoutException:
			print('Loading is taking too much time')

	def extract_post_titles(self):
		all_post = self.driver.find_elements_by_class_name('advert')
		post_title_list = []
		for post in all_post:
			title = post.text.split("$")

			title = title[0].split(" ")
			print(title[0])
			print(title[1])
			print(title[2])
			print(title[3])
			print(title[4])
			print(title[5])
			print(title[6])
			print(title[7])
			#print(post.text)
			post_title_list.append(post.text)
		return post_title_list

	def extract_post_url(self):
		url_list = []
		html_page = urllib.request.urlopen(self.url1)
		soup = BeautifulSoup(html_page, 'lxml')
		for link in soup.findAll('a',{'class': 'advert__image-link owl-lazy '}):
			print(link['href'])
			url_list.append(link['href'])
		return url_list

	def quit(self):
		self.driver.close()


dij = '0-110-ezer-ft'
tipus = 'lakas'
megye = 'budapest'
meret = '45-55-m2'

scraper = AlbeeScraper(dij,tipus,megye,meret)
scraper.load_albeeList_url()
scraper.extract_post_titles()
#scraper.extract_post_url()
scraper.quit()
