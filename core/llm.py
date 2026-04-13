from volcenginesdkarkruntime import Ark
from config import settings
import logging

logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self):
        self.client = Ark(
            base_url=settings.ARK_BASE_URL,
            api_key=settings.ARK_API_KEY,
        )
        self.model = settings.ARK_MODEL

    def chat(self, input_messages):
        try:
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
            logger.info("调用火山引擎成功")
            return response
        except Exception as e:
            logger.error(f"LLM调用异常: {str(e)}")
            raise Exception(f"大模型服务异常: {str(e)}")