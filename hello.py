import requests

gene = input("Enter a gene name: ")

base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# Search PubMed
search_url = f"{base}esearch.fcgi?db=pubmed&term={gene}[Title/Abstract]&retmode=json&retmax=5"
search_data = requests.get(search_url).json()

ids = search_data["esearchresult"]["idlist"]

if not ids:
    print("No articles found.")
else:
    # Get summaries
    summary_url = f"{base}esummary.fcgi?db=pubmed&id={','.join(ids)}&retmode=json"
    summary_data = requests.get(summary_url).json()

    print(f"\nTop articles about {gene}:\n")

    for uid in summary_data["result"]["uids"]:
        title = summary_data["result"][uid]["title"]
        print(title)
