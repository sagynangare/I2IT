import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

#response = requests.get("http://api.open-notify.org/iss-now.json")
#print(response)

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
#print(type(soup))

title = soup.title
print(title)

# Print out the text
text = soup.get_text()
print(soup.text)
