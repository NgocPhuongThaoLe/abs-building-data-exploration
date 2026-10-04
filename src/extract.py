import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit, urlunsplit

import pandas as pd
import requests

# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT/"data"/"raw"

DATASETS = [
    {
        "dataset": "BUILDING_ACTIVITY",
        "version": "1.0.0",
        "data_query": (
            "https://data.api.abs.gov.au/rest/data/"
            "ABS,BUILDING_ACTIVITY,1.0.0/"
            "...TOT.9.TOT..Q"
            "?startPeriod=2023-Q2"
            "&dimensionAtObservation=AllDimensions"
        ),
        "start_period": "2023-Q2",
        "end_period": "2023-Q4",
    },
    {
        "dataset": "BA_SA2",
        "version": "2.0.0",
        "data_query": (
            "https://data.api.abs.gov.au/rest/data/"
            "ABS,BA_SA2,2.0.0/"
            "..TOT.TOT..1+2+3+4+5+6+7+8+AUS.M"
            "?startPeriod=2023-07"
            "&dimensionAtObservation=AllDimensions"
        ),
        "start_period": "2023-07",
        "end_period": "2023-09",
    },
]

def extract_dataset(config):
    
    dataset = config["dataset"]
    data_query = config["data_query"]

    # Separate the endpoint from the query parameters.
    parts = urlsplit(data_query)
    endpoint = urlunsplit(
        (parts.scheme, parts.netloc, parts.path, "", "")
    )
    params= dict(parse_qsl(parts.query, keep_blank_values=True))


    # Override the date range to extract a small sample.
    params["startPeriod"] = config["start_period"]
    params["endPeriod"] = config["end_period"]
    params["dimensionAtObservation"] = "AllDimensions"

    # Use this header to request CSV rather than XML.
    # Remove a format parameter if the copied URL contains one.
    params.pop("format", None)
    headers = {"Accept": "text/csv"}

    print(f"\nExtracting {dataset}...")


    response = requests.get(
        endpoint,
        params=params,
        headers=headers,
        timeout=120,
    )

    #Check status before saving
    print(f"HTTP status: {response.status_code}")

    # Raise an error for unsuccessful HTTP responses.
    response.raise_for_status()

    if response.status_code == 204 or not response.content.strip():
        raise ValueError(f"No data returned for {dataset}.")

    content_type = response.headers.get("Content-Type", "")
    if "csv" not in content_type.lower():
        raise ValueError(
            f"Expected CSV for {dataset}, received: {content_type}"
        )

    extracted_at = datetime.now(timezone.utc)
    timestamp = extracted_at.strftime("%Y%m%dT%H%M%S%fZ")
    filename = f"{dataset.lower()}_{timestamp}.csv"

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = RAW_DIR / filename

    # Save the original response bytes without changing the data.
    csv_path.write_bytes(response.content)

    # Read the saved file to count data rows.
    df = pd.read_csv(csv_path)

    metadata = {
        "agency": "ABS",
        "dataset": dataset,
        "version": config["version"],
        "endpoint": endpoint,
        "parameters": params,
        "request_headers": headers,
        "request_url": response.url,
        "extracted_at_utc": extracted_at.isoformat(),
        "http_status": response.status_code,
        "content_type": content_type,
        "raw_file": filename,
        "row_count": len(df),
    }

    metadata_path = csv_path.with_suffix(".json")
    metadata_path.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Saved CSV: {csv_path.name}")
    print(f"Data rows: {len(df):,}")
    print(f"Saved metadata: {metadata_path.name}")


def main():
    for config in DATASETS:
        extract_dataset(config)


if __name__ == "__main__":
    main()

    
    

