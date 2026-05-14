from pathlib import Path
from collections import Counter
import pandas as pd
from tqdm import tqdm

seq_dir = Path("processed/book")
out_dir = Path("results/kmers")
out_dir.mkdir(parents=True, exist_ok=True)

ks = range(1, 7)

books = sorted(seq_dir.glob("*/*.txt"))

for k in ks:

    rows = []

    for book in tqdm(books, desc=f"k={k}"):

        lang = book.parent.name
        seq = book.read_text(encoding="utf-8")

        counts = Counter(
            seq[i:i+k]
            for i in range(len(seq) - k + 1)
        )

        total = sum(counts.values())

        for kmer, count in counts.items():

            rows.append({
                "language": lang,
                "book": book.stem,
                "k": k,
                "kmer": kmer,
                "count": count,
                "frequency": count / total
            })

    df = pd.DataFrame(rows)

    out_file = out_dir / f"k{k}_book_counts.tsv"

    df.to_csv(out_file, sep="\t", index=False)

    print(out_file)