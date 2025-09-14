import sounddevice as sd

from piper import PiperVoice


def main() -> None:
    # Setup piper
    model = "./static/voices/fr_FR-mls-medium.onnx"
    voice = PiperVoice.load(model)

    # Text to do
    text = "Hello from pastpartner!"

    # Execution
    audio = voice.synthesize(text)

    sd.play(audio, voice.config.sample_rate)
