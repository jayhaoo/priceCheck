import sys
import os.path
from os import path

def parse_text_file(textFile):
	print('Textfile: ', textFile)
	f = open(textFile, 'r')
	for item in f:
		print(item)
		items = item.split(' ')
		print(items[0])
		print(len(items))

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

	parse_text_file(textFile)


if __name__ == "__main__":
	main()