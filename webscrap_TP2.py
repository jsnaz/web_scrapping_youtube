from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

URL = "https://www.youtube.com/channel/UCasdPe6dgBm7V22njfHPtSQ/videos"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

buttons = driver.find_elements_by_tag_name('button')
accept_all_button = None
for button in buttons:
    if button.text == "ACCEPT ALL":
        accept_all_button = button
accept_all_button.click()

subs_count = driver.find_element_by_id("subscriber-count").text.split(" ")[0]
channel_title = driver.find_element_by_class_name("ytd-channel-name").text
videos = driver.find_elements_by_id("video-title")

print(subs_count)
print(channel_title)
print(str(len(videos)) + " videos")





