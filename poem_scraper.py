from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import os
from datetime import datetime

# Path to the Chrome driver executable
driver_path = "./chromedriver"

# URL of the webpage to scrape
url = "https://allpoetry.com"

while True:
    start = time.time()

    # Create a Chrome driver instance
    s = Service(driver_path)
    driver = webdriver.Chrome(executable_path=driver_path)

    # Load the webpage
    driver.get(url)

    # Wait for the page to fully load
    time.sleep(5)

    # Scroll down the page to load more poems
    while True:
        # Get the current height of the page
        last_height = driver.execute_script("return document.body.scrollHeight")

        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the page to load new poems
        time.sleep(2)

        # Calculate the new height of the page
        new_height = driver.execute_script("return document.body.scrollHeight")

        # If the height hasn't changed, we've reached the end of the page
        if new_height == last_height:
            break

        # Otherwise, continue scrolling down the page
        last_height = new_height

    # Get the page source
    content = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")

    # Extract all poems
    poems = soup.find_all("div", class_=lambda x: x and x.startswith("orig_"))

    # Create a new folder for today's results if it doesn't already exist
    today = datetime.today().strftime("%Y-%m-%d")
    if not os.path.exists(today):
        os.makedirs(today)

    # Write the output to a new file in the folder
    filename = "{}/poems_{}.txt".format(today, datetime.now().strftime("%H-%M-%S"))
    with open(filename, "w") as file:
        # Print the title, author, and poem of each poem
        for poem in poems:
            title = poem.find_previous("h1", class_="title").text.strip()
            author = poem.find_previous("a", class_="u nocolor").text.strip()

            file.write("Title: {}\n".format(title))
            file.write("Author: {}\n".format(author))

            # Remove leading tabs from lines after the first one
            text = poem.text.strip().replace("\t", "")
            text = text.split("\n")
            text = text[0] + "\n" + "\n".join([line.lstrip() for line in text[1:]])

            file.write(
                text
                + "\n------------------------------------------------------------\n\n"
            )

    # Close the browser
    driver.quit()

    end = time.time()
    print(f"Time: {end-start:.2f} sec")

    # Wait an hour before running again
    time.sleep(60 * 60)
