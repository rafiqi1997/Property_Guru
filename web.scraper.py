from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
import time
import json
import csv

with open('link.csv', newline='') as f:
    reader = csv.reader(f)
    url = list(reader)
    

def scraper():

    count = 0
     
    details = [1,1,1,1,1,1,1,1,1]

    # Scrap property's name
    name =  browser.find_elements_by_xpath("//div[@class='listing-title text-transform-none']")
    details[0] = name[0].text

    count = count + 1
    
    # Scrap property's type
    _type = browser.find_elements_by_xpath("//div[./div[text()='Type']]")
    if len(_type) > 0 :
        _type = str(_type[0].text)
        details[1] = _type[5:]
    else :
        _type = "N/A"
        details[1] = _type

    count = count + 1
    
    # Scrap property's price
    try : 
         price =  browser.find_element_by_xpath("//span[@class='element-label price']")    
         details[2] = "RM " + price.text
    except :
         details[2] = "Unsupported format" 
    count = count + 1
    
    # Scrap property's address
    address = browser.find_element_by_xpath("//span[@itemprop='streetAddress']")
    details[3] = address.text

    count = count + 1
    

    # Scrap price per sqft
    price_per_sqft = browser.find_elements_by_xpath("//div[./div[text()='PSF']]")
    if len(price_per_sqft) > 0 :
        price_per_sqft = str(price_per_sqft[0].text)
        details[4] = price_per_sqft[4:]
    else :
        price_per_sqft = "N/A"
        details[4] = price_per_sqft
        
    count = count + 1    

    # Scrap type of tenure
    tenure = browser.find_elements_by_xpath("//div[./div[text()='Tenure']]")
    if len(tenure) > 0 :
        tenure = str(tenure[0].text)
        details[5] = tenure[7:]
    else :
        tenure = "N/A"
        details[5] = tenure

    count = count + 1
    

    # Scrap furnishing status
    furnishing = browser.find_elements_by_xpath("//div[./div[text()='Furnishing']]")
    if len(furnishing) > 0 :
        furnishing = str(furnishing[0].text)
        details[6] = furnishing[11:]
    else :
        furnishing = "N/A"
        details[6] = furnishing
        
    count = count + 1

    # Scrap developer
    developer = browser.find_elements_by_xpath("//div[./div[text()='Developer']]")
    if len(developer) > 0 :
        developer = str(developer[0].text)
        details[7] = developer[10:]
    else :
        developer = "N/A"
        details[7] = developer

    count = count + 1

    details[8] = link
    
    return details


# property dict
_property = {

  "Name" : None,
  "Type" : None,
  "Price" : None,
  "Address" : None,
  "Price Per Square Feet" : None,
  "Tenure Status" : None,
  "Furnishing" : None,
  "Developer" : None,
  "Link" : None  
}

for i in range(len(url)) :

     options = Options()
     useragent = UserAgent()
     profile = webdriver.FirefoxProfile()
     PROXY_HOST = "12.12.12.123"
     PROXY_PORT = "1234"
     profile.set_preference("network.proxy.type", 1)
     profile.set_preference("network.proxy.http", PROXY_HOST)
     profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
     profile.set_preference("dom.webdriver.enabled", False)
     profile.set_preference('useAutomationExtension', False)
     profile.update_preferences()
     profile.set_preference("general.useragent.override", useragent.random)
     desired = webdriver.DesiredCapabilities.FIREFOX
     driver = "geckodriver.exe" # geckodriver full path
     browser = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired, executable_path = driver)
     link = url[i][0]
     if i == 0 :
          delay = 60
     else :
          delay = 20
     browser.get(link)
     time.sleep(delay)
     
     details = scraper()

     counter = 0

     for i in _property :
         _property[i] = details[counter]
         counter = counter + 1

     data = {}
     data['Property'] = []
     data['Property'].append(_property)

     print(_property)

     print(data)

     del counter


     with open("data.json") as file:

         data = json.load(file)
         temp = data['Property']
         temp.append(_property)

    
     with open('data.json', 'w') as outfile:
         json.dump(data, outfile, indent = 4)

    
     del details

     browser.quit()
    

