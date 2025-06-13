import chromadb

# TODO: Add test to the adapter


class ChromaAdapter:
    def __init__(self):
        self.client = chromadb.Client()

    def create_collection(self, collection_name):
        self.client.get_or_create_collection(collection_name)

    def get_collection(self, collection_name):
        collection = self.client.get_collection(name=collection_name)

        return collection
