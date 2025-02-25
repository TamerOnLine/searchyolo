import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_and_save_to_csv(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a', href=True)
    data = []

    keywords = [
        'cdc_disease_basics_overview-what-it-is',
        'cdc_disease_basics_types-types',
        'cdc_disease_basics_risk-risk-factors',
        'cdc_disease_basics_treatment-treatment-and-recovery',
        'cdc_disease_basics_res-resources'
    ]

    for link in links:
        href = link.get('href')
        if any(keyword in href for keyword in keywords):
            full_url = urljoin(url, href)
            data.append({'Link Text': link.get_text(strip=True), 'Href': full_url})

    with open('aortic_aneurysm_links.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Link Text', 'Href'])
        writer.writeheader()
        writer.writerows(data)

# URL for the page
url = 'https://www.cdc.gov/heart-disease/about/aortic-aneurysm.html#cdc_disease_basics_types-types'
scrape_and_save_to_csv(url)
