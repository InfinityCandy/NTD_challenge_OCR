from django.core.management.base import BaseCommand
from pathlib import Path


class Command(BaseCommand):
    help = "Processes the whole dataset of documents"

    def add_arguments(self, parser):
        parser.add_argument(
            "dataset_path",
            type=str,
            help="Path to where the dataset is stored"
        )

    def handle(self, *args, **options):
        dataset_path = options["dataset_path"]
        path = Path(dataset_path)

        if path.exists() and path.is_dir():
            for folder in path.iterdir():
                if folder.is_dir():
                    for file in folder.iterdir():
                        if file.is_file():
                            # TODO: Add processing pipeline here
                            print(f"  File: {file.name}")
        else:
            self.stdout.write(
                self.style.ERROR(
                    f"Path {dataset_path} does not exits or is not a folder!")
            )
