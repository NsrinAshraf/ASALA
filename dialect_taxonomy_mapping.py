import argparse
from pathlib import Path
import pandas as pd

ASALA_LABELS = {
    "AEB", "ALG", "EGY", "GENERAL", "GLF", "IRQ", "JRD",
    "LEV", "LYB", "MGH", "MSA", "SUD", "YEM"
}

DIALECT_MAP = {
    # "source_label": "ASALA_LABEL",
}

def map_label(value):
    if pd.isna(value):
        return value
    label = str(value).strip()
    if label in ASALA_LABELS:
        return label
    return DIALECT_MAP.get(label)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--keep-unmapped", action="store_true")
    a = p.parse_args()

    df = pd.read_csv(a.input)
    if "dialect" not in df.columns:
        raise ValueError("Input must contain a 'dialect' column.")

    original = df["dialect"].copy()
    mapped = original.apply(map_label)
    df["dialect"] = mapped.where(mapped.notna(), original) if a.keep_unmapped else mapped

    unmapped = df["dialect"].isna() & original.notna()
    if unmapped.any():
        print("Unmapped labels:")
        for x in sorted(original[unmapped].astype(str).unique()):
            print(" -", x)

    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(a.output, index=False)
    print(f"Records: {len(df):,}")
    print(f"Unmapped records: {int(unmapped.sum()):,}")

if __name__ == "__main__":
    main()
