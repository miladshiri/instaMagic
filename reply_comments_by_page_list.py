from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pickle
import random

###############
username = "mokaleme_asan"
password = "ldghn74474"
COUNT_LIMIT = 100

pages = ["english_code", "english_with_bardia","english.bio", "parisa_sjdi", "englishramin", "english_kamran", "englishhints"]
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

    login_link = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
    login_link.click()

    sleep(5)

    elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    elem.send_keys(username)

    elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    elem.send_keys(password)

    driver.implicitly_wait(5)
    elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    elem.click()

    driver.implicitly_wait(5)
    elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    elem.click()

    driver.implicitly_wait(15)
    try:
        elem = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
    except:
        elem = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")

    elem.click()
                                         
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

comment_count = 0

    
END_FLAG = False
while(len(pages) > 0):
    if END_FLAG:
        break
    sleep(15)
    driver.get('https://www.instagram.com/{}/'.format(pages.pop(random.randint(0,len(pages)-1))))

    post_urls = []

    for post_index in range(0, 3):
        sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[{}]/a".format(post_index+1))
        post_urls.append(elem.get_attribute('href'))


    for post_url in post_urls:
        if END_FLAG:
            break
        
        driver.get(post_url)

        numbers = list(range(1,11))
        for i in range(1,5):
            if END_FLAG:
                break
            try:
                print(i)
                print('a')
                sleep(random.randint(25, 35))
                try:
                    elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/ul[{}]/div/li/div/div/div[2]/div/div/button[2]".format( numbers.pop(random.randint(1,len(numbers)-1))))
                except:
                    elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/ul[{}]/div/li/div/div/div[2]/div/div/button".format( numbers.pop(random.randint(0,len(numbers)-1))))                              
                elem.click()

                print('b')
                sleep(5)
                elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea")
                elem.send_keys(extras[random.randint(0, len(extras)-1)] + '  ' + comments_part1[random.randint(0, len(comments_part1)-1)] + '  ' + comments_part2[random.randint(0, len(comments_part2)-1)])

                print('c')
                sleep(5)
                elem = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]")
                elem.click()

                comment_count += 1
                print("Comments count: {}".format(comment_count))
                if comment_count > COUNT_LIMIT:
                    END_FLAG = True
            except Exception as e: 
                print(e)
                continue


