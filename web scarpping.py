import requests
import pandas
from bs4 import BeautifulSoup
respond=requests.get("https://www.bikewale.com/yamaha-bikes/")
#print(respond)
soup= BeautifulSoup(respond.content,"html.parser")
#print(soup)
name=soup.find_all('a', class_="modelurl" )
names=[]
for i in  name[0:11]:
  d=i.get_text()
  names.append(d)
#print(len(names))
cc=soup.find_all('div', class_="text-xt-light-grey font14 margin-bottom15")
ccmodel=[]
for i in  cc[0:11]:
  d=i.get_text()
  ccmodel.append(d)
#print(len(ccmodel))
price=soup.find_all('span', class_="font18")
prices=[]
for i in  price[0:11]:
  d=i.get_text()
  prices.append(d)
#print(len(prices))
image=soup.find_all('img', class_="modelimage")
images=[]
for i in  image[0:11]:
  d=i.get("src")
  images.append(d)
#print(len(images))
rate=soup.find_all('a',  class_="btn btn-grey btn-sm margin-top15 font14 getquotation")
ratings=[]
for i in  rate[0:11]:
  d=i.get( "href")
  ratings.append(d)
#print(len(ratings))

data={'name':names,'cc':ccmodel,'price':prices,'image':images,'rate':ratings}
df=pandas.DataFrame(data)
#print(df)
df.to_csv("yamaha_bikes.csv")



