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

## Dataset

The current dataset contains 22 books from 7 languages.

| Language | Number of books | Books |
|---|---:|---|
| Dutch | 3 | `camera_obscura`, `max_havelaar`, `sara_burgerhart` |
| English | 4 | `alice`, `mobydick`, `pride`, `sherlock` |
| French | 3 | `candide`, `madame_bovary`, `notre_dame` |
| German | 3 | `faust`, `kafka_verwandlung`, `nietzsche_zarathustra` |
| Polish | 3 | `lalka`, `pan_tadeusz`, `quo_vadis` |
| Swedish | 3 | `gusta_berling`, `niels_holgersson`, `roda_rummet` |
| Turkish | 3 | `araba_sevdasi`, `mai_ve_siyah`, `serguzest` |

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

# to be continued