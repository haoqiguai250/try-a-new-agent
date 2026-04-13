from core.llm import LLMClient
from core.memory import Memory
import logging

logger = logging.getLogger(__name__)


class Agent:
    def __init__(self):
        self.llm = LLMClient()
        self.memory = Memory(max_round=10)

    def chat(self, prompt: str) -> str:
        if not prompt.strip():
            return "请输入有效问题"

        # 加入用户消息
        self.memory.add_user_message(prompt)

        try:
            resp = self.llm.chat(self.memory.get_messages())

            # 遍历火山返回的 output
            for output in resp.output:
                # 正常文本回答
                if output.type == "message":
                    reply = output.content[0].text
                    self.memory.add_assistant_message(reply)
                    return reply

                # 如果你以后要扩展工具调用，这里预留位置
                elif output.type == "function_call":
                    logger.info("模型触发function_call")
                    return "暂未支持自定义工具调用"

            return "未获取到有效回复"

        except Exception as e:
            logger.error(f"Agent对话异常: {e}")
            return f"服务暂时异常: {str(e)}"