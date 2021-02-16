import sys
import os.path
from os import path
import requests
from bs4 import BeautifulSoup

brands = ['adidas']

def adidas_get_price(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
	htmlPage = requests.get(url, headers=hdr, timeout=15)
	soup = BeautifulSoup(htmlPage.content, 'html.parser')
	htmlPrice = soup.find_all('div', class_='gl-price-item')
	price = htmlPrice[0]
	print(price)

def check_text_file_input(textFileInput):
	#print(textFileInput[0])
	if len(textFileInput) != 3:
		print('[ERROR]: Invalid syntax on line. Should be \'brand\' \'url\' \'price\'')
		return False
	if textFileInput[0] not in brands:
		print('[ERROR]: \'',textFileInput[0], '\' not supported brand')
		return False

	return True

def parse_text_file(textFile):
	# I can make this the multithreaded part
	f = open(textFile, 'r')
	for item in f:
		if check_text_file_input(item.split(' ')):
			print('Able to parse given input')

def main():
	if len(sys.argv) != 2:
		print('[ERROR]: expecting textfile')
		print('usage: python3 priceCheck.py [\'example.txt\']')
		quit()

	textFile = sys.argv[1]

	if path.exists(textFile) == False:
		print('[ERROR]: ', textFile, 'does not exist')
		quit()
	elif path.isfile(textFile) == False:
		print('[ERROR]: ', textFile, ' is not a file.')
		quit()
	elif textFile.endswith('.txt') == False:
		print('[ERROR]: ', textFile, ' is not a text file')
		quit()

	parse_text_file(textFile)

if __name__ == "__main__":
	main()