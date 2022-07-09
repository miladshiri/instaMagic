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
username = "mokaleme_asan"
password = "ldghn74474"
COUNT_LIMIT = 100
use_following_list = True
SLEEP_TIME_MIN = 120
POST_TIME_THRESHOLD_MIN = 130

page_list_1 = ["english_code", "english_with_bardia","english.bio", "parisa_sjdi", "englishramin", "english_kamran", "englishhints"]
page_list_2 = ["bbcpersian", "dw_persian", "radiochehrazi", "doniamadaniii", "donya", "alidaei", "aliiiiiiiikarimi8", "tataloo", "ehsanalikhani", "n.moein", "ghomayshi", "bahare", "b.rahnama", "khaby00", "emelijad", "mehraadjam", "farzadfarzin1", "serna_amini", "sadaf_beauty", "golfarahani", "alirezatalischioriginal", "ovin_org", "tohi", "tannaz_farahanii", "rambodjavan1", "behdad_hamed", "navidmohammadzadeh", "sima_sufi", "monas_ideas", "bahramafshariofficial", "sardar_azmoun", "amir_food_review", "loghme_", "chef_babak1", "donyanini", "mr.taster", "ebi", "bank.lebas"]

comments_part1 = [
    "به نظر من برای یادگرفتن مکالمه انگلیسی باید کل مکالمه رو تمرین کنید.",
    "با تجربه من یادگرفتن لغات به تنهای کارسازی نیست، باید در جمله باشه.",
    "برای یادگرفتن مکالمه انگلیسی حفظ لغت کاربردی نداره باید مکالمه کامل رو تمرین کنید.",
    "حفظ لغت و ضرب المثل کمکی به مکالمه نمیکنه، باید جملات رو حفظ کنید.",
    "تنها راه عملی برای یادگرفتن سریع مکالمه، حفظ عبارات برای موقعیت های مختلف هست.",
    "نکته مهم در رابطه با یادگیری مکالمه زبان این هست که بتونی جمله حفظ کنی.",
    "باید برای موقعیت مختلف مکالمه های مختلف رو تمرین کنید تا ملکه ذهنتون بشه.",
    "نصف مکالمه انگلیسی دانش هست، نصف دیگه مکالمه تمرین کردن مکالمه هست.",
    "برای خوب صحبت کردن باید عضلات فک و دهان شما به مرور عادت کنه، حفظ جمله و لغت به تنهایی کاربرد نداره.",
    "هیچ ایرادی نداره در مکالمه تپق بزنید حتی در زبان فارسی هم با خیلی اوقات گیر میکنیم.",
    "هرچقدر که دانش لغت و گرامر دارین می تونید مکالمه رو شروع کنید.",
    "هنر صحبت کردن به انگلیسی در حفظ لغت نیست، در این هست که بتونید با همون چیزهایی که بلد هستین صحبت کنید.",
    "برای مکالمه انگلیسی باید از موضوعات عام و جملات ساده شروع کرد.",
    "با تجربه من لازم نیست جملات پیچیده و ضرب المثل یادگرفت، با جملات ساده میشه مکالمه کرد.",
    "اولین کار در مکالمه اینه که بتونید خودتون رو به سادگی معرفی کنید.",
    "برای مکالمه انگلیسی باید مکالمه های ساده رو تمرین کنید.",
    "برای مکالمه انگلیسی نیاز به کسی ندارید، میتونید از خودتون سوال بپرسین و خودتون هم جواب بدین.",
    "با تجربه من وقتی خارج میای مهمترین نکته اینه بتونی جملات ساده رو در مکالمه به کارببری، نه اینکه ضرب المثل بگی."
]

comments_part2 = [
    "برای نکات بیشتر به پیج من هم سر بزنید.",
    "برای یادگرفتن مکالمه های مختلف به پیج من هم سر بزنید.",
    "برای یادگرفتن عبارات کاربردی مختلف پیج من رو هم فالو کنید.",
    "من در پیجم از تجربیاتم در یادگیری انگلیسی بعد از مهاجرت میگم. لطفا فالو کنید.",
    "در پیچ عبارات رو در غالب مکالمه یادمیدن. به پیج من هم سر بزنید.",
    "با استفاده از ویدیوهای داخل پیجم میتونید مکالمه دو طرف با من داشته باشید.",
    "به صفحه من سربزنید تا در این مورد بیشتر یادبگیرید.",
    "در پیجم هر روز یه مکالمه ساده و کاربردی میزارم. فالو کنید." 
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


