#import the necessary libraries

from bs4 import BeautifulSoup
import requests
import csv

def main(URL):
    #creating an excel file to store all the product details
    File = open("details.csv","a")

    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

    webpage = requests.get(URL,headers=HEADERS)

    #reading the content
    soup1 = BeautifulSoup(webpage.content,"lxml")
    #making the data better formatted
    soup2 = BeautifulSoup(soup1.prettify(),"lxml")

    #obtaining the title of the product 
    try:
        title = soup2.find("span", attrs={"id":"productTitle"})
        #converting the find func's output into a string 
        title_value = title.string 
        #formatting for easier storing
        title_string = title_value.strip().replace(",", "")

    except AttributeError:
        title_string = "NA"

        print("Product Title : ",title_string)

    File.write(f"{title_string},")


    #obtaining the product price
    try:
        price = soup2.find("span",attrs={"id":"priceblock_ourprice"}).string.strip().replace(",","")

    except AttributeError:
        price = "NA"

        print("Product Price :",price)

    File.write(f"{price},")

    #obtaining the product's rating
    try:
        rating = soup2.find("span",attrs={"id":"a-icon a-icon-star a-star-4-5"}).string.strip().replace(",","")

    except AttributeError:
        rating = "NA"

        print("Overall Rating : ",rating)

    File.write(f"{rating},")


    #obtaining the reviews count of the product
    try:
        review_count = soup2.find("span",attrs={"id":"acrCustomerReviewText"}).string.strip().replace(",","")

    except AttributeError:
        review_count = "NA"

    print("Total Reviews : ",review_count)
    File.write(f"{review_count},")

    #finally, obtaining the avaliablity status

    try:
        availability = soup2.find("div",attrs = {"id" : "availability"}).string.strip().replace(",","")

    except AttributeError:
        availability = "NA"

    print("Availability : ",availability)

    File.write(f"{availability},\n")

    #close the file after adding all required information
    File.close()

if __name__ == '__main__':
    myFile = open("url.txt","r") #opening the file which has all the URLs

#read each url in the input file
for link in myFile.readlines():
    main(link)












