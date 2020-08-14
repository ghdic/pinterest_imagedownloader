# # 방법 1 headless로 창크기를 엄청나게 크게하여 사진 로드함
import urllib.request
import re
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import keyboard  # using module keyboard

def downloadPinterestImages(link):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    #options.headless = True
    #options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    global driver
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    
    driver.set_window_size(1920, 100000)
    print("start")
    driver.get(link)
    print("link start")
    while True: # cpu가 더 이상 일 안하면 0% 되면 q 눌러줌! 이미지 로드 더이상 안하는거임
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed q Key!')
            break  # finishing the loop
    
    images = driver.find_elements_by_css_selector("img")
    print(f"{len(images)}개 사진을 찾았습니다!!")    
    if not os.path.exists("image"):
        os.mkdir("image")
    for img in images:
        image_url = img.get_attribute("srcset").split(",")[-1].strip().split(" ")[0]
        #print(image_url)
        pattern = re.compile("https://i.pinimg.com/.*")
        if pattern.match(image_url):
            urllib.request.urlretrieve(image_url, "image/"+image_url.split("/")[-1])
    driver.close()
    driver.quit()
try:
    downloadPinterestImages("https://www.pinterest.co.kr/krabel019347/masiro/")
    
except:
    driver.close()
    driver.quit()
    


# # 방법2 스크롤 다운
# import urllib.request
# import re
# import time
# import sys
# import os
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By

# def waitSession(val, second):
#     try:
#         element = WebDriverWait(driver, second).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, val))
#         )
#     except TimeoutException:
#         print("타임아웃")
#         raise Exception('타임아웃')

# def scrollDown():
#     SCROLL_PAUSE_TIME = 4
#     res = set()
#     last_height = driver.execute_script("return document.body.scrollHeight")
    
#     while True:
        
#         images = driver.find_elements_by_css_selector("img")
#         urls = get_url(images)
#         res.update(urls)
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(SCROLL_PAUSE_TIME)
        
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height
#     time.sleep(SCROLL_PAUSE_TIME)
#     images = driver.find_elements_by_css_selector("img")
#     urls = get_url(images)
#     res.update(urls)
#     return res

# def get_url(images):
#     urls = []
#     for img in images:
#         image_url = img.get_attribute("srcset")
#         if not image_url:
#             image_url = img.get_attribute("src")
#         if image_url:
#             image_url = image_url.split(",")[-1].strip().split(" ")[0]
#             pattern = re.compile("https://i.pinimg.com/.*")
#             if pattern.match(image_url):
#                 urls.append(image_url)
#     return urls

# def downloadPinterestImages(email, password, link):
#     global driver
#     driver = webdriver.Chrome('chromedriver.exe')
#     driver.maximize_window()
#     driver.get(link)


#     driver.find_element_by_css_selector("#HeaderContent > div > div.Jea.gjz.hs0.zI7.iyn.Hsu > div.wc1.zI7.iyn.Hsu > button").click()
#     waitSession("#email", 10)
#     driver.find_element_by_css_selector("#email").send_keys(email)
#     driver.find_element_by_css_selector("#password").send_keys(password)
#     driver.find_element_by_css_selector("#__PWS_ROOT__ > div.zI7.iyn.Hsu > div > div > div:nth-child(6) > div > div > div > div > div > div:nth-child(3) > form > div:nth-child(5) > button").click()
    
#     time.sleep(5)
#     if not os.path.exists("images"):
#         os.mkdir("images")

#     urls = scrollDown()
#     print(f"{len(urls)}개 사진을 찾았습니다!!")    
#     for image_url in urls:        
#         urllib.request.urlretrieve(image_url, "images/"+image_url.split("/")[-1])
        

#     driver.close()
#     driver.quit()

# downloadPinterestImages("email@email.com", "mypassword", "https://www.pinterest.co.kr/krabel019347/menhera-chan/")
