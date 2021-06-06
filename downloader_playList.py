import time
from selenium import webdriver

playlist = input('url of playlist : ')
web = webdriver.Chrome("chromedriver.exe")
web.get(playlist)
numberOFvideos = web.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]/span[1]').text
print(numberOFvideos)

one = web.find_elements_by_xpath('//*[@id="video-title"]')

web2 = webdriver.Chrome("chromedriver.exe")

for i in range(len(one)):
    try:
        web2.get('https://ar.savefrom.net/' + str(one[i].get_attribute('href')).split('&list')[0])
        time.sleep(2)
        web2.find_element_by_xpath('//*[@id="sf_submit"]').click()
        time.sleep(7)
        web2.find_element_by_xpath('//*[@id="sf_result"]/div/div/div[2]/div[2]/div[1]').click()
        time.sleep(1)
        print(i)
    except:
        print(str(one[i].get_attribute('href')).split('&list')[0])
