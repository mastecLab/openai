from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The RobotCub Consortium, funded in part by the European Commission's Cognitive Systems and Robotics program, started developing the humanoid iCub in 2004."
)
response.stream_to_file(speech_file_path)
