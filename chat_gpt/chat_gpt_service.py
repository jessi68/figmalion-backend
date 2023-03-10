import os
import openai
from chat_gpt.chat_gpt_model import MessageRequestDTO
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
openai.api_key = os.getenv('OPENAI_API_KEY')

class ChatGptService:
    @classmethod
    def get_ai_model_answer(cls,data:MessageRequestDTO):
        return openai.Completion.create(
            prompt=data.question,
            model=data.model_id,
            temperature=data.temperature,
            max_tokens=data.max_tokens
        )

    @classmethod
    def list_models(cls):
        return openai.Model.list()