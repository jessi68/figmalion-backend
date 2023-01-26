from flask import Flask, jsonify
from chat_gpt.chat_gpt_service import ChatGptService
from chat_gpt.chat_gpt_controller import chat_gpt_route_path, chat_gpt_route

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if __name__ == '__main__':
    # register modules/blueprints
    app.register_blueprint(chat_gpt_route, url_prefix=f'/{chat_gpt_route_path}')
    # start app
    #port = 3000
    app.run(port=3000, debug=True)
