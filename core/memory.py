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
        # 一轮对话占2条消息，超过就只保留最新的，保留N轮对话
        max_messages = self.max_round * 2
        if len(self.messages) > max_messages:
            self.messages = self.messages[-max_messages:]

    def clear(self):
        self.messages = []