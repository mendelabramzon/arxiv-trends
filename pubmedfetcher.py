import requests
import xml.etree.ElementTree as ET

def fetch_pubmed_data(key_phrase, max_results=10):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = f"{base_url}esearch.fcgi?db=pubmed&term={key_phrase}&retmode=json&retmax={max_results}"
    search_response = requests.get(search_url)
    search_data = search_response.json()
    
    id_list = search_data['esearchresult']['idlist']
    if not id_list:
        return []

    fetch_url = f"{base_url}efetch.fcgi?db=pubmed&id={','.join(id_list)}&retmode=xml"
    fetch_response = requests.get(fetch_url)
    root = ET.fromstring(fetch_response.content)

    results = []
    for article in root.findall(".//PubmedArticle"):
        doi = ""
        abstract = ""
        pdf = ""

        article_data = article.find(".//ArticleIdList")
        for item in article_data:
            if item.attrib['IdType'] == "doi":
                doi = item.text
                break

        abstract_data = article.find(".//AbstractText")
        if abstract_data is not None:
            abstract = abstract_data.text

        # Note: PubMed doesn't always provide direct PDF links. This is a placeholder.
        # You might need to use the DOI to fetch the PDF from the respective journal's website.
        if doi:
            pdf = f"https://doi.org/{doi}"

        results.append({
            "doi": doi,
            "abstract": abstract,
            "pdf": pdf
        })

    return results

key_phrase = input("Enter the key phrase: ")
articles = fetch_pubmed_data(key_phrase)
for article in articles:
    print(article)
