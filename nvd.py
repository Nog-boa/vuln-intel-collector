# nvd.py
import requests

NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def fetch_recent_cves(results_per_page=5):
    params = {
        "resultsPerPage": results_per_page
    }
    headers = {
        "User-Agent": "vuln-intel-collector/1.0"
    }

    r = requests.get(NVD_API_URL, params=params, headers=headers, timeout=10)
    r.raise_for_status()

    data = r.json()
    return data.get("vulnerabilities", [])
