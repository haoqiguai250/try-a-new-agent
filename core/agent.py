from core.llm import LLMClient
from core.memory import Memory

class Agent:
    def __init__(self):
        self.llm = LLMClient()
        self.memory = Memory()

    def chat(self, prompt: str):
        # 1. 把用户输入加入记忆
        self.memory.add_user_message(prompt)

        # 2. 调用火山引擎（完全官方格式）
        resp = self.llm.chat(self.memory.get_messages())

        # 3. 解析官方返回结构
        for output in resp.output:
            if output.type == "message":
                reply = output.content[0].text

                # 4. 把回答存入记忆
                self.memory.add_assistant_message(reply)
                return reply

        return "抱歉，我没有获取到有效回复"