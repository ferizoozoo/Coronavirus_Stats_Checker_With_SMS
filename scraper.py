import bs4
import requests

website_addr = 'https://www.worldometers.info/coronavirus/'

def scrap(addr):
	"""Return the BeautifulSoup instance of the website address.
	"""
	res = requests.get(addr)
	siteSoup = bs4.BeautifulSoup(res.text, 'html.parser')
	return siteSoup

def allCountries():
	"""Return a list of all countries with their statistics.
	"""
	soup = scrap(website_addr)
	countries = []

def eachCountry(country):
	"""Return the data of each country as a dictionary.
	"""
	country_addr = website_addr + f'country/{country}' 
	soup = scrap(country_addr)
	country_data = soup.find_all(attrs = { 'id': 'maincounter-wrap' })
	return {country_data[i].h1.text[:-1].strip() : country_data[i].span.text.strip() for i in range(len(country_data))}
