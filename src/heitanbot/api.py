import requests
from logging import getLogger

logger = getLogger(__name__)

class HeitanAPI:
    def __init__(self, is_debug=False):
        master = "https://0htjwvzstd.execute-api.ap-northeast-1.amazonaws.com/master"
        dev = "https://l3g8ddslol.execute-api.ap-northeast-1.amazonaws.com/dev"
        self.base_url = dev if is_debug else master

    def moderate(self, text:str) -> str:
        endpoint = "/moderations"
        data = {
            "prompt": text,
            "user_id": "heitanbot",
            "model": "gpt-4-turbo",
            "response_language": "日本語"
        }
        return self._post(endpoint, data)["response"]

    def is_safe(self, text:str) -> bool:
        endpoint = "/moderations/suggestions/safety"
        data = {
            "prompt": text,
            "user_id": "heitanbot"
        }
        return self._post(endpoint, data)["is_required_moderation"]

    def _post(self, endpoint, data):
        try:
            header = {
                "Content-Type": "application/json"
            }
            response = requests.post(self.base_url + endpoint, json=data, headers=header)
            return response.json()
        except requests.exceptions.ConnectionError as e:
            logger.error(f"ConnectionError: {e}")
            return None
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTPError: {e}")
            return None
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout: {e}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"RequestException: {e}")
            return None



