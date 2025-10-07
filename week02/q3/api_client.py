import requests
import json
from requests import RequestException


def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        data = json.loads(response.text)
        return data
    except RequestException as error:
        return None
    except requests.exceptions as error:
        return None
    except Exception as e:
        print(e)
        return None




