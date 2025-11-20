import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("books_data.json")


def load_data(path: Path = DATA_FILE):
    """Load and return the books dataset as a dict."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def list_genres(data=None):
    """Return a sorted list of available genres."""
    if data is None:
        data = load_data()
    return sorted(data.keys())


def get_titles_by_genre(genre: str, data=None):
    """Return list of titles for the given genre (empty list if not found)."""
    if data is None:
        data = load_data()
    return data.get(genre, [])


if __name__ == "__main__":
    data = load_data()
    genres = list_genres(data)
    print("Available genres:", ", ".join(genres))

    # show a small sample for a genre
    sample = "Fantasy"
    print(f"\nSample titles in '{sample}':")
    for t in get_titles_by_genre(sample, data)[:10]:
        print(" -", t)
