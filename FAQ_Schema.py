from selenium import webdriver
from bs4 import BeautifulSoup
import json
# import os


web = input("Enter Your Url: ")
div=input("select the type of tag parent: \n Eg:- div : ")
paren_class=input("enter class in which Q & A there: ")
div2=input('Enter question tag: ')
quest_class=input("enter question class: ")
div3=input('Enter answer tag: ')
answer_class=input("enter answer class:")

driver = webdriver.Chrome()
faqs=[]


def schema():
    for faq in soup.find_all(div,class_=paren_class):
        quest=faq.find(div2,class_=quest_class)
        ans=faq.find(div3,class_=answer_class)
        faq_dic={
        #    <script type="application/ld+json"> 
        #    {
            # "@context": "https://schema.org",
            # "@type": "FAQPage",
            # "mainEntity": {
                "@type": "Question",
                "name": quest.text,
                "acceptedAnswer": 
                {"@type": "Answer",
                 "text": ans.text
                }
                # }
                # }
                # </script>
                }
        faqs.append(faq_dic)
        print(quest.text)
        with open("schema.json","w") as f:
            f.write(json.dumps(faqs))
print(json.dumps(faqs))

if web == False:
    print("Pllease try again later...\n value can't be null")
    quit()
else:
    driver.get(web)
    content=driver.page_source
    soup=BeautifulSoup(content,'html.parser')

schema()
