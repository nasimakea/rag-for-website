import requests
from bs4 import BeautifulSoup



def scrape_website(url: str) -> str:
    """
    Scrapes a website and returns clean text.

    """
    

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching website: {e}")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    # ❌ Remove unwanted elements
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.extract()

    # ✅ Extract text
    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    clean_text = "\n".join(lines)

    return clean_text



    


