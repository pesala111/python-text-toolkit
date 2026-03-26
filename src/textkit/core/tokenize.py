import re

_TOKEN = re.compile(r"\w+|[^\w\s]", re.UNICODE)

def simple_tokenize(text: str) -> list[str]:
    """Tokenize into words and punctuation."""
    return _TOKEN.findall(text)