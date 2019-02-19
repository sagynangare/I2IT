import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
'''
    Sends a GET request.
'''

#print(page)
#print(page.status_code)
#print(page.content)
'''content
Content of the response, in bytes.
'''

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prittify)
'''
The prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string,
with a separate line for each HTML/XML tag and string
'''
#print(list(soup.children))
'''
The BeautifulSoup object itself has children. In this case, the <html> tag is the child of the
BeautifulSoup object.:
len(soup.contents)
# 1
soup.contents[0].name
# u'html'
'''
html = list(soup.children)[2]
#print(list(html.children))

body = list(html.children)[3]
#print(list(body.children))

p = list(body.children)[1]
#print(p.get_text())
'''
If you only want the text part of a document or tag, you can use the get_text() method.
It returns all the text in a document or beneath a tag, as a single Unicode string
'''
#Finding all instances of a tag at once

#print(soup.find_all('p'))
'''
it will find all 'p' tags
'''
#print(soup.find_all('p')[0].get_text())

#Searching for tags by class and id
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup1 = BeautifulSoup(page.content, 'html.parser')
#print(soup1.find_all('p', class_='outer-text'))
#print(soup1.find_all(id="first"))
#print(soup.select("div p"))

#Downloading weather data

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
'''

'''

forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

#print(period)
#print(short_desc)
#print(temp)

img = tonight.find("img")
desc = img['title']

#print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
#print(periods)
'''BeautifulSoup has a .select() method which uses SoupSieve to run a CSS
selector against a parsed document and return all the matching elements.
Tag has a similar method which runs a CSS selector against the contents of a
single tag.
(Earlier versions of Beautiful Soup also have the .select() method, but
only the most commonly-used CSS selectors are supported.)
'''

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print('short_descs ',short_descs)
#print(temps)
#print(descs)

import pandas as pd
weather = pd.DataFrame({
        "period": periods, 
        "short_desc": short_descs, 
        "temp": temps, 
        "desc":descs
    })
print(weather)
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
#print(temp_nums)
#print(weather["temp_num"].mean())

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
#print(is_night)
#print(weather[is_night])







































