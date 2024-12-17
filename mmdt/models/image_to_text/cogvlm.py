from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import torch

import requests
from PIL import Image
from transformers import AutoModelForCausalLM, LlamaTokenizer


class CogVLMClient:
    def __init__(self, model_id):
        self.device = "cuda"
        assert model_id == 'THUDM/cogvlm-chat-hf'
        self.tokenizer = LlamaTokenizer.from_pretrained('lmsys/vicuna-7b-v1.5', cache_dir='./cache')
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=True, cache_dir='./cache'
        ).to(self.device).eval()

    def generate(self, text, image_path, **kwargs):
        image = Image.open(image_path)
        image = image.convert(mode='RGB')
        inputs = self.model.build_conversation_input_ids(self.tokenizer, query=text, history=[], images=[image])
        inputs = {
            'input_ids': inputs['input_ids'].unsqueeze(0).to(self.device),
            'token_type_ids': inputs['token_type_ids'].unsqueeze(0).to(self.device),
            'attention_mask': inputs['attention_mask'].unsqueeze(0).to(self.device),
            'images': [[inputs['images'][0].to(self.device).to(torch.bfloat16)]],
        }
        # gen_kwargs = {"max_length": 2048, "do_sample": False}

        with torch.no_grad():
            outputs = self.model.generate(**inputs, **kwargs)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
        return self.tokenizer.decode(outputs[0])