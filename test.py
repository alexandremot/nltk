from bs4 import BeautifulSoup
from lxml import etree
import pickle
import re


def write_to_file(what_to_print):
    with open('words.txt', 'w',  encoding="utf-8") as txt_file:
        for line in what_to_print:
        	txt_file.write("%s\n" % line)


def get_id_incidente(soup):
    anchors_list = soup.find_all("a", {"class": "linked formlink"})
    for item in anchors_list:
        print(item.text)
    
    

if __name__ == "__main__":
	with open("results.html", encoding="utf8") as f:
		soup = BeautifulSoup(f.read(), features="html.parser")

	result = soup.find_all("td", {"class": "vt"})
	
	titles_list = []

	for item in result:
		if 'data-original-title' in (item.attrs):
			titles_list.append(str(item.attrs['data-original-title']))

	write_to_file(titles_list)