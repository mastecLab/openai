from openai import OpenAI
client = OpenAI()

audio_file_path = open("VIDEO1_2.mp3", "rb")
#audio_file_path = open("audio/5_tools_audio.mp4", "rb")
transcript = client.audio.transcriptions.create(
    model = "whisper-1",
    file=audio_file_path
)

# Extraer el texto de la transcripción
print(transcript)

f = open("transcription1_2.txt", "w", encoding="utf-8")
print(transcript, file=f)
f.close()
