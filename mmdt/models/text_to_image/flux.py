import requests
import os

import time
import torch
from diffusers import FluxPipeline

class FluxClient:
    def __init__(self, model_id):
        assert model_id in ["black-forest-labs/FLUX.1-dev"]
        self.model_id = model_id
        self.client = FluxPipeline.from_pretrained(model_id, torch_dtype=torch.bfloat16)
        self.client.enable_model_cpu_offload()

    def generate(self, text, seed, save_path):
        success = False
        while not success:
            try:
                response = self.client(
                    text,
                    output_type="pil",
                    num_inference_steps=4,
                    generator=torch.Generator("cpu").manual_seed(seed)
                ).images[0]
            except:
                continue
            success = True
        response.save(save_path)
        return response
