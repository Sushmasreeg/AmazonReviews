from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import csv


PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

phonesExcluded=[]

#Reading the URL of the mobiles from the mobile information written into AMAZON_PRODUCT_DETAILS.csv
with open("AMAZON_PRODUCT_DETAILS.csv", "r") as csvfile:
    DetailsReader=csv.reader(csvfile)
    for row in DetailsReader:
        try:
            if(row[1]=="Oppo"):
                driver.get(row[2])
                driver.implicitly_wait(1000)
                print("Hello")
                try:
                    #Getting the link to reviews page of a particular mobile phone
                    reviews = WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-hook='see-all-reviews-link-foot'].a-link-emphasis.a-text-bold")))
                except:
                    continue
                if(len(reviews)>0):
                    reviews_link=""
                    for k in reviews:
                        reviews_link=k.get_attribute("href")
                    driver.get(reviews_link)
                    
                    #Reading the number of reviews and ratings
                    noOfReviews = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#filter-info-section span")))
                    
                    numberReviews=0

                    #Replacing ',' and converting the string format of No.of reviews to integer
                    for j in noOfReviews:
                        s=j.text
                        print(s)
                        ratingsAndReviews=s.split("|")
                        index=ratingsAndReviews[1].index("g")
                        numberReviews=ratingsAndReviews[1][1:index-1]
                        if("," in numberReviews):
                            numberReviews=numberReviews.replace(",","")
                        numberReviews=int(numberReviews)
                    driver.implicitly_wait(1000)
                    countReviews=0
                    while(countReviews<=60 and countReviews<numberReviews):

                        #Reading the reviewer names, ratings, review title and the review description on one page
                        
                        names=WebDriverWait(driver,1000).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#cm_cr-review_list div[data-hook='review'] div.a-profile-content span")))
                        ratings=WebDriverWait(driver,1000).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#cm_cr-review_list .review-rating span.a-icon-alt")))
                        review_title=driver.find_elements_by_css_selector("a[data-hook='review-title'] span")
                        review_desc=WebDriverWait(driver,1000).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.review-data span[data-hook='review-body'] span")))
                        driver.implicitly_wait(1000)
                        
                        for num in range(0,len(review_title)):
                            #Writing these details into the csv file AMAZON_PRODUCT_REVIEWS.csv
                            with open("AMAZON_PRODUCT_REVIEWS.csv", "a+",encoding="utf-8") as reviewfile:
                                writer=csv.writer(reviewfile)
                                try:
                                    writer.writerow([row[0],row[1],row[3],names[num].text,ratings[num].get_attribute("innerHTML"),review_title[num].text,review_desc[num].text])
                                    print(review_title[num].text)
                                except:
                                    continue
                        
                        countReviews+=len(review_title)
                        
                        if(countReviews<=60 and countReviews<numberReviews):
                            driver.implicitly_wait(1000)
                            
                            #Getting the next review page
                            nextReview=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.a-last a")))
                            nextRev=""
                            for i in nextReview:
                                nextRev=i.get_attribute("href")
                            time.sleep(2)
                            driver.get(nextRev)
                        else:
                            continue
            
        except:
            phonesExcluded.append(row[0])
            continue
            
            
                
                
                
                            
                            
                
                        









                    
            
            
