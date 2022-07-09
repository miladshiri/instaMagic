from time import sleep
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pickle
import random
import time 
import datetime

random.seed(time.time())
###############
username = "nexttrendingtech"
password = "1236951000Hp"
COUNT_LIMIT = 100
use_following_list = True
SLEEP_TIME_MIN = 120
POST_TIME_THRESHOLD_MIN = 1*24*60+10

page_list_1 = []
page_list_2 = []

comments_part1 = [
    "انواع آموزش رایگان شامل مباحث ماشین لرنینگ، بلاکچین، ساخت فیلتر اینستاگرام و ... در پیج ما",
    "آموزش های ویدیویی رایگان ماشین لرنینگ و بلاکچین",
    "آموزش ساخت فیلتر اینستاگرام به صورت رایگان در صفحه ما",
    "یادگیری آسان تکنولوژی های مرز دانش در صفحه ما",
    "آموزش های ویدیویی رایگان برنامه نویسی و ماشین لرنینگ با پایتون",
    "هوش مصنوعی و بلاکچین در صفحه ما به صورت کامل و رایگان آموزش داده می شود",
    "آموزش رایگان پیش بینی بورس با ماشین لرنینگ و هوش مصنوعی در صفحه ما گذاشته شده است",
    "ویدیوهای رایگان و پروژه های رایگان هوش مصنوعی و بلاکچین در صفحه ما قرار داده شده است",
    "پروژه های کلاسبندی و کلاسترینگ با هوش مصنوعی در پیج ما",
    "دوره های رایگان ماشین لرنینگ و پردازش تصویر در صفحه ما قرار داده شده است"

]

comments_part2 = [
    "اگر به تکنولوژی های مرز دانش علاقه دارید صفحه ما را هم دنبال کنید",
    "اگر به این مباحث علاقه دارید صفحه ما را دنبال کنید",
    "اگر علاقه مند به مشاهده ویدیوهای رایگان در حوزه هوش منصوعی هستید ما را دنبال کنید",
    "صفحه ما را برای دریافت ویدیوها و دوره های رایگان فالو کنید"

]

extras = [
    "مرسی از ادمین.",
    "جالب بود.",
    "عالی بود، مرسی.",
    "خوب بود مرسی."
    ]

pages = page_list_2

#####################################
# options = Options()
# options.binary_location = r'C:\Users\Milad\AppData\Local\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r'F:\workspace\instapy\geckodriver.exe', options=options)
# driver.implicitly_wait(5)

ser = Service("C:\\webdriver\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

print('##### Started ##########################################################################')
driver.get('https://www.instagram.com/')
try:
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://www.instagram.com/')
except:

    login_link = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
    login_link.click()

    sleep(5)

    elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    elem.send_keys(username)

    elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    elem.send_keys(password)

    driver.implicitly_wait(5)
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    elem.click()

    driver.implicitly_wait(5)
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
    elem.click()

    driver.implicitly_wait(15)
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]")
    except:
        elem = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")

    elem.click()
                                         
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

comment_count = 0

###### Get the followings ########################
if (use_following_list):
    driver.get('https://www.instagram.com/{}/'.format(username))
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
    elem.click()
    sleep(2)
    # /html/body/div[6]/div/div/div[3]
    fBody  = driver.find_element(By.XPATH, "//div[@class='isgrP']")
    scroll = 0
    while scroll < 25: # scroll 5 times
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        sleep(1)
        scroll += 1

    fList  = driver.find_elements(By.XPATH,"//div[@class='isgrP']//li")
    # print("fList len is {}".format(len(fList)))
    following_pages = []
    for i in range(0, len(fList)):
        elem = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div[3]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a".format(i+1))
        following_pages.append(elem.get_attribute('href'))
    pages = following_pages

END_FLAG = False
while(not END_FLAG):
    total_post_reviewd = 0
    while(len(pages) > 0):
        if END_FLAG:
            break
        
        sleep(15)
        page = pages.pop(random.randint(0,len(pages)-1))
        print("##### Investigating {} #############################".format(page))
        if (use_following_list):
            driver.get(page)
        else:
            driver.get('https://www.instagram.com/{}/'.format(page))

        sleep(1)
        try:
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a")
        except:
            elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a")                                
        
        last_post = elem.get_attribute('href')
            
        driver.get(last_post)

        post_min = 1000000000
        post_hour = 100
        post_day = 100

        post_time_string = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[2]/a/time").get_attribute('innerText')
        if "DAYS AGO" in post_time_string or "DAY AGO" in post_time_string:
            post_day = int(post_time_string.replace(" DAYS AGO", "").replace("DAY AGO", ""))
            post_min = post_day * 24 * 60
        elif "HOURS AGO" in post_time_string or "HOUR AGO" in post_time_string:
            post_hour = int(post_time_string.replace(" HOURS AGO", "").replace(" HOUR AGO", ""))
            post_day = 0
            post_min = 60 * post_hour
        elif "MINUTES AGO" in post_time_string or "MINUTE AGO" in post_time_string:
            post_min = int(post_time_string.replace(" MINUTES AGO", "").replace(" MINUTE AGO", ""))
            post_hour = 0
            post_day = 0

        total_post_reviewd += 1
        print("### Last post created {} minutes ago.".format(post_min))
        if post_min < POST_TIME_THRESHOLD_MIN:
            try:
                print('a')
                sleep(random.randint(25, 35))

                sleep(5)
                elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[1]")
                elem.click()
                sleep(1)
                elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea")
                elem.send_keys(extras[random.randint(0, len(extras)-1)] + '  ' + comments_part1[random.randint(0, len(comments_part1)-1)] + '  ' + comments_part2[random.randint(0, len(comments_part2)-1)])

                print('b')
                sleep(5)
                elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]")
                elem.click()

                comment_count += 1
                print("Comments count: {}".format(comment_count))
                print(page)
                print('###########################################')
                
                if comment_count > COUNT_LIMIT:
                    END_FLAG = True
            except Exception as e: 
                print(e)
                pass
            

            numbers = list(range(1,5))
            for i in range(1,3):
                if END_FLAG:
                    break
                try:
                    print(i)
                    print('a')
                    sleep(random.randint(25, 35))
                    try:
                        elem = driver. find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/ul[{}]/div/li/div/div/div[2]/div/div/button[2]".format(numbers.pop(random.randint(0,len(numbers)-1))))
                    except:
                        elem = driver. find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/ul[{}]/div/li/div/div/div[2]/div/div/button".format(numbers.pop(random.randint(0,len(numbers)-1))))  
                    elem.click()
                    print('b')
                    sleep(5)
                    elem = driver. find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea")
                    elem.send_keys(extras[random.randint(0, len(extras)-1)] + '  ' + comments_part1[random.randint(0, len(comments_part1)-1)] + '  ' + comments_part2[random.randint(0, len(comments_part2)-1)])

                    print('c')
                    sleep(5)
                    elem = driver. find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]")
                    elem.click()

                    comment_count += 1
                    print("Comments count: {}".format(comment_count))
                    if comment_count > COUNT_LIMIT:
                        END_FLAG = True
                except Exception as e: 
                    print(e)
                    continue
    print("#Total post reviewd: {}".format(total_post_reviewd))
    print("#Waiting for the next round ...")
    print(datetime.datetime.now())
    sleep(60*SLEEP_TIME_MIN)            


