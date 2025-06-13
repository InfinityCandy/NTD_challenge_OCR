def flatten_metadata(doc_type, entities):
    flat_metadata = {"type": doc_type}
    for key, value in entities.items():
        if isinstance(value, (list, dict)):
            flat_metadata[key] = str(value)
        else:
            flat_metadata[key] = value
    return flat_metadata
