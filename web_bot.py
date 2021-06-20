from secrets import menti_code, useragent
from time import sleep
import random
import concurrent.futures

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


class WebBot:
    def __init__(self):
        # self.browser = webdriver.Chrome()# start the browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("window-size=1400,600")
        useragent = UserAgent().random
        chrome_options.add_argument("user-agent={}".format(useragent))
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--disable-gpu")
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities["acceptSslCerts"] = True
        capabilities["acceptInsecureCerts"] = True
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(
            chrome_options=chrome_options,
            desired_capabilities=capabilities,
        )
        # executable_path=r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome')
        self.browser.get("https://www.menti.com")
        sleep(5)

    def login(self):
        menti_code_inp = self.browser.find_element_by_xpath(
            '//input[@id="enter-vote-key"]'
        )
        menti_code_inp.send_keys(menti_code)

        default_login_btn = self.browser.find_element_by_xpath(
            '//button[@type="submit"]'
        )
        default_login_btn.click()

    def random_vote(self):
        vote_candidate = None
        # vote_id = 0
        attempts = 10
        # max 10 attempts to find a random voting option
        while vote_candidate == None and attempts > 0:
            vote_id = random.randint(0, 6)  # usually 6 options are there
            try:
                vote_candidate = self.browser.find_element_by_xpath(
                    '//label[@data-testid="choice-' + str(vote_id) + '"]'
                )
                vote_candidate.click()
            except:
                vote_candidate = None
                attempts -= 1

        submit_vote_btn = self.browser.find_element_by_xpath('//button[@type="submit"]')
        submit_vote_btn.click()
        if attempts >= 0:
            print("Voted successfully to " + str(vote_id))
        else:
            print("Voting failed")
        return attempts >= 0


class MentiFakeVoter:
    def cast_single_random_vote(self):
        menti_bot = WebBot()
        menti_bot.login()
        return menti_bot.random_vote()

    def cast_parallel_votes(self, N=8):
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            # Start the load operations and mark each future with its URL
            future_votes = [
                executor.submit(self.cast_single_random_vote).result() for i in range(N)
            ]
            print(f"Performed {int(sum(future_votes))} fake menti votes")
            return sum(future_votes)


voter = MentiFakeVoter()
voter.cast_parallel_votes()

print(" !! Program Running Successfully !! ")
