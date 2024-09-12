import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def generate_text(theme):
    API_KEY = os.getenv("OPENAI_API_KEY")

    # Define the endpoint
    endpoint = "https://api.openai.com/v1/chat/completions"

    # Define the model
    model = "gpt-4o-mini-2024-07-18"

    # Define headers
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # JSON payload based on your provided schema and expectation
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Your name is StorytellerGPT. Your task is to create engaging narratives that explore different perspectives in conversations. In this story, two characters, Alice and Bob, engage in a lively debate about the teme that is provided. Make it big drama and lots of emotions"
            },
            {
                "role": "user",
                "content": "Write story about " + theme
            }
        ],
        "response_format": {  # Ispravljeno dodavanje 'response_format' unutar glavnog objekta
            "type": "json_schema",
            "json_schema": {
                "name": "dialogue_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "result": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "character": {
                                        "type": "string",
                                        "enum": ["person 1", "person 2"]
                                    },
                                    "text": {
                                        "type": "string"
                                    }
                                },
                                "required": ["character", "text"],
                                "additionalProperties": False
                            }
                        }
                    },
                    "required": ["result"],
                    "additionalProperties": False
                }
            }
        }
    }

    # Send the POST request
    response = requests.post(endpoint, headers=headers,
                             data=json.dumps(payload))

    if response.status_code == 200:
        # Parsing the full response
        response_json = response.json()

        # Accessing the "choices" list and the first message's content
        choices = response_json.get("choices")
        if choices:
            message = choices[0].get("message")
            if message:
                # Print only the JSON part corresponding to the user's question
                parsed_content = message.get("content")
                if parsed_content:
                    parsed_dict = json.loads(parsed_content)["result"]
                    return parsed_dict
                else:
                    # For schemas with `strict=False`
                    print("No parsed content found.")
            else:
                print("No message content found.")
        else:
            print("No choices found in the response.")
    else:
        print(f"Request failed: {response.status_code} - {response.text}")
