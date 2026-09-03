# book2genome

Understanding sequence analysis through books and language.

## Overview

This project uses books and human language as an analogy for biological sequence analysis.

Instead of working directly with DNA sequences, books are transformed into simple character sequences. Short sequence fragments (k-mers) are then counted and compared across languages to explore how local sequence composition can reveal larger structural patterns.

The goal of this project is educational: to explain ideas from bioinformatics and genomics in a way that is easier to understand for non-specialists.

---

## The Analogy

| Language | Biology |
|---|---|
| letters | nucleotides |
| books | genomes / transcripts |
| character frequency (k-mers) | sequence motifs |
| language patterns | biological sequence signatures |
| clustering by language | clustering by species or samples |

---

## Data

This project doesn't ship with book data. Add your own under `data/book/<language>/*.txt`.

Any public-domain, plain-text book in an alphabetic script works — swap in whatever
languages or titles you like. Good sources include Project Gutenberg
(gutenberg.org) for many European languages, or your national digital library
for languages Gutenberg doesn't cover well.

Requirements:
- Plain `.txt`, UTF-8 encoded
- One folder per language, using the language name in lowercase (e.g. `english/`, `french/`)
- `scripts/preprocess.py` handles removing Project Gutenberg boilerplate and
  reducing text to uppercase letters only — no other cleanup needed beforehand

The example dataset used in `notebooks/01_kmer_exploration.ipynb` contains 22 books
across 7 languages:

| Language | Number of books | Books |
|---|---:|---|
| Dutch | 3 | `camera_obscura`, `max_havelaar`, `sara_burgerhart` |
| English | 4 | `alice`, `mobydick`, `pride`, `sherlock` |
| French | 3 | `candide`, `madame_bovary`, `notre_dame` |
| German | 3 | `faust`, `kafka_verwandlung`, `nietzsche_zarathustra` |
| Polish | 3 | `lalka`, `pan_tadeusz`, `quo_vadis` |
| Swedish | 3 | `gusta_berling`, `niels_holgersson`, `roda_rummet` |
| Turkish | 3 | `araba_sevdasi`, `mai_ve_siyah`, `serguzest` |

The notebook itself works with a balanced 3-book, 3-language subset (English,
French, German) as a worked example — adjust the `languages` and `keep_books`
variables at the top of the notebook to explore a different subset.

Books are preprocessed into uppercase character-only sequences before analysis.

---

## Workflow

```text
books
→ preprocessing
→ k-mer counting
→ normalization
→ variance filtering
→ PCA / clustering
→ motif exploration
```

---

## Repository Structure

- `scripts/` — preprocessing and k-mer counting
- `notebooks/` — exploratory analysis and visualization
- `processed/` — cleaned character sequences
- `results/` — generated k-mer frequency tables
- `figures/` — output plots and visualizations

---

## Environment Setup

```bash
conda env create -f env/book.yml
conda activate book
```

## Run preprocessing

```bash
python scripts/preprocess.py
```

## Run k-mer counting

```bash
python scripts/count_kmers.py
```

## Explore the analysis

Open:

```text
notebooks/01_kmer_exploration.ipynb
```

---

## Example Analyses

- k-mer frequency distributions
- normalization effects
- PCA clustering by language
- discriminative sequence motifs
- compositional heatmaps

---

## Educational Goal

Although this project uses books and language, the same computational ideas are commonly used in genomics and transcriptomics.

The project is intended as a simple and intuitive way to introduce concepts such as sequence composition, motif discovery, clustering, and exploratory sequence analysis.