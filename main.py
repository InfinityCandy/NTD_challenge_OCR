import re
from textblob import TextBlob
import pytesseract
from PIL import Image
from transformers import pipeline
from document_types import DOCUMENT_TYPES


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    text = re.sub(r'page\s+\d+', '', text)

    return text.strip()


def correct_text(text: str) -> str:
    blob = TextBlob(text)
    corrected = [str(TextBlob(str(sentence)).correct())
                 for sentence in blob.sentences]

    corrected_text = ' '.join(corrected)

    return corrected_text


def classify_doc_type(text: str) -> str:
    classifier = pipeline(
        "text2text-generation",
        model="teknium/OpenHermes-2.5-Mistral-7B"
    )

    doc_type_names = []
    doc_type_descriptions = ""
    for doc_type in DOCUMENT_TYPES:
        doc_type_names.append(doc_type["name"])

        doc_type_descriptions += f"""Name: {doc_type["name"]} \nDescription: {doc_type["description"]}\n\n"""

    prompt = f"""
    Classify the document type of the following text:\n\n{text}\n\n

    Here is a short description of each one of the different documment types: {doc_type_descriptions}
    
    Answer with one label only from the following list of labels: {", ".join(doc_type_names)}."""

    print(len(prompt))

    result = classifier(prompt, max_new_tokens=10)
    return result[0]['generated_text']


def main():
    print("Text extraction")
    text = extract_text(PATH)
    print("Text cleaning")
    cleaned_text = clean_text(text)

    print("Text correction")
    corrected_text = correct_text(cleaned_text)
    print(corrected_text)
    print("Doc type clasification")
    doc_type = classify_doc_type(corrected_text)

    print(doc_type)


if __name__ == "__main__":
    main()
