from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from documents_classifier.document_processor.constants import DOCUMENT_LABELS, DOCUMENT_ENTITIES
from documents_classifier.document_processor.store_document import store_document
from documents_classifier.document_processor.run_ocr import run_ocr


def processor_pipeline(file):
    text = run_ocr(file)

    # model_id = "mistralai/Mistral-7B-Instruct-v0.1"
    # classifier = pipeline(
    #     "zero-shot-classification",
    #     model=model_id
    # )
    # result = classifier(
    #     text,
    #     candidate_labels=DOCUMENT_LABELS
    # )

    # tokenizer = AutoTokenizer.from_pretrained(model_id)
    # model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

    # pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

    # entities_to_extract = DOCUMENT_ENTITIES[result]
    # entities_to_extract = ", ".join(entities_to_extract)

    # prompt = f"""
    # Extract the following fields: {entities_to_extract}

    # From the text, that belongs to a document of type: {result}, below:

    # Text:
    # \"\"\"{text}\"\"\"

    # Give me the extracted fields in JSON format
    # """
    # result = pipe(prompt, max_new_tokens=100, do_sample=False)

    entities = {
        "first_name": "Jack",
        "last_name": "Doe",
        "email": "jackdoe@mail.com",
        "education": "Standford University",
        "work_eperience": "+12 of Software Engineering",
        "skills": ["Math", "Programming", "Communication"],
        "certifications": ["AWS Associated", "AWL ML Practicioner"],
        "languages": ["English", "German", "Japanes"]
    }

    store_document(text, "resume", entities)

    return {"text": text, "type": "resume", "entities": entities}
