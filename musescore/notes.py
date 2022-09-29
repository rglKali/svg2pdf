# [DOWNLOAD SVG]
import urllib.request

# [UNDETECTED CHROMEDRIVER]
import undetected_chromedriver.v2 as uc

# [SELENIUM]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# [OTHER]
from time import sleep


class MusicScore:
    def __init__(self, link):
        self.local_links = []
        self.images = []
        self.aop = 0  # amount of pages.
        self.link = link

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # This is to remove our window and reduce memory usage.

        self.chromedriver_path = 'path_to_chromedriver'  # Тут и так все ясно))).
        self.options.binary_location = '/usr/bin/google-chrome-stable'  # Default path to google chrome(debian based OS)

        self.options.add_argument('--no-sandbox')  # Chrome executing mode.
        self.options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        self.options.add_argument('--disable-dev-shm-usage')  # Disable shm to bypass an errors with JS.
        self.options.add_argument('--disable-infobars')  # I don't know what is it, but it helps me sometimes.
        caps = webdriver.DesiredCapabilities.CHROME
        caps['acceptSslCerts'] = True  # We accept all SslCerts. Just keep our time.
        self.driver = uc.Chrome(
            port=0,
            options=self.options,
            desired_capabilities=caps,
            keep_alive=True
        )
        self.wait = lambda seconds: WebDriverWait(self.driver, seconds)
        self.driver.get(self.link)

    def pars_link(self):
        divs = self.wait(5).until(ec.presence_of_all_elements_located((By.TAG_NAME, 'div')))
        for div in divs:
            self.driver.execute_script('arguments[0].scrollIntoView();', div)
            sleep(0.2)
            img = self.driver.find_element(By.TAG_NAME, 'img')
            self.images.append(img.get_attribute('src'))

    def save_svg(self):
        i = 0
        for url in self.images:
            if 's3' in url:
                urllib.request.urlretrieve(url, f'svgs/{i}.svg')
                i += 1


if __name__ == '__main__':
    ms = MusicScore(link='https://musescore.com/kevintran99/scores/5490570/embed')
    ms.pars_link()
    ms.save_svg()
