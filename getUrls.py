import requests
import json
from bs4 import BeautifulSoup

def saveToFile(text):
	with open('urls.txt' , 'a') as file:
		file.write(text)

def readFile(filename):
    urls = []
    urlfile = open(filename, "r")
    for x in urlfile:
        u = x.replace("\n", "").lower()
        if not u in urls:
            urls.append(u)
    urlfile.close()
    return urls

def fetchBrand():
    URL = "https://www.prestigemills.com/products-collection.html"

    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.select(".product-feature .product-link")
    if len(links) > 0 :
        text = ""
        for link in links:
            text += link['href'] + "\n"
        saveToFile(text)

# def checkUpdateProduct(file1, file2):
#     list1 = readFile(file1)
#     list2 = readFile(file2)
#     added = []
#     deleted = []
#     for x in list2:
#         if not x in list1:
#             added.append(x)
#     for x in list1:
#         if not x in list2:
#             deleted.append(x)
#     print(added)
#     print("*"*20)
#     print(deleted)

# checkUpdateProduct('urls.txt', 'urls-1.txt')
fetchBrand()
