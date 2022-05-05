from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,instaAdi,sifre):
        self.browser = webdriver.Chrome()
        self.instaAdi = instaAdi
        self.sifre = sifre
        self.takipci = []
        self.takip = []
        self.takip_etmeyenler = []


    def girisYap(self):
        self.browser.get("https://www.instagram.com/")

        time.sleep(1)

        self.browser.find_element_by_name("username").send_keys(self.instaAdi)
        self.browser.find_element_by_name("password").send_keys(self.sifre)
        

        time.sleep(1)

        #Click ile "Giriş Yap" butonuna HTML yoluyla tıklayarak giriş yapma
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(2)


    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.instaAdi}/")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        follower_count = len(dialog.find_elements_by_css_selector("li"))
        
        
        action = webdriver.ActionChains(self.browser)

        # space ile scroll yapmak için takipçi penceresine 1 kere tıklıyoruz.
        dialog.click()         
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
        
        dialog.click()
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
        
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)


            
        while True:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            new_count = len(dialog.find_elements_by_css_selector("li"))

            if follower_count != new_count:
                follower_count = new_count
                time.sleep(2)
            else:   
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            link = user.find_element_by_tag_name("a span").text
            self.takipci.append(link)
            print(link)

        
    def getFollow(self):
        self.browser.get(f"https://www.instagram.com/{self.instaAdi}/")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/div").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        follow_count = len(dialog.find_elements_by_css_selector("li"))


        action = webdriver.ActionChains(self.browser)

        dialog.click()
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
        dialog.click()

        while True:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            new_count = len(dialog.find_elements_by_css_selector("li"))

            if follow_count != new_count:
                follow_count = new_count
                time.sleep(2)
            else:   
                break
        
        follow = dialog.find_elements_by_css_selector("li")

        for user in follow:
            link = user.find_element_by_tag_name("a span").text
            self.takip.append(link)
            print(link)


    def geri_takip_etmeyenler(self):
        self.getFollowers()
        self.getFollow()

        for i in self.takip:
            if i not in self.takipci:
                self.takip_etmeyenler.append(i)

        print(f"Geri Takip Etmeyen Kullanıcılar: {'-'.join(self.takip_etmeyenler)}")




instaAdi = input("Kullanıcı adınızı girin: ")
sifre = input("Parolanızı girin: ")

instagram = Instagram(instaAdi,sifre)
instagram.girisYap()
time.sleep(4)
instagram.geri_takip_etmeyenler()