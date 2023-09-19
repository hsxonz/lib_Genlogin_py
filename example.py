from Genlogin import Genlogin
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

gen = Genlogin("")
profileID = gen.getProfiles(0,1)["profiles"][0]["id"]
wsEndpoint = gen.runProfile(profileID)["wsEndpoint"].replace("ws://","").split('/')[0]

chrome_driver = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", wsEndpoint)

service = Service(executable_path=r'chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://genlogin.com")
time.sleep(5)
gen.stopProfile(profileID)









