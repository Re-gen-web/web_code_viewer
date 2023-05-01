import requests import time
webpage = input("what is the webpage link? (include http://) ")
x = requests.get(webpage, verify=False)
print(x.text) #will return the HTML of the website
time.sleep(999999999999999)
