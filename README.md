# Amazon Scraper

A Scrapy + Playwright project for extracting product data from Amazon.

## Features
- Extracts product titles, prices, ratings, and images.  
- Supports crawling multiple result pages.  
- Saves output to CSV or JSON.  

## Installation
```bash
git clone https://github.com/hamidreza-akbari-eng/amazon-scraper.git
cd amazon-scraper
python -m venv venv
source venv/bin/activate   
pip install -r requirements.txt

## Usage
Run the spiders in order:
1. scrapy crawl link_extractor
2. scrapy crawl data_extractor

## Output
- there will be two outputs, first pages_url.csv and second output will be monitors_info.csv file.

## ⚠️ Disclaimer:
This project is for educational purposes only. Scraping Amazon may violate their Terms of Service. Use responsibly.

