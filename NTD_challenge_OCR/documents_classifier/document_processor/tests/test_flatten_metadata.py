from documents_classifier.document_processor.flatten_metadata import flatten_metadata


def test_flatten_metadata_with_list_and_dict():
    doc_type = "resume"
    entities = {
        "skills": ["Python", "ML"],
        "experience": {"years": 5, "role": "Engineer"},
    }
    expected = {
        "type": "resume",
        "skills": "['Python', 'ML']",
        "experience": "{'years': 5, 'role': 'Engineer'}",
    }
    result = flatten_metadata(doc_type, entities)
    assert result == expected


def test_flatten_metadata_with_primitives():
    doc_type = "invoice"
    entities = {
        "total": 199.99,
        "paid": True,
        "date": "2025-01-01"
    }
    expected = {
        "type": "invoice",
        "total": 199.99,
        "paid": True,
        "date": "2025-01-01"
    }
    result = flatten_metadata(doc_type, entities)
    assert result == expected
