import requests
from bs4 import BeautifulSoup
import jsbeautifier
import time
url = "https://880218394199220334.discordsays.com"
doc = requests.get(url).text # Watch Together

soup = BeautifulSoup(doc, 'html.parser')

def write(contents):
	with open('main.js', 'w') as f:
		f.write(contents)
		f.close()

for script in soup.find_all('script'):
	src = script.get('src')
	if src is not None: 
		print("[Link] " + url + str(src))
	else:
		continue
	
	if "main" not in str(src):
		continue

	scriptSrc = requests.get(url+src).text
	write(jsbeautifier.beautify(scriptSrc))
	print("Done")