import json
from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
from bs4 import  BeautifulSoup
import pandas as pd

data=webdriver.Chrome() #"/usr/lib/chromium-browser/chromedriver"

# sudo find / -type f -name chromedriver  ---- this will find the path of your chrome driver
questions={}#dic to store questions
answer={}#dic to store answers
# web=input("enter website FAQ page url: ")
data.get('https://larknorthgate.com/faqs/')#website url
# data.get(web)

content = data.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('div',class_='collapse-items'):
    # questions=a.find('div',attrs={'class':'title'})
    questons=a.find('h2', class_='title')
    answer=a.find('p',class_='content')
# questions=data.find_element_by_xpath('//span[@class="auto-link"][1]')
    # questions.append(questions.txt)
    print(questions.text)
    # answer.append(answer.txt)
    print(answer.text)

# df= pd.DataFrame({'Questions':questions,'Answer':answer})
# df.to_csv('products.csv', index=False, encoding='utf-8')
# df.to_json('FAQ.json')

print(json.dump())
