import logging
from core.agent import Agent

# 企业级基础日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)



if __name__ == "__main__":
    ai = Agent()

    print("你：今天的日期？")
    print("AI：", ai.chat("今天的日期？"))

    print("\n---")
