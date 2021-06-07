import time
from selenium import webdriver

playlist = input('url of playlist : ')
playListTap = webdriver.Chrome("chromedriver.exe")
playListTap.get(playlist)
numberOFvideos = playListTap.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]/span[1]').text
print(numberOFvideos)



downloadTap = webdriver.Chrome("chromedriver.exe")

listVideos=[]
errorListVideos=[]

for video in playListTap.find_elements_by_xpath('//*[@id="video-title"]'):
    listVideos.append(video.get_attribute('href').split('&list')[0])

playListTap.quit()
for i in range(len(listVideos)):
    try:
        downloadTap.get('https://ar.savefrom.net/' + listVideos[i])
        time.sleep(2)

        downloadTap.find_element_by_xpath('//*[@id="sf_submit"]').click()
        time.sleep(7)
        # click on download button
        downloadTap.find_element_by_xpath('//*[@id="sf_result"]/div/div/div[2]/div[2]/div[1]').click()
        time.sleep(1)

        # error
        print(str(i+1)+" done")
    except:
        print(listVideos[i])
        errorListVideos.append(listVideos[i])
        print(i+1)

time.sleep(300)
for i in range(len(errorListVideos)):
    try:
        downloadTap.get('https://ar.savefrom.net/' + errorListVideos[i])
        time.sleep(2)

        downloadTap.find_element_by_xpath('//*[@id="sf_submit"]').click()
        time.sleep(7)
        # click on download button
        downloadTap.find_element_by_xpath('//*[@id="sf_result"]/div/div/div[2]/div[2]/div[1]').click()
        time.sleep(1)

        # error
        print(str(i+1)+" done")
    except:
        print(errorListVideos[i])
        print(i+1)
