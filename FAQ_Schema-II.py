from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver=webdriver.Chrome()

faqs=[]
quest={}

driver.get('https://larknorthgate.com/faqs/')

# website=input("Enter Your Website: ")
# if website != 0:
#     driver.get(website)
# else:
#     print("sorry please again later")
#     exit()

content=driver.page_source
soup=BeautifulSoup(content)

for faq in soup.find_all('div',class_='collapse-items'):
    question=faq.find('h2', class_='title')
    answer=faq.find('p',class_='content')
    question.append(question.text)
    print(question.text)
    answer.append(answer.text)
    print(answer.text)


print(json.dumps(faqs))
with open ("schema.json","w") as f :
    f.write(json.dumps(faqs))