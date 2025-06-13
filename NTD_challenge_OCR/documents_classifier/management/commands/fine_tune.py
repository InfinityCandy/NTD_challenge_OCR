from pathlib import Path
import json
from django.core.management.base import BaseCommand
from documents_classifier.ocr.run_ocr import run_ocr
from documents_classifier.utils.clean_text import clean_text
from documents_classifier.llm.fine_tune_model import fine_tune_model


class Command(BaseCommand):
    help = "Fine-tunes the LLM model used for the calsification task"

    def add_arguments(self, parser):
        parser.add_argument(
            "dataset_path",
            type=str,
            help="Path to where the dataset used to fine-tune the model is stored"
        )

    def handle(self, *args, **options):
        dataset_path = options["dataset_path"]
        path = Path(dataset_path)

        if path.exists() and path.is_dir():
            for folder in path.iterdir():
                extracted_texts = []

                if folder.is_dir():
                    files = list(folder.iterdir())[:15]

                    for file in files:
                        if file.is_file():
                            text = run_ocr(f"{path}/{folder.name}/{file.name}")
                            cleaned_text = clean_text(text)

                            print({
                                "filename": file.name,
                                "label": folder.name
                            })

                            extracted_texts.append({
                                "filename": file.name,
                                "text": cleaned_text,
                                "label": folder.name
                            })

                file_name = f"documents_classifier/data/processed_{folder.name}_texts.json"
                with open(file_name, "w", encoding="utf-8") as json_file:
                    json.dump(extracted_texts, json_file, indent=4)

            fine_tune_model()

        else:
            self.stdout.write(
                self.style.ERROR(
                    f"Path {dataset_path} does not exits or is not a folder!")
            )
