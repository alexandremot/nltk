if __name__ == "__main__":
	with open("results.html", encoding="utf8") as f:
		soup = BeautifulSoup(f.read(), features="html.parser")
	first_column = soup.select('table tr td:nth-of-type(2)')
	print(first_column)
