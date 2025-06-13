import re


def clean_text(text):
    text = text.replace('‘', "'").replace(
        '’', "'").replace('“', '"').replace('”', '"')

    text = re.sub(r"(?<=\n)[\.\-•]", "", text)

    text = re.sub(r"-\n", "", text)

    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\.\.+", ".", text)

    return text.strip()
