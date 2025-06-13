import uuid
import chromadb
from documents_classifier.document_processor.flatten_metadata import flatten_metadata


def store_document(text, doc_type, entities):
    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(name="documents")

    document_id = str(uuid.uuid4())

    collection.add(
        ids=[document_id],
        documents=[text],
        metadatas=flatten_metadata(doc_type, entities)
    )
