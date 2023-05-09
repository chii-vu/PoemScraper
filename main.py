import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://allpoetry.com/#t_picks"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

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
        file.write("\n" + poem.text.strip() + "\n\n")
