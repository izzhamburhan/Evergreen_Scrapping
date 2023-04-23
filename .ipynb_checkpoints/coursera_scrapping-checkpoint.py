
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.udemy.com/?utm_source=adwords&utm_medium=udemyads&utm_campaign=Generic-Exact_la.EN_cc.ROW&utm_content=deal4584&utm_term=_._ag_86841140136_._ad_636511199023_._kw_coursers_._de_c_._dm__._pl__._ti_kwd-337278152550_._li_9066780_._pd__._&matchtype=e&gclid=EAIaIQobChMIst3drOG3_gIVQ2ArCh0CkAYeEAAYAiAAEgJk5_D_BwE'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,'html.parser')

filename = 'coursera.csv'
f = open(filename, 'w')
headers = 'brand,price'
f.write(headers)

brandcontainers = page_soup.findAll("a",{'class':'ga-pclick'})

for i in range(0, len(brandcontainers)):
    brand = brandcontainers[i]['title']
    price = brandcontainers[i]['data-price']
    f.write(brand.replace(",","|")+","+price.replace(",","|")+"\n")

f.close