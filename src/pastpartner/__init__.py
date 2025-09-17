from pastpartner.modules.speak import speak
from pastpartner.modules.listen import listen


def main() -> None:
    result = listen()
    print(result)

    speak(result)
