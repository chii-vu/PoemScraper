# Poem Scraper

This Python script scrapes poems from https://allpoetry.com, a poetry community website. It uses the BeautifulSoup and Selenium WebDriver libraries to extract the title, author, and content of the poems from the HTML source code of the website. The script retrieves the first 100 poems displayed on the website by scrolling down the page and loading more content. Finally, it writes the scraped data to a text file named "poems.txt".

## Prerequisites

- Python 3.6 or later
- BeautifulSoup 4
- Selenium WebDriver
- ChromeDriver (for running the script with Google Chrome)

## Installation

- Clone or download the repository to your local machine.
- Create a virtual environment in the same directory as the script: `python -m venv PoemScraperVenv`
- Activate the virtual environment: `source PoemScraperVenv/bin/activate`
- Install the required libraries using pip: `pip install -r requirements.txt`
- Download ChromeDriver from https://chromedriver.chromium.org/downloads and place it in the same directory as the script.

## Usage

To run the script, navigate to the directory where the script is located and run the following command:

```
python poem_scraper.py
```

The script will launch Google Chrome and start scraping the poems displayed on https://allpoetry.com periodically, then write them to dated folders.

## Async version
Run the WebDriver as a service using the downloaded chromedriver file
```
# Linux command
./chromedriver --port=9999

# Windows command
.\chromedriver --port=9999
``` 
Run the script

```
python poem_scraper_async.py
```
This version tends to be a little faster than the asynchronous one.
More information in [Caqui page](https://pypi.org/project/caqui/#description)
