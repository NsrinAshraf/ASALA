# ASALA Dataset

ASALA is a multi-dialect Arabic text dataset derived from authentic conversational speech, including podcasts, street interviews, and public discussion programs. It is designed to support Arabic dialect identification, conversational NLP, language modelling, and related Arabic NLP research.

## Dataset Versions

ASALA is released in two versions:

* ASALA-Raw: A large-scale corpus combining self-collected speech-derived Arabic text with publicly available Arabic dialect datasets. It preserves the original source-driven distribution and may contain textual redundancy.
* ASALA-QA: A quality-assured corpus containing 71,604 manually reviewed records. It was independently collected and reviewed using selected ISO/IEC 25012 data-quality dimensions, with greater attention to dialect representation and data quality.

The main dataset fields are `text`, `dialect`, and, where available, `country`.

## Repository Contents

This repository provides scripts supporting the reproducibility of the ASALA preprocessing workflow:

* `schema_harmonization.py` — harmonizes heterogeneous dataset schemas.
* `dialect_taxonomy_mapping.py` — maps source dialect labels to the ASALA taxonomy.
* `text_normalization_duplicate_analysis.py` — performs Arabic text normalization, exact-duplicate analysis, and cross-dialect overlap analysis.
* `requirements.txt` — lists the required Python dependencies.

Duplicate analysis in ASALA-Raw is used to quantify textual redundancy; duplicate rows are not removed from the raw release. The provided analysis performs exact matching after text normalization and should not be interpreted as semantic near-duplicate detection.

## Installation

```bash
pip install -r requirements.txt
```

## Dataset Access

The ASALA dataset is publicly available on Zenodo:

DOI: https://doi.org/10.5281/zenodo.21859731

## Citation

If you use ASALA, please cite the ASALA dataset and its associated data article.

ASALA: A Quality-Assured Multi-Dialect Authentic Spoken Arabic Text Dataset

Zenodo DOI: https://doi.org/10.5281/zenodo.21859731
