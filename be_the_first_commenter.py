from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pickle
import random
from selenium.webdriver.common.by import By
from datetime import datetime

random.seed(datetime.now())
###############
username = "mokaleme_asan"
password = "ldghn74474"
COUNT_LIMIT = 100

pages = [
        "bbcpersian",
        "dw_persian",
        "radiochehrazi",
        "doniamadaniii",
        "donya",
        "alidaei",
        "aliiiiiiiikarimi8",
        "tataloo",
        "ehsanalikhani",
        "n.moein",
        "ghomayshi",
        "bahare",
        "b.rahnama",
        "khaby00",
        "emelijad",
        "mehraadjam",
        "farzadfarzin1",
        "serna_amini",
        "sadaf_beauty",
        "golfarahani",
        "alirezatalischioriginal",
        "ovin_org",
        "tohi",
        "tannaz_farahanii",
        "rambodjavan1",
        "behdad_hamed",
        "navidmohammadzadeh",
        "sima_sufi",
        "monas_ideas",
        "bahramafshariofficial",
        "sardar_azmoun",
        "amir_food_review",
        "loghme_",
        "chef_babak1",
        "donyanini",
        "mr.taster",
        "ebi",
        "bank.lebas"
        ]
comments_part1 = [
    " در پیج من هم می تونید مکالمه رو روان یادبگیرین",
    " از تجربیاتم از یادگیری زبان بعد از مهاجرت میگم",
    "چقد خوب، با هم مکالمه تمرین کنیم؟",
    " دنبال یادگیری مکالمه کاربردی هستی؟",
    "مکالمه انگلیسی کار کنیم باهم؟",
    "مکالمه دو طرفه از راه دور",
    "عبارات کاربردی برای مکالمه انگلیسی در پیجم"
]

comments_part2 = [
    "مکالمه انگلیسی راحته.",
    "ترفند یادگیری مکالمه حفظ جملات هست.",
    "حفظ لغات کاربردی نداره.",
    "مکالمه آسانه فقط قلق داره.",
    "حتی اگر گرامر نمیدونی مکالمه رو شروع کن.",
    "باید از ساده تر عبارات شروع کنید.",
    "به جای جمله سازی باید جملات را حفظ کنید.",
    "حفظ لغات تنها کاربردی نداره.",
    "باید بتونید با کلماتی که بلدین مکالمه کنید."
]

extras = [
    "عالی،",
    "ایول، ",
    "چقد خوب.",
    "ایوووول",
    "احسنتتتت."
]

#####################################
options = Options()
options.binary_location = r'C:\Users\Milad\AppData\Local\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'F:\workspace\instapy\geckodriver.exe', options=options)
driver.implicitly_wait(5)

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

    
END_FLAG = False
while(len(pages) > 0):
    if END_FLAG:
        break
    sleep(15)
    page = pages.pop(random.randint(0,len(pages)-1))
    driver.get('https://www.instagram.com/{}/'.format(page))

    sleep(1)
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a")
    except:
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a")                                
    
    last_post = elem.get_attribute('href')
        
    driver.get(last_post)

    post_min = 100
    post_hour = 100
    post_day = 100

    post_time_string = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[2]/a/time").get_attribute('innerText')
    if "DAYS AGO" in post_time_string:
        post_day = int(post_time_string.replace(" DAYS AGO", ""))
    elif "HOURS AGO" in post_time_string:
        post_hour = int(post_time_string.replace(" HOURS AGO", ""))
        post_day = 0
    elif "MINUTES AGO" in post_time_string:
        post_min = int(post_time_string.replace(" MINUTES AGO", ""))
        post_hour = 0
        post_day = 0
    
    if post_min < 10:
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
            continue


