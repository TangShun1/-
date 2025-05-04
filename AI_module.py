from openai import OpenAI


class Ai:
    def __init__(self):
        self.ai_url = "https://api.deepseek.com"  # AI的网址
        self.ai_key = "sk-5523ef8187c443b19e333c79de6e3e59"  # AI的key
        self.client = None
        self.chu_ai()  # 初始Ai
        self.disable_vocabulary = ["习近平"]  # AI的敏感词

    def chu_ai(self):
        self.client = OpenAI(api_key=self.ai_key, base_url=self.ai_url)

    def replace_sensitive_words(self, content):  # 替换全部的敏感词防止AI异常
        for vocabulary in self.disable_vocabulary:
            content = content.replace(vocabulary, "")
        return content

    def get_answer(self, content: str):  # 标准AI回复
        content = self.replace_sensitive_words(content)
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": content},
                          {
                              "role": "system",
                              "content": "请你简洁的回复.\n"
                          }],
                stream=False)
        except Exception as e:
            print(e)  # 出现异常
            return "AI出现问题"
        return response.choices[0].message.content
