# Introduction
This project intents to scrap data from the links from https://www.propertyguru.com.my and store the data to MySQL database.


# How to use

(1) Run the init_mysql.py to initialize the database and table in MySQL.

(2) Copy the link of propertis from  https://www.propertyguru.com.my and paste the links in the link.csv file according to csv format shown below


  ![alt text](https://github.com/rafiqi1997/Property_Guru/blob/master/Images/link.PNG)
  

(3) Then run the web.scraper.py file to scrap the data.

(4) Open the data.json file to view the scraped data from the website.


(5) Run the requests_and_post.py and copy the local host link, '127.0.0.1:5000/postjson' into Postman API testing tool.


   ![alt_text](https://github.com/rafiqi1997/Property_Guru/blob/master/Images/postman.PNG)
   

(6) Copy the whole json data from data.sjon and paste it in the Postman apps to send the data to MySQL database


   ![alt_text](https://github.com/rafiqi1997/Property_Guru/blob/master/Images/data.PNG)
   

(7) To view the data from MySQL in browser, visit the landing page at localhost url, https //127.0.0.1:500/ on web browser.
