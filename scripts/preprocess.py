from pathlib import Path
import unicodedata
import re
from tqdm import tqdm

raw_dir = Path("data/book")
out_dir = Path("processed/book")
out_dir.mkdir(parents=True, exist_ok=True)

keep_az = re.compile("[^A-Z]+")

def strip_gutenberg(text):

    start = text.find("*** START OF")
    if start != -1:
        text = text[start:]

        first_newline = text.find("\n")
        text = text[first_newline:]

    end = text.find("*** END OF")
    if end != -1:
        text = text[:end]

    return text

def clean_text(text):

    text = strip_gutenberg(text)

    text = unicodedata.normalize("NFKD", text.upper())
    text = keep_az.sub("", text)

    return text

books = sorted(raw_dir.glob("*/*.txt"))

for book in tqdm(books, desc="preprocessing books"):

    lang = book.parent.name
    (out_dir / lang).mkdir(parents=True, exist_ok=True)

    raw = book.read_text(encoding="utf-8", errors="ignore")
    seq = clean_text(raw)

    out_file = out_dir / lang / book.name
    out_file.write_text(seq, encoding="utf-8")