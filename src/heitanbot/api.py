from logging import getLogger
import config
import asyncio
import aiohttp

logger = getLogger(__name__)


class HeitanAPI:
    def __init__(self):
        master = "https://0htjwvzstd.execute-api.ap-northeast-1.amazonaws.com/master"
        dev = "https://l3g8ddslol.execute-api.ap-northeast-1.amazonaws.com/dev"
        is_debug = config.IS_DEV
        api_key = config.OPENAI_API_KEY
        self.base_url = dev if is_debug else master
        self.api_key = api_key

    async def moderate(self, text: str) -> str:
        endpoint = "/moderations"
        data = {
            "prompt": text,
            "user_id": "heitanbot",
            "model": "gpt-3.5-turbo-0125",
            "response_language": "日本語",
            "custom_client": {"token": self.api_key},
        }
        response = await self._post(endpoint, data)
        return response["response"] if response else "エラーが発生しました"

    async def is_required_moderation(self, text: str) -> bool:
        endpoint = "/moderations/suggestions/safety"
        data = {
            "prompt": text,
            "user_id": "heitanbot",
            "custom_client": {"token": self.api_key},
        }
        response = await self._post(endpoint, data)
        return response["is_required_moderation"] if response else False

    async def _post(self, endpoint, data):
        try:
            header = {"Content-Type": "application/json"}
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.base_url + endpoint, json=data, headers=header
                ) as response:
                    return await response.json()
        except Exception as e:
            logger.error(f"Error: {e}")
            return None
