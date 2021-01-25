                                        WEB SCRAPER
----------------------------------------------------------------------------------------------------------
USE THE COMMAND BELOW IN THE TERMINAL:
  python main.py --page_num_max 5 --dbname products.db

WHERE,
5 - NUMBER OF PAGES TO BER PARSED
products.db - NAME OF DATABASE IN EHICH THE SCRAPED DAT IS TO BE ENTERED

UNCOMMENT THE LINE NUMBER 65 IN 'main.py' TO SEE THE SCRAPED DATA IN A '.csv' FILE.


# Libraries used
1. requests -- responsible for getting web page conent
    To install use - 'pip install requests'
2. BeautifulSoup -- parsing the html code  
    To install use - 'pip install beautifulsoup4'
3. pandas -- to store in data in csv
    To install use - 'pip install pandas'
4. argparse -- Argument parse 
    To install use - 'pip install argparse'
5. sqlite3 -- FOR SQL QUERIES
    To install use -- 'pip install db-sqlite3'


# Methods or functions
1. find_all -- finding all the listing elements
2. find -- finding one element only
3. .text -- to get the text only(without html)
4. .split(',') -- spliting the string by comma(,) and converting to a list
5. .to_csv() -- converting the pandas dataframes to csv file
6. .add_argument() -- used to add argument in command line
--SQL--
7. .connect() --  to connect with database or create file, if not exist and make connection
8. .execute() -- to execute the sql commands 
9. .commit() -- to commit the changes
10. .close() -- to close the connection

 

