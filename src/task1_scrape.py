import requests
from bs4 import BeautifulSoup
import json


def fetch_wikipedia_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def extract_title(soup):
    title_tag = soup.find("h1", id="firstHeading")
    if title_tag:
        return title_tag.get_text().strip()
    return None


def extract_first_sentence(soup):
    for p in soup.find_all("p"):
        text = p.get_text().strip()
        if text:
            first_sentence = text.split(".")[0].strip() + "."
            return first_sentence
    return None


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    page_content = fetch_wikipedia_page(url)
    soup = BeautifulSoup(page_content, 'html.parser')

    # Extract the title of the page
    title = extract_title(soup)

    # Extract the first sentence of the first paragraph
    first_sentence = extract_first_sentence(soup)

    # Combine the extracted data
    extracted_data = {"title": title, "first_sentence": first_sentence}

    # Print the extracted data
    print("Extracted Data:", extracted_data)

    # Save the data to a JSON file
    save_to_json(extracted_data, 'extracted_wikipedia_data.json')

    print("Data successfully saved to extracted_wikipedia_data.json")
