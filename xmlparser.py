from bs4 import BeautifulSoup
infile = open("books.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
titles = soup.find_all('title')

# 1 getting all the titles
print('\n')
print(''.join(['-']*30))
print('[INFO] getting all the titles from the xml doc')
for title in titles:
    print(title.get_text())
print(''.join(['-']*30))
print('\n')

# 2 title by author with price
print(''.join(['-']*30))
print('[INFO] getting all the titles by author with price from the xml doc')
titles = soup.find_all('title')
authors = soup.find_all('author')
prices = soup.find_all('price')
for i in range(0, len(titles)):
    print(titles[i].get_text(),"by",end=' ')
    print(authors[i].get_text(),end=' ')
    print("costs $" + prices[i].get_text())
print(''.join(['-']*30))
print('\n')