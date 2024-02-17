import whisper

model = whisper.load_model("base")
result = model.transcribe("sample.mp3")
print(result["text"])

