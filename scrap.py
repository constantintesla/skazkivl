# -*- coding: utf-8 -*-
from typing import Optional, List, Any
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("C:/bin/chromedriver.exe", options=chrome_options)

url = "https://www.newsvl.ru/"
print(url)
driver.get(url)
driver.implicitly_wait(3)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
elems = driver.find_elements_by_class_name("story-list__comments-link")
print (elems)
links: List[Optional[Any]] = [elem.get_attribute('href') for elem in elems]
#print(links)
mlinks = np.array(links)
print (links)
# commenttxt = ''

list_of_comments = []

for x in mlinks:
    url = x
    # global dbname
    # dbname = url.replace('https://www.newsvl.ru/', '').replace('/', '-')
    #print('Название базы = ' + dbname)
    driver.get(url)
    driver.implicitly_wait(3)
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    ctext1 = driver.find_elements_by_class_name("comment-text")
    for i in ctext1:
        if i.text != '':
            list_of_comments.append(i.text)
            # commenttxt += i.text + '\n'  # or whatever the way you want to concatenate your text
            # with open(dbname, "w", encoding="utf-8") as text_file:
            #     text_file.write(commenttxt)
            #     text_file.close()


res = '\n'.join(list_of_comments)
with open('coms.txt', 'w', encoding="utf-8") as file:
    file.write(res)
    file.close()

driver.close()
