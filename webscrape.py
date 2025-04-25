### Example script to open a link from a webpage using selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')
browser = webdriver.Chrome(options=options)

## Get webpage and confirm based on the title of the page.
browser.get('https://www.scrapingbee.com/blog/selenium-python/')
if browser.title != 'Web Scraping Tutorial Using Selenium & Python (+ examples) | ScrapingBee':
    raise ValueError('Failed to open example page.')
else: 
    print(browser.title)
    
## Obtain the href link by drilling down to the <a> tag inside of the <span> tag with the matching classes.    
button = browser.find_element(by=By.XPATH, value="//span[@class='hidden md:block']/a").get_attribute('href') 

## Open a new Tab with the link we have just obtained.
browser.execute_script("window.open('" + button +"');")    
print(button)

# Sleep and wait to return to the previous page.
time.sleep(3)    
print(browser.current_url)
browser.quit()
    
    
## Using forms    
#userElem = browser.find_element_by_id('user_name')
#userElem.send_keys('your_real_username_here')

#passwordElem = browser.find_element_by_id('user_pass')
#passwordElem.send_keys('your_real_password_here')
#passwordElem.submit()



