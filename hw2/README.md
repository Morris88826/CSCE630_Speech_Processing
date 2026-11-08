# CSCE 630 - HW2: Speech Modification, Forced Alignment, and Speech Recognition

PSOLA-based pitch/duration modification, forced alignment with the Montreal Forced
Aligner (MFA), and text-to-speech / speech recognition experiments using the recordings
in `hw2_data/` (course speech clips plus my own voice).

## Contents

- [`problem1.ipynb`](./problem1.ipynb) - PSOLA pitch and duration modification (Praat via
  `parselmouth`), PSOLA vs. resampling, and modification of my own voice.
- [`problem2.ipynb`](./problem2.ipynb) - Forced alignment with MFA: alignment inspection,
  speaking rate and pause fraction, stressed-vowel formants/durations, and alignment of
  PSOLA-slowed speech.
- [`problem3.ipynb`](./problem3.ipynb) - Text-to-speech and Whisper (tiny/base) speech
  recognition: WER on synthetic, clean, and noisy speech, ASR robustness to PSOLA
  modification, and recognition of my own voice.
- `src/` - Helper modules: `analyzer.py` (pitch/formant analysis), `psola.py` (PSOLA
  modification), `display.py` (audio tables in notebooks).
- `output/` - Generated audio, alignments, and CSVs:
  - `problem1/` - PSOLA, resampled, and my-voice modified `.wav` files
  - `problem2/` - MFA inputs (`data/`) and `TextGrids/` with `alignment_analysis.csv`
  - `problem3/` - synthesized/modified audio, `transcripts.csv` (predicted from ASR), `asr_results.csv`
- [`report.pdf`](./report.pdf) - A single report (PDF) containing every requested plot, table, and discussions. 

## Get Started

Install necessary packages, such as `numpy`, `pandas`, `librosa`, `parselmouth-praat`,
`scipy`, `matplotlib`, `tqdm`, `torch`, `transformers`, and `jiwer`, plus the
[Montreal Forced Aligner](https://montreal-forced-aligner.readthedocs.io/) for Problem 2.

Place the data under `hw2_data/`, then run the notebooks in
order: `problem1.ipynb`, `problem2.ipynb`, then `problem3.ipynb`.
