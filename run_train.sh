torchrun --nproc_per_node=2 --master_port=20001 fastchat/train/train_xformers.py \
    --model_name_or_path /bask/projects/j/jlxi8926-auto-sum/dongwei/Llama-2-7b-chat-hf \
    --data_path data/dummy_conversation.json \
    --bf16 True \
    --output_dir output_dongwei \
    --num_train_epochs 3 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 16 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 1200 \
    --save_total_limit 10 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --lazy_preprocess True
