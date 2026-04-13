from volcenginesdkarkruntime import Ark
from config import settings

class LLMClient:
    def __init__(self):
        self.client = Ark(
            base_url=settings.ARK_BASE_URL,
            api_key=settings.ARK_API_KEY,
        )
        self.model = settings.ARK_MODEL

    def chat(self, input_messages):
        # 完全按照你给的火山官方格式！
        response = self.client.responses.create(
            model=self.model,
            input=input_messages,
            tools=[
                {
                    "type": "web_search",
                    "max_keyword": 2,
                }
            ],
        )
        return response