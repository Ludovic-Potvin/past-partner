import wave
from importlib.resources import files

from piper import PiperVoice

def main() -> None:
    file = 'fr_FR-mls-medium.onnx'
    model = files().joinpath(voice_file)


    voice = PiperVoice.load(voice_model)
    print("Hello from pastpartner!")
