import re

_WHITESPACE = re.compile(r"\s+")


def normalize_text(text: str, *, lower: bool = False) -> str:
    """Trim, collapse whitespace, optionally lowercase."""
    out = _WHITESPACE.sub(" ", text.strip())
    return out.lower() if lower else out