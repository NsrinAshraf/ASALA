"""Exact normalized-text duplicate analysis for ASALA.

This script quantifies duplicates; it does not delete ASALA-Raw rows.
It does not perform semantic near-duplicate detection.
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path
import pandas as pd

DIACRITICS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
SPACE = re.compile(r"\s+")

def normalize_text(value):
    if pd.isna(value):
        return ""
    text = unicodedata.normalize("NFKC", str(value))
    text = DIACRITICS.sub("", text)
    text = text.replace("\u0640", "")
    return SPACE.sub(" ", text).strip()

def duplicate_stats(df):
    counts = df["normalized_text"].value_counts(dropna=False)
    repeated = counts[counts > 1]
    total = len(df)
    distinct = int(counts.size)
    return {
        "total_records": total,
        "distinct_normalized_texts": distinct,
        "text_level_uniqueness_rate": distinct / total if total else 0.0,
        "distinct_texts_with_repeated_occurrences": int(repeated.size),
        "records_in_duplicate_groups": int(repeated.sum()),
        "redundant_occurrences_beyond_first": int((repeated - 1).sum()),
    }

def cross_dialect(df):
    valid = df[df["normalized_text"].ne("") & df["Dialect"].notna()].copy()
    out = (
        valid.groupby("normalized_text")
        .agg(
            dialect_count=("Dialect", "nunique"),
            dialects=("dialect", lambda s: "|".join(sorted(set(map(str, s))))),
            occurrence_count=("Dialect", "size"),
        )
        .reset_index()
    )
    out = out[out["dialect_count"] > 1].copy()
    out["word_count"] = out["normalized_text"].str.split().str.len()
    return out.sort_values(["word_count", "occurrence_count"], ascending=False)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output-dir", required=True)
    a = p.parse_args()

    df = pd.read_csv(a.input)
    for col in ("Text", "Dialect"):
        if col not in df.columns:
            raise ValueError(f"Input must contain '{col}'.")

    df["normalized_text"] = df["Text"].apply(normalize_text)
    stats = duplicate_stats(df)
    overlaps = cross_dialect(df)

    sets = overlaps["dialects"].apply(lambda x: frozenset(x.split("|")))
    related = sets.eq(frozenset({"AEB", "MGH"})) | sets.eq(frozenset({"JRD", "LEV"}))
    remaining = overlaps.loc[~related]

    stats.update({
        "cross_dialect_distinct_texts": int(len(overlaps)),
        "aeb_mgh_or_jrd_lev": int(related.sum()),
        "aeb_mgh_or_jrd_lev_percentage":
            float(related.mean() * 100) if len(overlaps) else 0.0,
        "other_cross_dialect_texts": int((~related).sum()),
        "other_overlaps_ge_20_words": int((remaining["word_count"] >= 20).sum()),
        "other_overlaps_ge_30_words": int((remaining["word_count"] >= 30).sum()),
        "other_overlaps_ge_50_words": int((remaining["word_count"] >= 50).sum()),
        "other_overlaps_ge_100_words": int((remaining["word_count"] >= 100).sum()),
    })

    outdir = Path(a.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    with open(outdir / "duplicate_statistics.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    overlaps.to_csv(outdir / "cross_dialect_exact_overlaps.csv",
                    index=False, encoding="utf-8-sig")

    long_other = overlaps.loc[(~related) & (overlaps["word_count"] >= 20)]
    long_other.to_csv(outdir / "manual_review_candidates_ge20.csv",
                      index=False, encoding="utf-8-sig")

    for key, value in stats.items():
        print(f"{key}: {value:.4f}" if isinstance(value, float)
              else f"{key}: {value:,}")
    print("Exact matches after normalization; not semantic near-duplicates.")

if __name__ == "__main__":
    main()
