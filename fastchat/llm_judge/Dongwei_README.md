Step 1: Generate multiple model answers: python gen_model_answer.py --model-path meta-llama/Llama-2-13b-chat-hf --model-id 13b_4
Step 2: Run GPT-4 eval on those answers: python gen_judgment.py --model-list 13b_4 --parallel 50, mv data/mt_bench/model_judgment/gpt-4-0125-preview_single.jsonl data/mt_bench/model_judgment/gpt-4-0125-preview_single_13_4.jsonl
Step 3: Aggregrate results with prefix: python aggregrate_json_result.py gpt-4-0125-preview_single_13
