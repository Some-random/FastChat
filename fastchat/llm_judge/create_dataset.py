from datasets import load_dataset

# Replace 'path_to_your_file.jsonl' with the actual path to your JSONL file
dataset = load_dataset('json', data_files={'validation': 'mt_bench_7b_evaluative.jsonl'})
dataset.save_to_disk('mt_bench_7b_evaluative')

