###
# Nick Bild
# February 2024
#
# Be sure to start the LLM before running this script, e.g.:
# ./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
###

import os
from openai import OpenAI
import pyaudio
import wave
import whisper
import RPi.GPIO as GPIO


BUTTON = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

model = whisper.load_model("base")

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key = "sk-no-key-required"
)


def record_wav():
    form_1 = pyaudio.paInt16
    chans = 1
    samp_rate = 16000
    chunk = 4096
    record_secs = 2
    dev_index = 1
    wav_output_filename = 'input.wav'

    audio = pyaudio.PyAudio()

    # Create pyaudio stream.
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # Loop through stream and append audio chunks to frame array.
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("finished recording")

    # Stop the stream, close it, and terminate the pyaudio instantiation.
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the audio frames as .wav file.
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    return


def main():
    ###
    # Get the voice request.
    ###

    record_wav()
    result = model.transcribe("input.wav")
    
    print("Transcription: {0}".format(result["text"]))
    request = result["text"]

    ###
    # Query the LLM.
    ###

    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=[
            {"role": "system", "content": "You are an AI assistant. Your priority is helping users with their requests."},
            {"role": "user", "content": request}
        ]
    )

    ###
    # Speak the result.
    ###

    print("LLM result: {0}".format(completion.choices[0].message))
    os.system('espeak "{0}" 2>/dev/null'.format(completion.choices[0].message.content))


if __name__ == "__main__":
    print("Ready...")
    while(True):
        if GPIO.input(BUTTON) == GPIO.LOW:
            main()

