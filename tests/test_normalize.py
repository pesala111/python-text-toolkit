from textkit.core.normalize import normalize_text


def test_normalize_whitespace() -> None:
    assert normalize_text("  hi   there \n") == "hi there"


def test_normalize_lower() -> None:
    assert normalize_text("HeLLo", lower=True) == "hello"