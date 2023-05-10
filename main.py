from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Path to the Chrome driver executable
driver_path = "/home/dev/chromedriver"

# URL of the webpage to scrape
url = "https://allpoetry.com/#t_picks"

# Create a Chrome driver instance
s = Service(driver_path)
driver = webdriver.Chrome(service=s)

# Load the webpage
driver.get(url)

# Wait for the page to fully load
time.sleep(5)

# Get the page source
content = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Extract all poems
poems = soup.find_all("div", class_=lambda x: x and x.startswith("orig_"))

# Write the output to a file
with open("poems.txt", "w") as file:
    # Print the title, author, and poem of each poem
    for poem in poems:
        title = poem.find_previous("h1", class_="title").text.strip()
        author = poem.find_previous("a", class_="u nocolor").text.strip()
        file.write("Title: {}\n".format(title))
        file.write("Author: {}\n".format(author))
        file.write(
            "\n"
            + poem.text.strip()
            + "\n------------------------------------------------------------\n\n"
        )
