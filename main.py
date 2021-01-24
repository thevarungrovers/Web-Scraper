import requests # responsible for getting web page conent
from bs4 import BeautifulSoup # parsing the html code

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

req = requests.get(url) # get api request

content = req.content # getting the content from url
# print(content)

soup = BeautifulSoup(content, "html.parser") # parsing the html

 # ("tag",{"attribute":"value"}) 
all_products = soup.find_all("div",{"class":"thumbnail"}) # returns a list if all the elements which satsfy the given condition in parenthesis

for product in all_products:
    pro_name = product.find("a",{"class":"title"}).text
    pro_price = product.find("h4",{"class":"price"}).text 
    pro_review = product.find("p",{"class":"pull-right"}).text

    pro_desc = product.find("p",{"class":"description"}).text
    pro_desc_list = pro_desc.split(',') # converting the description into list

    print(pro_name,pro_price,pro_desc_list[:4],pro_review) 
    