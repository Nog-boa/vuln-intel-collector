# main.py
from nvd import fetch_recent_cves

def main():
    cves = fetch_recent_cves()

    for item in cves:
        cve = item["cve"]
        print(cve["id"], cve["published"])

if __name__ == "__main__":
    main()
