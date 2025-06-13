from documents_classifier.llm.constants import LABELS_TO_IDS
from datasets import Dataset


def label_data(data):
    data["label_id"] = data["label"].map(LABELS_TO_IDS)

    dataset = Dataset.from_pandas(data[["text", "label_id"]])
    dataset = dataset.train_test_split(test_size=0.2)

    return dataset
