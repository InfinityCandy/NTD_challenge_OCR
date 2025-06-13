from documents_classifier.llm.label_data import label_data
from documents_classifier.llm.get_training_data import get_training_data
from documents_classifier.llm.tokenize_chunks import tokenize_chunks
from documents_classifier.llm.train_model import train_model
from transformers import AutoTokenizer
from transformers import pipeline
from functools import partial
from datasets import DatasetDict


def fine_tune_model():
    data = get_training_data()
    dataset = label_data(data)

    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    tokenize_fn = partial(tokenize_chunks, tokenizer=tokenizer)
    tokenized_dataset = DatasetDict({
        split: ds.map(
            tokenize_fn,
            batched=False,
            remove_columns=ds.column_names
        )
        for split, ds in dataset.items()
    })

    train_model(tokenized_dataset, tokenizer)

    classifier = pipeline(
        "text-classification",
        model="./my_bert_doc_classifier",
        tokenizer=tokenizer
    )

    print(classifier("Brihue Dil Ine. C 'Dr,_Venezian joined the staff of Arthur D. Little, Inc. in 1961. Since that time he 'as been engaged in a diversi-y of projects dealing with epideaiology, the design and analysis of control systeas, storage and \"retrieval of infornation, and economic problens in the fuel industry. His work has included the developrent of mathematical models of information retrieval systens and of large-scale computer systens. His Jepideniological work has dealt with mathematical models of patterns of infection and with developzent of disease subsequent to infection. \"De. Venezian received his B.Eng. in Chenical Engineering from McGill Y WUniversity in 1958. He continued his studies and received his doctorate at Californie Institute of Technology, specializing in the field of turbulent heat transfer. He is an associate member of the Operations Research Society of Anerica, the Engineering Institute of Canada, and of Signa Xi. rate"))
