# textkit

A small, clean, type-checked Python toolkit for common text-processing tasks: whitespace normalization and simple tokenization, usable as a library or a CLI.

## Features

Key features include: normalization (trim, collapse repeated whitespace, and optionally lowercase text), tokenization (split text into words and punctuation), full type hints checked with mypy strict mode, linting via ruff, tests via pytest, and a Dockerfile for containerized use.

## Installation

Requires Python 3.11+.

```
pip install -e .
```

Or with uv (https://github.com/astral-sh/uv):

```
uv pip install -e .
```

## Usage

As a CLI:

```
textkit "Hello World" --normalize
textkit "HELLO" --lower
```

As a library:

```
from textkit.core import normalize_text, simple_tokenize

normalize_text("Hi there", lower=True)
simple_tokenize("Hi, world!")
```

## Development

```
make check
make fmt
make test
```

## Docker

```
docker build -f docker/Dockerfile -t textkit .
docker run --rm textkit "Hello World" --normalize
```
