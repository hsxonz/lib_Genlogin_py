# Library <a href="https://genlogin.com" target="_blank">Genlogin API</a>
# Official Package

## Getting Started

Genlogin supports MacOS and Windows platforms.

### Installation

<!--`npm i genlogin`-->

for running example.py install slenium

`pip install selenium`

### Example

```py
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

```

### Running example:
`python example.py`
### Full GoLogin API
- Swagger: <a href="http://localhost:55550/api-docs" target="_blank">Link here</a> 

### Methods:
LOCAL_URL = "http://localhost:55550/profiles"

- ### getProfiles(limit=1000,offset=0)
  - return { profiles :[...],pagination: [...]}
- ### getProfiles(id)
  - return { id: ..., user_id: ...,profile_data:{...},...}
- ### getWsEndpoint(id)
  - return { success: true, data: { wsEndpoint: 'xxx' } }
- ### runProfile(id)
  - return {success: true, wsEndpoint: 'xxx'}
- ### stopProfile(id)
  - return { success: true }
- ### getProfilesRunning()
  - return { success: true, data: [...] }
