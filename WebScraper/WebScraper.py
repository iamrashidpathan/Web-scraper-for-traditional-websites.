import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')  # sends request to the web page and gets the html.

soup = bs4.BeautifulSoup(res.text, 'lxml')  # makes bs4 object of the text from res
# print(soup)
grab = soup.select('.mw-headline')  # selects all the tags with class = mw-headline and stores in a list.
# print(len(grab))
for i in grab:  # loops through the list with all the tags.
    print(i.text)  # prints the text in tags.

# print(grab)
