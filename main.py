from scripts.video_generator import concatenate_videos_with_audio
from scripts.text_generation import generate_text
from scripts.voice_generator import generate_audio
import os
from dotenv import load_dotenv
load_dotenv()


AUDIO_OUTPUT_FOLDER = "generated_audio"
VIDEO_OUTPUT_FOLDER = "generated_video"

INPUT_VIDEO_FOLDER = "videos"
INPUT_AUDIO_FOLDER = "generated_audio"
OUTPUT_FILE = "generated_video/output.mp4"

PERSON_1_VOICE = "pNInz6obpgDQGcFmaJgB"
PERSON_2_VOICE = "TX3LPaxmHKxFdv7VOQHJ"


if __name__ == "__main__":
    STORY_THEME = input("Unesite temu na koju želite napraviti video: ")
    scenario = generate_text(STORY_THEME)

    # Extracting voice from script
    for i in range(len(scenario)):
        line = scenario[i]
        text = line["text"]
        voice = ""
        if line["character"] == "person 1":
            voice = PERSON_1_VOICE
        if line["character"] == "person 2":
            voice = PERSON_2_VOICE

        # generating audio for the script
        os.makedirs(AUDIO_OUTPUT_FOLDER, exist_ok=True)
        generate_audio(text, voice, AUDIO_OUTPUT_FOLDER, str(i) + ".mp3")

    os.makedirs(VIDEO_OUTPUT_FOLDER, exist_ok=True)
    # generating video
    concatenate_videos_with_audio(
        INPUT_VIDEO_FOLDER, INPUT_AUDIO_FOLDER, OUTPUT_FILE)
