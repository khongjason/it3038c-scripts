import request
from bs4 import BeautifulSoup

res = requests.get(url="http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book")
soup = BeautifulSoup(res.text,"html.parser") 
book_div = soup.find(attrs={"id":"book"})

book_a= book_div.findAll(attrs={"class":"title"})
book_b = book_div.findAll(attrs={"class":"desc"})

for book in book_a:
	print(book.string)