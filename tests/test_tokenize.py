from textkit.core import simple_tokenize


def test_simple_tokenize() -> None:
    assert simple_tokenize("Hi, world!") == ["Hi", ",", "world", "!"]