"""
GitHub Developer, Stargazer & Contributor Lead Enricher — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/github-developer-recruiter-lead-enricher ($0.80 / 1,000 developers)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~github-developer-recruiter-lead-enricher/run-sync-get-dataset-items"

payload = {
    "repositories": [
        "langchain-ai/langchain",
        "n8n-io/n8n"
    ],
    "maxContributors": 50
}

if __name__ == "__main__":
    print(f"Running GitHub Developer, Stargazer & Contributor Lead Enricher on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
