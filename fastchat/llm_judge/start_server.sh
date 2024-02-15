python3 -m fastchat.serve.controller
python3 -m fastchat.serve.vllm_worker --model-path meta-llama/Llama-2-7b-chat-hf
python3 -m fastchat.serve.openai_api_server --host localhost --port 8000

