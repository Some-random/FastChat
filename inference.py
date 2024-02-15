from transformers import AutoTokenizer
import transformers
import torch

# Hugging face repo name
model = "output_dongwei" #chat-hf (hugging face wrapper version)

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto" # if you have GPU
)

sequences = pipeline(
    'I liked "Breaking Bad" and "Band of Brothers". Do you have any recommendations of other shows I might like?\n',
    do_sample=True,
    top_k=10,
    top_p = 0.9,
    temperature = 0.2,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200, # can increase the length of sequence
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

