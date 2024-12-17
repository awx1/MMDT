import base64
import requests
import os
from together import Together


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


class Llama3_2Client:
    def __init__(self, model_id):
        self.api_key = os.getenv('TOGETHER_API_KEY')
        self.base_url = os.getenv('TOGETHER_BASE_URL')

        assert model_id in ["meta-llama/Llama-Vision-Free",
                            "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
                            "meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
                            "meta-llama/Llama-3.2-90B-Vision-Instruct"]
        self.model_id = model_id
        self.client = Together(api_key=self.api_key, base_url=self.base_url)

    def generate(self, text, image_path, **kwargs):
        temperature = kwargs['temperature'] if 'temperature' in kwargs else 0
        base64_image = encode_image(image_path)

        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
            temperature=temperature
        )

        responses = [resp.message.content for resp in response.choices]
        return responses[0]