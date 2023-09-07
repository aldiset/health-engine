from app.engine.engine import ChatGPT
from app.schema.chat import SchemaChats

class SymptomChecker:

    def __init__(self, symptoms):
        self.symptoms = symptoms

    async def run(self, functions: list):
        chats = SchemaChats(
            role="user",
            content=f"Bisakah Anda memberikan wawasan komprehensif tentang status kesehatan saya secara keseluruhan, faktor risiko, dan rekomendasi untuk perawatan?",
        )
        chatgpt = ChatGPT()
        return await chatgpt.run()