# -*- coding: utf-8 -*-
"""webscraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15WqE4vW14r6mv5Uy8K-ba7vPcOYwa97m

To install selenium
"""

pip install selenium

pip install beautifulsoup4

pip install webdriver-manager

import requests
from bs4 import BeautifulSoup
import json

# URL dari situs yang akan di-scrape
url = "https://www.darmajaya.ac.id"

# Menentukan headers dengan User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parser")

    news_titles = soup.find_all("h4")

    news_data = [{"title": title.get_text(strip=True)} for title in news_titles]

    with open("scraping_berita_darmajaya.json", "w", encoding="utf-8") as json_file:
        json.dump(news_data, json_file, ensure_ascii=False, indent=4)

    print("Data berita berhasil disimpan dalam format JSON.")
else:
    print("Gagal mengakses halaman. Status Code:", response.status_code)