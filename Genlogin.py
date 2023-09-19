import requests

class Genlogin:

    def __init__(self, api_key):
        self.api_key = api_key
        self.LOCAL_URL = 'http://localhost:55550/profiles'

    def getProfile(self, id):
        url = f'{self.LOCAL_URL}/{id}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get('data')
        except requests.exceptions.RequestException as err:
            return err.response.json()

    def getProfiles(self, offset=0, limit=1000):
        url = self.LOCAL_URL
        params = {'limit': limit, 'offset': offset}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get('data')
            return {
                'profiles': data.get('lst_profile'),
                'pagination': data.get('pagination')
            }
        except requests.exceptions.RequestException as err:
            return err.response.json()

    def getWsEndpoint(self, id):
        url = f'{self.LOCAL_URL}/{id}/ws-endpoint'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            return err.response.json()

    def runProfile(self, id):
        url = f'{self.LOCAL_URL}/{id}/start'
        try:
            resEndpoint = self.getWsEndpoint(id);
            if  resEndpoint["data"]["wsEndpoint"] != '' : 
                return {'success': True, 'wsEndpoint': resEndpoint["data"]["wsEndpoint"]}
            
            response = requests.get(url)
            response.raise_for_status()
            if response.json().get('success'):
                return {'success': True, 'wsEndpoint': response.json().get('wsEndpoint')}
            else:
                resEndpoint = self.getWsEndpoint(id)
                if resEndpoint.get('wsEndpoint') != '':
                    return {'success': True, **resEndpoint}
                else:
                    return {'success': False, 'message': 'Profile is running in another device'}
        except requests.exceptions.RequestException as err:
            return err.response.json()

    def stopProfile(self, id):
        url = f'{self.LOCAL_URL}/{id}/stop'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            return err.response.json()

    def getProfilesRunning(self):
        url = f'{self.LOCAL_URL}/running'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            return err.response.json()
