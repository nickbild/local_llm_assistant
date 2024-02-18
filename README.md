# World's Easiest GPT-like Voice Assistant

The World's Easiest GPT-like Voice Assistant uses an open-source Large Language Model (LLM) to respond to verbal requests, and it runs 100% locally on a Raspberry Pi.

My [ChatGPT-powered voice assistant](https://github.com/nickbild/voice_chatgpt) has received a lot of interest, with many requests being made for a step-by-step installation guide. I never got around to writing up the guide, and now the methods used are a bit dated and technology has advanced. As such, I have decided to build an updated LLM-based voice assistant, and this time, also provide full instructions.

This time around, the voice assistant runs fully locally on a Raspberry Pi 4 — no Internet connectivity or cloud-based services are needed. It is also very easy to set up, so I named it the World's Easiest GPT-like Voice Assistant, which is almost certainly not true. But it is at least close to the truth, and it gets the point across in few words, so please go easy on me. :)

## How It Works

## Instructions

- Write Ubuntu 22.04.3 LTS (64-BIT) to an SD card with the Raspberry Pi Imager software.
  - Raspberry Pi OS is incompatible with llamafile, unless you are using a Raspberry Pi 5.

On the Raspberry Pi:

```
sudo apt update
sudo apt install ffmpeg
sudo apt install espeak
sudo apt install python3-pip
sudo apt install python3-pyaudio
pip3 install openai openai-whisper RPi.GPIO pyaudio

git clone https://github.com/nickbild/local_llm_assistant
cd local_llm_assistant
wget https://huggingface.co/jartine/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile?download=true
mv TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile?download=true TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
chmod 755 TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
```

- Plug a speaker into the headphone jack
- Plug in a USB microphone
- Wire a pushbutton to pins 6 and 8 (BOARD numbering scheme)

Start up the LLM with:
```
./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
```
Then, in a different window, start the voice assistant software:
```
python3 chatbot.py
```

Wait a few seconds until you see the "Ready..." message, then press the button when you want to talk. When you see the "recording" message, speak your request. After the LLM completes its work, the response will be spoken through the speaker.

*NOTE*: The first time that you run this script, the speech-to-text model will need to be downloaded, so have patience. It will be cached locally for future runs.

## Media

## Bill of Materials

- 1 x Raspberry Pi 4 (a Pi 5 should also work great, but not tested)
- 1 x USB microphone
- 1 x Speaker with TRS plug input
- 1 x Pushbutton

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
