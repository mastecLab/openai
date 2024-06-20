from pathlib import Path
import openai


f=open("transcription1_1_prueba.txt", "r", encoding="utf-8")
content = f.read()
speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
model="tts-1",
voice="alloy",
 # input="Felicidades Julen"
input= content 
  
 # f = open("transcription1_2.txt", "w", encoding="utf-8")
)
response.stream_to_file(speech_file_path)
