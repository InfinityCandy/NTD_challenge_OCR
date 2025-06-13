from documents_classifier.llm.constants import MAX_TOKENS


def tokenize_chunks(example, tokenizer):
    encoded = tokenizer(
        example["text"],
        truncation=True,
        max_length=MAX_TOKENS,
        padding="max_length",
        return_attention_mask=True
    )

    return {
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"],
        "label": example["label_id"]
    }
