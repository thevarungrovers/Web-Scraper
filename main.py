import requests # responsible for getting web page conent
from bs4 import BeautifulSoup # parsing the html code
import pandas # to store in data in csv

main_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="

page_num_max = 3 # maximum number of pages
scraped_info_list = [] # scraped data


for page_num in range(1,page_num_max):
    url = main_url + str(page_num)
    req = requests.get(url) # get api request

    content = req.content # getting the content from url
    # print(content)

    soup = BeautifulSoup(content, "html.parser") # parsing the html

    # ("tag",{"attribute":"value"}) 
    all_products = soup.find_all("div",{"class":"thumbnail"}) # returns a list if all the elements which satsfy the given condition in parenthesis

    for product in all_products:
        product_dic = {} # empty  dictionary
        product_dic["name"] = product.find("a",{"class":"title"}).text # name
        product_dic["price"] = product.find("h4",{"class":"price"}).text # price
        product_dic["review"] = product.find("p",{"class":"pull-right"}).text # review

        pro_desc = product.find("p",{"class":"description"}).text # description
        
        pro_desc_list = pro_desc.split(',') # converting the description into list

        # product_dic["Description"] = ', '.join(pro_desc_list[:4]) # description
        product_dic["Screen-size"] = ''.join(pro_desc_list[0]) # description - Screen-size
        product_dic["Processor"] = ''.join(pro_desc_list[1]) # description - Processor
        product_dic["RAM"] = ''.join(pro_desc_list[2]) # description - RAM
        product_dic["ROM"] = ''.join(pro_desc_list[3]) # description - ROM

        scraped_info_list.append(product_dic) # list of products' dictionary


        # print(pro_name,pro_price,pro_desc_list[:4],pro_review) 

dataframes = pandas.DataFrame(scraped_info_list) # converting the scraped data to pandas dataframes
dataframes.to_csv('product.csv') # conver dataframe to csv file