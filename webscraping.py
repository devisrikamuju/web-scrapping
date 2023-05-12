import requests
import pandas
from bs4 import BeautifulSoup    
respond= requests.get("https://www.flipkart.com/search?sid=czl&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG")
#print(respond)
soup= BeautifulSoup (respond.content,'html.parser')
#print(soup)
name= soup.find_all('a', class_="s1Q9rs" )
names=[]
for i in name[0:20]:
    d=i.get_text()
    names.append(d)
#print(names)
price= soup.find_all('div', class_="_30jeq3" )
prices=[]
for i in price[0:20]:
    d=i.get_text()
    prices.append(d)
#print(prices)
rate= soup.find_all('div',class_="_3LWZlK" )
rating=[]
for i in rate[0:20]:
    d=i.get_text()
    rating.append(d)
#print(rating)
offer= soup.find_all('div',class_="_3Ay6Sb" )
off=[]
for i in offer[0:20]:
    d=i.get_text()
    off.append(d)
#print(off)

review= soup.find_all('span', class_="_2_R_DZ" )
rev=[]
for i in review[0:20]:
    d=i.get_text()
    rev.append(d)
#print(rev)

image= soup.find_all('img',  class_="_396cs4")
images=[]
for i in image[0:20]:
    d=i['src']
    images.append(d)
#print(images)

#print(df)
data={'name':names,'price':prices,
      'rate':rating,'offer':off, 'review':rev,'image':images}

df= pandas.DataFrame(data)
#print(df)
df.to_csv("tv-details.csv")

