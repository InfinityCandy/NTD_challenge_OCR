from documents_classifier.utils.clean_text import clean_text


def test_replace_quotes_and_apostrophes():
    input_text = "Hello, he said. ‘It’s fine.’"
    expected_output = "Hello, he said. \'It\'s fine.'"
    assert clean_text(input_text) == expected_output


def test_hyphen_linebreak_removal_and_single_newline_handling():
    input_text = "This is a hyphen-\nbroken word.\nAnd this is a\nnew line."
    expected_output = "This is a hyphenbroken word. And this is a new line."
    assert clean_text(input_text) == expected_output


def test_bullet_and_whitespace_cleanup():
    input_text = "\n• First item\n- Second item\n. Third item\n\nMore text...\n\n"
    expected_output = "First item Second item Third item More text."
    assert clean_text(input_text) == expected_output


def test_collapse_multiple_whitespace():
    input_text = "This   sentence\tcontains   irregular   whitespace.\n\n"
    expected_output = "This sentence contains irregular whitespace."
    assert clean_text(input_text) == expected_output


def test_collapse_ellipsis_and_multiple_dots():
    input_text = "Wait... What..... Really......?"
    expected_output = "Wait. What. Really.?"
    assert clean_text(input_text) == expected_output
