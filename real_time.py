from threading import Thread
from queue import Queue
import pyaudio
import vosk

messages = Queue()
recordings = Queue()

# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))
#

CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2
chunk = 1024


messages.put(True)


def record_microphone(chunks=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT, channels=CHANNELS, rate=FRAME_RATE,
                    input=True, frames_per_buffer=chunk)

    frames = []

    while not messages.empty():
        data = stream.read(chunks)
        frames.append(data)

        if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunks:
            recordings.put(frames.copy())
            frames = []

    stream.stop_stream()
    stream.close()
    p.terminate()


with output:
     display("Starting")
     record = Thread(target=record_microphone)
     record.start()

     transcribe = Thread(target=speech_recognition, args=(output,))
     transcribe.start()
