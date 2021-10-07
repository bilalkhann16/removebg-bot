from selenium import webdriver
import time
from pathlib import Path
import os
import urllib.request
import urllib.parse

def download_image(removed_background):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0')]
    urllib.request.install_opener(opener)
    filename = removed_background.split("/")[-1]
    urllib.request.urlretrieve(removed_background,filename)
    print ("Image downloaded\n")

def upload(image_naem):
    print ("image_name", image_naem)
    driver = webdriver.Firefox()
    bk = driver.get("https://www.remove.bg/upload")
    file_input = driver.find_element_by_css_selector("button.btn-primary:nth-child(1)").click()
    inc = "//input[@type='file']"
    field = driver.find_element_by_xpath(inc)
    driver.execute_script("arguments[0].style.display = 'block';", field)
    field = driver.find_element_by_xpath(inc)

    abs_path = str(Path().absolute())+"/"
    abs_path = abs_path+image_naem
    abs_path = str(abs_path)
    print(abs_path)
    time.sleep(10)
    field.send_keys(abs_path)
    
    time.sleep(15)
    removed_background = driver.find_element_by_css_selector("a.btn-primary").get_attribute('href')
    print ("url:",removed_background)
    download_image(removed_background)
    driver.quit()

def upload_file():
    f = open("input.txt", "r")
    for i in (f):
        upload(i)
        time.sleep(10)
        

upload_file()