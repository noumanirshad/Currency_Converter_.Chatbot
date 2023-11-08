from src.Currency_Converter_Chatbot.logger import logging
from src.Currency_Converter_Chatbot.exception import CustomException
from flask import Flask
import sys
from dataclasses import dataclass


class FlaskApp:
    app = Flask(__name__)

    @app.route('/')
    def app():
        try:
            logging.info("Successfully run")
            return "hello world"

        except Exception as e:
            logging.info(f"An exception has occurred : {e}")
            raise CustomException(e, sys)
    if __name__ == "__main__":
        try:
            app.run(debug = True)
        except Exception as e:
            logging.info(f"An exception has occurred : {e}")

