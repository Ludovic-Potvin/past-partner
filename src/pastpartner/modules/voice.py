import sounddevice as sd
from piper import PiperVoice

MODEL_PATH = "./src/pastpartner/static/fr_FR-gilles-low.onnx"


def play(text: str):
    voice: PiperVoice = PiperVoice.load(MODEL_PATH)
    with sd.OutputStream(
        samplerate=voice.config.sample_rate,
        channels=1,  # or chunk.sample_channels
        dtype="float32",
    ) as stream:
        for chunk in voice.synthesize(text):
            _ = stream.write(chunk.audio_float_array)
