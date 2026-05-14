# book2genome

Understanding biological sequence analysis through books and language.

## Idea

This project treats books as biological-like sequences.

Instead of DNA bases (A/C/G/T), books are converted into letter sequences.
Character k-mer analysis is then used to explore compositional patterns across languages,
analogous to motif discovery and sequence analysis in genomics.

## Workflow

books
→ preprocessing
→ k-mer counting
→ normalization
→ variance filtering
→ PCA / clustering
→ motif interpretation

## Structure

- `scripts/` : preprocessing and k-mer counting
- `notebooks/` : exploratory analysis
- `processed/` : cleaned text sequences
- `results/` : k-mer frequency tables
- `figures/` : generated visualizations

## Environment

```bash
conda env create -f env/book.yml
conda activate book