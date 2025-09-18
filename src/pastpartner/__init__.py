import os
from pastpartner.modules.speak import speak
from pastpartner.modules.listen import listen
from pastpartner.modules.think import think
from dotenv import load_dotenv


def main() -> None:
    # Loading env
    BASEDIR = os.path.abspath(os.path.dirname("pastpartner"))
    load_dotenv(os.path.join(BASEDIR, ".env"))

    while True:
        # Listen
        result = listen()

        # ChatGPT
        test = think(result)
        print(test)

        # Speak
        if test:
            speak(test)
