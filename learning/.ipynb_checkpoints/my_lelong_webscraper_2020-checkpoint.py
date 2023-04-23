
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.lelong.com.my/'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,'html.parser')

filename = 'lelongproducts_2020.csv'
f = open(filename, 'w')
headers = 'brand, price\n'
f.write(headers)

brandcontainers = page_soup.findAll("a",{'class':'ga-pclick'})

for i in range(0, len(brandcontainers)):
    brand = brandcontainers[i]['title']
    price = brandcontainers[i]['data-price']
    f.write(brand.replace(",","|")+","+price.replace(",","|")+"\n")

f.close