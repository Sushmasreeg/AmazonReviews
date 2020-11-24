from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import csv

PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

#Opening the Amazon link to get details of different Oppo Mobiles
driver.get("https://www.amazon.in/s?k=oppo+smartphones&i=electronics&rh=n%3A1805560031%2Cp_89%3AOppo&dc&qid=1605587088&rnid=3837712031&ref=sr_nr_p_89_1")

products={}
PRODUCT_REVIEWS=[]
productName=[]



with open("AMAZON_PRODUCT_DETAILS.csv", "a+") as csvfile:
    writer=csv.writer(csvfile)

    brand="Oppo"
    for i in range(1,6):
        #Getting information like ID, URL of the mobile phone, Name, Price and Image link of different mobiles
        product_id=driver.find_elements_by_css_selector("div.s-main-slot div[data-component-type='s-search-result']")
        product_url=driver.find_elements_by_css_selector("div.s-main-slot div[data-component-type='s-search-result'] span.widgetId\=search-results h2 a.a-link-normal")
        product_name=driver.find_elements_by_css_selector("div.s-main-slot div[data-component-type='s-search-result'] span.widgetId\=search-results h2 a.a-link-normal span.a-size-medium")
        product_price=driver.find_elements_by_css_selector("div.s-main-slot div[data-component-type='s-search-result'] span.widgetId\=search-results .a-price-whole")
        product_image=driver.find_elements_by_css_selector("div.s-main-slot div[data-component-type='s-search-result'] span.widgetId\=search-results .s-image-fixed-height .s-image")
    
        minimum=min(len(product_id),len(product_url),len(product_name),len(product_price),len(product_image))
        
        
        for j in range(minimum):
            price=product_price[j].text
            price=float(price.replace(",",""))
            prod=product_name[j].text.split("(")[0]
            if lower(prod) not in productName and prod!="":
                #Writing this information into an csv file called AMAZON_PRODUCT_DETAILS.csv
                
                writer.writerow([product_id[j].get_attribute("data-asin"),brand,product_url[j].get_attribute("href"),prod,price,product_image[j].get_attribute("src")])
                productName.append(lower(prod))
            

        print(productName)
        
        #Getting the next page
        driver.get("https://www.amazon.in/s?k=oppo+smartphones&i=electronics&rh=n%3A1805560031%2Cp_89%3AOppo&dc&page={}&qid=1605587093&rnid=3837712031&ref=sr_pg_{}".format(str(i+1),str(i)))


    
    




