"""
GitHub Developer, Stargazer & Contributor Lead Enricher — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/github-developer-recruiter-lead-enricher ($0.80 / 1,000 developers)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~github-developer-recruiter-lead-enricher/run-sync-get-dataset-items"

def run_github_developer_recruiter_lead_enricher(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes GitHub Developer, Stargazer & Contributor Lead Enricher on Apify Cloud ($0.80/1k developers).
    Extract developer profiles, verified public commit emails, top programming languages, candidate seniority scores (0-100), company affiliations, personal blogs, and X/Twitter handles from GitHub repos.
    """
    default_payload = {
    "repositories": [
        "langchain-ai/langchain",
        "n8n-io/n8n"
    ],
    "maxContributors": 50
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
