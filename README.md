# Poem Scraper

This Python script scrapes poems from https://allpoetry.com, a poetry community website. It uses the BeautifulSoup and Selenium WebDriver libraries to extract the title, author, and content of the poems from the HTML source code of the website. The script retrieves the first 100 poems displayed on the website by scrolling down the page and loading more content. Finally, it writes the scraped data to a text file named "poems.txt".

## Prerequisites

- Python 3.6 or later
- BeautifulSoup 4
- Selenium WebDriver
- ChromeDriver (for running the script with Google Chrome)

## Installation

- Clone or download the repository to your local machine.
- Install the required libraries using pip: `pip install -r requirements.txt`
- Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads and place it in the same directory as the script.

## Usage

To run the script, navigate to the directory where the script is located and run the following command:

```
python poem_scraper.py
```

The script will launch Google Chrome and start scraping the poems displayed on https://allpoetry.com. After the scraping is complete, the script will write the scraped data to a file named "poems.txt" in the same directory.
