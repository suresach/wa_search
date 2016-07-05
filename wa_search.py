from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
browser.get('http://web.whatsapp.com')
input()
reciever = browser.find_element_by_xpath('//span[contains(text(),"Aditi")]')
reciever.click()
reciever_input = browser.find_elements_by_class_name('msg')
#print(reciever_input.text)
#print(reciever_input[0])
le = len(reciever_input)
le = le - 1
query = reciever_input[le].text
final_query = [s for s in query if s.isalpha()]
print(final_query)
final_query = ''.join(final_query)
print("https://www.google.com/search?q=" + final_query)
url = "https://www.google.com/search?q=" + final_query
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
code_box = urlopen(req).read()
#code_box = urlopen("https://www.google.com/search?q=" + final_query).read()
soup = BeautifulSoup(code_box, 'html.parser')
top_results = soup.find_all("span", { "class" : "st" }, limit=3)
reciever.click()
reciever_input = browser.find_elements_by_class_name('input')
reciever_input[1].send_keys("Showing top 3 results for : ")
reciever_input[1].send_keys(final_query)
reciever_input[1].send_keys(Keys.SHIFT, Keys.RETURN)
for results in top_results:
	results = results.get_text()
	reciever_input[1].send_keys(results)
	reciever_input[1].send_keys(Keys.SHIFT, Keys.RETURN)
reciever_input[1].send_keys("© Sachin :D ")    
browser.find_element_by_class_name('send-container').click()