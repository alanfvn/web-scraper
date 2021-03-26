import requests
import time
import datetime
import os
import tweepy
from bs4 import BeautifulSoup


def main():
	url = 'https://www.intelaf.com/precios_stock_detallado.aspx?codigo=DDR3-4GB-CR1333'
	f = requests.get(url)
	soup = BeautifulSoup(f.content, "html.parser")
	find_data(soup)


def find_links(soup):
	urls = soup.find_all("a")
	for url in urls:
		print("<a href'%s'>%s</a>"%(url.get("href"), url.text))


def find_data(soup):
	g_data = soup.find_all("div", {"class":"cuerpo_lateral"})
	for item in g_data:
		contenido = item.contents[1].contents

		text = contenido[0].text
		num = contenido[1].text
		warn(text+": "+num)

		if num != "0":
			os.system('cls')
			print("#"*100+"\n"+"#"*100)
			print("DONE")
			send_message("DONE")
			print("#"*100+"\n"+"#"*100)



def send_message(msg):
	auth = tweepy.OAuthHandler("", "")
	auth.set_access_token("", "")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	#api.send_direct_message("id", msg)


def warn(msg):
	print("\n["+f"{datetime.datetime.now():%H:%M:%S %d/%m/%Y}"+"] "+msg)


while True:
	main()
	time.sleep(30)
