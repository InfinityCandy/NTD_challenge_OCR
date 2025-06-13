## Project Setup

Each one of the steps described below contains the commands that need to be run in order to complete the configuration step.

1. Navigate to project's root folder

```
$ cd NTD_challenge_OCR
```

2. Create a new virtual environment

```
$ python -m venv .venv
```

3. Install the tesseract OCR globally in your system

```
$ brew install tesseract
```

or if you are using windows check the official documentation on: https://tesseract-ocr.github.io/tessdoc/Installation.html

4. Install project dependencies

```
$ pip install -r requirements.txt
```

5. Install transformers for PyTorch

```
$ pip install "transformers[torch]"
```

5. Navigate to Django project folder and run migrations

```
$ cd NTD_challenge_OCR
$ python manage.py migrate
```

6. Fine-Tune model

```
$ python manage.py fine_tune "/absolute/path/to/dataset/for/fine/tunning"
```

7. Run migrations

```
$ python manage.py migrate
```

7. Create Django Superuser

```
$
```

7. Run Django server

```
$ python manage.py runserver
```

## Test solution

There are two options available to test the solution.

1. The first one is to run the following command that will allow you to test the solution over the whole dataset:

```
$ cd NTD_challenge_OCR
$ python manage.py process_dataset "/absolute/path/to/dataset"
```

You can query the ChromaDB directly to get the relevant entities and document types for each one of the processed documents using the following command:

```
$
```

2. The second option will allow you to test the solution on one single document at the time:

   1. Make sure you have the Django server up and running
   2. Open a new terminal
   3. Paste the following command on the terminal you just opened (Make sure to change the path to the document you want to process)

   ```
   $ curl -X POST -F "file=@/absolute/path/to/your/file.jpg" http://localhost:8000/process_document/
   ```

## Architecture Overview

### 1. High-Level Diagram

<Insert architecture diagram here>
USE mermaid for the diagrma

### 2. System Components

#### a. Frontend / CLI

Brief description...

#### b. Backend API

Technology used, main routes...

#### c. Document Processing Pipeline

OCR, NLP, etc...

#### d. Storage Layer

Local, cloud, DB...

### 3. Data Flow Example

Describe how an invoice is processed from upload to result...

### 4. Design Choices and Justifications

Explain everything that was open to be choosen on the components part (OCR, LLM, explain the adapter pattern, SQLite)
