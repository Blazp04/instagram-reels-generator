import requests
import os


def generate_audio(text, voice_id, output_folder, file_name):
    API_KEY = os.getenv("ELEVENLABS_API_KEY")
    if not API_KEY:
        raise ValueError(
            "ELEVENLABS_API_KEY not found in environment variables. Make sure it's set in your .env file.")

        # Define the
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": API_KEY
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
