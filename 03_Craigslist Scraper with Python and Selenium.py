#Craigslist Scraper with Python and Selenium

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

chromedriver = 'C:\\Users\\Hanokri2\\Documents\\Python\\chromedriver.exe'
#browser = webdriver.Chrome(chromedriver)
class CraiglistScraper(object):
	#constructor -->
	def __init__(self, location, postal , max_price, radius):
		self.location = location
		self.postal = postal
		self.max_price = max_price
		self.radius = radius

		self.url = f"https://{location}.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}"


#search_distance=5&postal=94201&max_price=500

		#self.driver = webdriver.Firefox()
		self.driver = webdriver.Chrome(chromedriver)
		self.delay = 3 

	def load_craiglist_url(self):
		self.driver.get(self.url)
		try:
			wait = WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, "searchform"))) #addig var amig meg nem jelenik egy elem
			#erdekes--> ( hiszti h nincs 3 parameter) -> ((nicns hiszti o.o ))

			print("betoltott az oldal")
		except TimeoutException:
			print('Loading is taking too much tome')

	def extract_post_information(self):
		all_post = self.driver.find_elements_by_class_name('result-row')
		
		dates = []
		titles = []
		prices = [] 


		for post in all_post:
			title = post.text.split("$")


			#stringet rendezz ha van az elejen '' akkor leveszi
			if title[0] == '':
				title = title[1]
				#title[''] = title[dollar]
			else:
				title = title[0]
				
			title = title.split("\n")
			price = title[0]
			title = title[-1] #utso elem
					#title[datum termek neve]

			title = title.split(" ") #felbonja space-ek alapjan
			month = title[0]
			day = title[1]
			title = ' '.join(title[2:])
			date = month + ' ' + day
			#month = date[0]
			#day = date[1]

			#print('Price --> ' + price )
			#print('Title ==> ' + title)
			#print('Selling date -> ' + month + ' '+ day )
			#print("\n")

			titles.append(title)
			dates.append(date)
			prices.append(price)
		return titles, prices, dates


			#print(post.text) #kivonja a szoveget a html-bol
			


	def extract_post_url(self):
		url_list = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, 'lxml')
		for link in soup.findAll('a',{'class': 'result-title hdrlnk'}):
			print(link['href'])
			url_list.append(link['href'])
		return url_list

	def quit(self):
		self.driver.close()


location = 'sfbay'
postal = '94201'
radius = '5'
max_price = '1000'

scraper = CraiglistScraper(location,postal,max_price,radius)
scraper.load_craiglist_url()
titles, prices, dates = scraper.extract_post_information()
print(titles)
#scraper.extract_post_url()
scraper.quit( )
