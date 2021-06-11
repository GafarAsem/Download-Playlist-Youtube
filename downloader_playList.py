import time
from selenium import webdriver

playlist = input('url of playlist : ')
playListTap = webdriver.Chrome("chromedriver.exe")
playListTap.get(playlist)
numberOFvideos = playListTap.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]/span[1]').text
print(numberOFvideos)

downloadTap = webdriver.Chrome("chromedriver.exe")

listVideos = []
errorListVideos = []

for video in playListTap.find_elements_by_xpath('//*[@id="video-title"]'):
    listVideos.append(video.get_attribute('href').split('&list')[0])

def downloadVideo(url):
    downloadTap.get('https://ar.savefrom.net/' + url)
    time.sleep(1)

    downloadTap.find_element_by_xpath('//*[@id="sf_submit"]').click()
    time.sleep(5)
    # click on download button
    downloadTap.find_element_by_xpath('//*[@id="sf_result"]/div/div/div[2]/div[2]/div[1]').click()
    time.sleep(2)

playListTap.quit()
for i in range(len(listVideos)):
    while True:
        try:
            downloadVideo(listVideos[i])
            if i%10:
                time.sleep(30)
            print(str(i + 1) + " done")
            break
        except:
            print(listVideos[i])
            errorListVideos.append(listVideos[i])
            print(i + 1)

