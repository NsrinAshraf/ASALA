# ASALA Reproducibility Scripts

This repository contains scripts supporting preprocessing and technical validation of ASALA.

## Included scripts
- `schema_harmonization.py`: renames heterogeneous source columns into the common ASALA schema.
- `dialect_taxonomy_mapping.py`: maps source-specific dialect labels to the ASALA taxonomy.
- `text_normalization_duplicate_analysis.py`: normalizes Arabic text and quantifies exact textual duplication and cross-dialect exact overlap.

## Important methodological notes
ASALA-Raw preserves source-driven characteristics, so duplicate analysis does not delete rows from ASALA-Raw.

Exact duplicate detection is performed after schema harmonization using normalized textual content. The procedure applies Unicode normalization, removes Arabic diacritics and tatweel, and normalizes whitespace. This is exact matching after normalization, not semantic near-duplicate detection.

The analysis scripts require `text` and `dialect` columns. A `country` column is optional.

The dataset is released without predefined train/validation/test partitions. Researchers should construct leakage-aware task-specific splits.

## Usage
```bash
python schema_harmonization.py --input SOURCE.csv --output harmonized.csv --source SOURCE_NAME
python dialect_taxonomy_mapping.py --input harmonized.csv --output mapped.csv
python text_normalization_duplicate_analysis.py --input mapped.csv --output-dir duplicate_analysis
```

## Before public release
Fill the configuration dictionaries in the schema and dialect-mapping scripts with the exact mappings actually used in the final ASALA workflow. Do not add undocumented mappings.

Add the permanent ASALA dataset DOI and the selected code license before publication.
