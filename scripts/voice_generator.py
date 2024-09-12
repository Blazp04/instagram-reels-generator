import requests
import os
from dotenv import load_dotenv

load_dotenv()


def generate_audio(text, voice_id, output_folder, file_name):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY")
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    try:
        response = requests.post(url, json=data, headers=headers)

        response.raise_for_status()

        output_path = os.path.join(output_folder, file_name)

        with open(output_path, 'wb') as f:
            f.write(response.content)

        print(f"Audio generated and saved as {output_path}")
        return output_path

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
