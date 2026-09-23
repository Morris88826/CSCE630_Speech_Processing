# CSCE 630 - HW1: Vowel Acoustics and Classification

Analysis of vowel formants and speaker-independent vowel classification using the
recordings in `hw1_data/` (men, women, and children producing 12 vowels each).

## Contents

- [`problem1.ipynb`](./problem1.ipynb) - Formant/pitch extraction (Praat via `parselmouth`), steady-state
  vowel-space visualization, group differences (men/women/children), vocal-tract-length
  (VTL) estimation, and VTL-based formant normalization.
- [`problem2.ipynb`](./problem2.ipynb) - kNN vowel classification: feature preparation, k selection and
  speaker-independent 5-fold cross-validation, generalization
  to children (raw vs. VTL-normalized formants), and MFCC-based features.
- `output/` - Generated CSVs and figures:
  - `extracted_formants.csv`, `normalized_vowelspace.csv`, `feature_table_*.csv`
  - `problem1/`, `problem2/` - plots (steady-state windows, vowel space, VTL by group,
    cross-validation results, confusion matrices, generalization accuracy, etc.)

## Get Started

Install necessary packages, such as `numpy`, `pandas`, `librosa`,
`parselmouth-praat`, `scikit-learn`, `scipy`, `seaborn`, `matplotlib`, and `tqdm`.

Place the data under `hw1_data/` (not tracked in git), then run the notebooks in
order: `problem1.ipynb` first (produces the formant/normalization CSVs consumed by
`problem2.ipynb`), then `problem2.ipynb`.
