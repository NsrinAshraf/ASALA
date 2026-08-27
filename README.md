# ASALA Dataset

ASALA is a multi-dialect Arabic text dataset derived from authentic conversational speech, including podcasts, street interviews, and public discussion programs. It is designed to support Arabic dialect identification, conversational NLP, language modelling, and related Arabic NLP research.

## Dataset Versions

ASALA is released in two complementary versions:

* ASALA-Raw: A large-scale corpus combining self-collected speech-derived Arabic text with publicly available Arabic dialect datasets. It preserves the source-driven characteristics and dialect distribution of the integrated resources. Exact duplicate analysis is provided to characterize textual redundancy in this version.

* ASALA-QA: A quality-assured corpus containing 71,604 manually reviewed records independently collected from conversational sources. The corpus underwent additional manual verification and quality assessment based on selected ISO/IEC 25012 data-quality dimensions, with greater attention to dialect representation and data quality.

ASALA-QA contains three fields:

| Field     | Description                                    |
| --------- | ---------------------------------------------- |
| `Text`    | Speech-derived Arabic transcription            |
| `Dialect` | Assigned Arabic dialect category               |
| `Country` | Geographic association of the source recording |

Country and dialect represent different levels of information: `Country` describes the geographic association of the source, whereas `Dialect` represents the linguistic variety assigned to the corresponding text.

## Repository Contents

This repository provides scripts and analysis resources supporting the reproducibility and characterization of ASALA:

* `schema_harmonization.py` — harmonizes heterogeneous source schemas into the ASALA structure.
* `dialect_taxonomy_mapping.py` — maps source-specific dialect labels to the unified ASALA dialect taxonomy.
* `text_normalization_duplicate_analysis.py` — performs Arabic text normalization, exact-duplicate analysis, and cross-dialect exact-overlap analysis.
* `ASALA_QA_dataset_specifications.ipynb` — generates descriptive statistics and technical specifications for ASALA-QA, including dialect and country distributions, text-length statistics, lexical statistics, missing values, duplicate analysis, and cross-dialect overlap.

## Duplicate Analysis

For ASALA-Raw, duplicate analysis is used to quantify textual redundancy while preserving the source-driven structure of the integrated corpus. Duplicate rows are not removed from the raw release.

Duplicate detection is based on exact comparison of normalized textual content. The procedure should therefore be interpreted as exact normalized-text duplicate detection and not as semantic or near-duplicate detection.

## Data Splits

ASALA is released without predefined training, validation, or test partitions. Researchers can construct task-specific splits according to their experimental requirements and are encouraged to apply appropriate duplicate and leakage checks when creating evaluation partitions.

## Dataset Access

The ASALA dataset is publicly available on Zenodo.

DOI: https://doi.org/10.5281/zenodo.21859731

## Citation

If you use ASALA in your research, please cite the dataset and its associated data article:

ASALA: A Quality-Assured Multi-Dialect Authentic Spoken Arabic Text Dataset

Zenodo DOI: https://doi.org/10.5281/zenodo.21859731
