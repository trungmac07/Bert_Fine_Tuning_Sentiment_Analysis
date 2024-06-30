import torch

import numpy as np

from datasets import load_dataset

from transformers import AutoTokenizer, BertForSequenceClassification, TrainingArguments, Trainer, BertForSequenceClassification

from peft import LoraConfig, TaskType, get_peft_model, PeftModel

import evaluate



def get_fine_tuned_model(path, device = 'cpu'):
    lora_config = LoraConfig(task_type=TaskType.SEQ_CLS, r=1, lora_alpha=1, lora_dropout=0.1)
    tokenizer = tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    model = BertForSequenceClassification.from_pretrained("bert-base-cased", num_labels=2)
    model.load_adapter(path, peft_config = lora_config)
    return tokenizer, model.to(device)
