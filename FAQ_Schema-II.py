from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json

driver=webdriver.Chrome()

faqs=[]
# quest={}
# ans={}
web=input("Enter the url: ")
# https://larknorthgate.com/faqs/
try:
    driver.get(web)
except:
    print("Please Make sure you are connected to internet")
    
content=driver.page_source
soup=BeautifulSoup(content,'html.parser')

def schema():
    for faq in soup.find_all('div',class_='collapse-items'):
        quest=faq.find('h2', class_='title')
        ans=faq.find('p',class_='content')
        faq_dic={
            'question': quest.text,
            'answer':ans.text
        }
        faqs.append(faq_dic)
        # quest.append(quest.text)
        # print(quest.text)
        # ans.append(ans.text)
        # print(ans.text)

        with open ("schema.json","w") as f :
            f.write(json.dumps(faqs))

    print(json.dumps(faqs))
