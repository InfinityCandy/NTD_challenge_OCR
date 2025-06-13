from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from documents_classifier.llm.constants import LABELS_TO_IDS, IDS_TO_LABELS


def train_model(tokenized_dataset, tokenizer):
    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=len(LABELS_TO_IDS),
        id2label=IDS_TO_LABELS,
        label2id=LABELS_TO_IDS
    )

    training_args = TrainingArguments(
        output_dir="./results",
        eval_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
        tokenizer=tokenizer,
    )

    trainer.train()

    trainer.save_model("./my_bert_doc_classifier")
