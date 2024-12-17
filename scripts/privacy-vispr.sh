 #!/bin/bash

### vispr
export OPENAI_API_KEY=""
export GOOGLE_API_KEY=""
export TOGETHER_API_KEY=
export TOGETHER_BASE_URL=

model_id="models/gemini-1.5-pro-001"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

model_id="llava-hf/llava-v1.6-vicuna-7b-hf"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

model_id="gpt-4o-2024-05-13"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

model_id="meta-llama/Llama-3.2-90B-Vision-Instruct"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

model_id="OpenGVLab/Mini-InternVL-Chat-4B-V1-5"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

model_id="OpenGVLab/InternVL2-8B"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

model_id="THUDM/cogvlm-chat-hf"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

# gpt-4-vision-preview has been deprecated, you need access to an OpenAI API key that historially had access
export OPENAI_API_KEY=''
model_id="gpt-4-vision-preview"
task="vispr"
scenario="vispr"
cd mmdt/perspectives
# export PYTHONPATH=/Users/alexxiong/Documents/Github/MMDT:$PYTHONPATH
python privacy/generate_image_to_text.py --model_id ${model_id} --scenario ${scenario} --task ${task}

