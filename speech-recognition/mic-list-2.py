import speech_recognition as sr
import pyaudio
m = None
for device_index in sr.Microphone.list_working_microphones():
    m = sr.Microphone(device_index=device_index)
    break
else:
    raise Error("No working microphones found!")

if m is not None:
    print("Mic ready")

    # Now you are ready to recognize
    r = sr.Recognizer()