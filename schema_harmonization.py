import argparse
from pathlib import Path
import pandas as pd

SOURCE_SCHEMAS = {
    # "SOURCE_NAME": {"original_text_col": "Text",
    #                 "original_dialect_col": "Dialect",
    #                 "original_country_col": "Country"},
}

def harmonize_schema(df, source_name):
    if source_name not in SOURCE_SCHEMAS:
        raise KeyError(
            f"No mapping configured for {source_name!r}. "
            "Add the exact study mapping to SOURCE_SCHEMAS."
        )
    out = df.rename(columns=SOURCE_SCHEMAS[source_name]).copy()
    missing = [c for c in ("text", "dialect") if c not in out.columns]
    if missing:
        raise ValueError(f"Missing required columns after harmonization: {missing}")
    out["source_dataset"] = source_name
    return out

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--source", required=True)
    a = p.parse_args()

    df = pd.read_csv(a.input)
    out = harmonize_schema(df, a.source)
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(a.output, index=False)
    print(f"Input records: {len(df):,}")
    print(f"Output records: {len(out):,}")

if __name__ == "__main__":
    main()
