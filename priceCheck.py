import sys
import os.path
from os import path
import urllib.request

def get_http():
	contents = urllib.request.urlopen("https://www.adidas.com/us/ultraboost-4.0-dna-shoes/FY9318.html").read()
	print(contents)

def parse_text_file(textFile):
	print('Textfile: ', textFile)
	f = open(textFile, 'r')
	#for item in f:
		#print(item)
		#items = item.split(' ')
		#print(items[0])
		#print(len(items))


def main():
	if len(sys.argv) != 2:
		print('ERROR: expecting textfile')
		print('usage: python3 priceCheck.py [\'example.txt\']')
		quit()

	textFile = sys.argv[1]

	if path.exists(textFile) == False:
		print('ERROR: ', textFile, 'does not exist')
		quit()
	elif path.isfile(textFile) == False:
		print('ERROR: ', textFile, ' is not a file.')
		quit()
	elif textFile.endswith('.txt') == False:
		print('ERROR: ', textFile, ' is not a text file')
		quit()

	#parse_text_file(textFile)
	#get_http()

if __name__ == "__main__":
	main()