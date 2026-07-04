from llm import safe_invoke


class LLMService:
    def generate(self, prompt: str) -> str:
        return safe_invoke(prompt).content


llm_service = LLMService()
