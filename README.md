# Amazon Scraper

A Scrapy + Playwright project for extracting product data from Amazon.

## Features
- Extracts product titles, prices, ratings, and images.  
- Supports crawling multiple result pages.  
- Saves output to CSV or JSON.  

## Installation
- git clone https://github.com/hamidreza-akbari-eng/amazon-scraper.git<br>
- cd amazon-scraper<br>
- python -m venv venv<br>
- source venv/bin/activate  
- pip install -r requirements.txt

## Usage
Run the spiders in order:
1. `scrapy crawl link_extractor`
2. `scrapy crawl data_extractor`

## Output
- There will be two outputs: `pages_url.csv` and `monitors_info.csv`.

## ⚠️ Disclaimer
This project is for educational purposes only. Scraping Amazon may violate their Terms of Service. Use responsibly.
