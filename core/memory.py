class Memory:
    def __init__(self, max_round=10):
        self.messages = []
        self.max_round = max_round  # 限制对话轮数，防止token溢出

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})
        self._truncate()

    def add_assistant_message(self, content):
        self.messages.append({"role": "assistant", "content": content})
        self._truncate()

    def get_messages(self):
        return self.messages

    def _truncate(self):
        # 保留最近 N 轮对话
        if len(self.messages) > self.max_round * 2:
            self.messages = self.messages[-self.max_round * 2:]

    def clear(self):
        self.messages = []