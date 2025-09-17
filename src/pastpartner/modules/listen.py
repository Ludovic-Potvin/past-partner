import vosk
import pyaudio
import json

MODEL_PATH = "/home/lpotvin/projects/pastpartner/src/pastpartner/static/vosk-model-small-fr-0.22/"
INPUT_DEVICE_INDEX = 3


def listen() -> str:
    model = vosk.Model(MODEL_PATH)

    rec = vosk.KaldiRecognizer(model, 16000)

    # Open the microphone stream
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"Device {i}: {info['name']} (inputs: {info['maxInputChannels']})")

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8192,
        input_device_index=INPUT_DEVICE_INDEX,
    )

    while True:
        data = stream.read(8192)  # read in chunks of 4096 bytes
        if rec.AcceptWaveform(data):  # accept waveform of input voice
            # Parse the JSON result and get the recognized text
            result = json.loads(rec.Result())
            if result["text"] != "":
                recognized_text = result["text"]
                return recognized_text
