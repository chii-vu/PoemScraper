import time
import asyncio
from bs4 import BeautifulSoup
import os
from datetime import datetime
from caqui import asynchronous, synchronous

async def main():
    # URL of the webpage to scrape
    url = "https://allpoetry.com"

    while True:   
        start = time.time()

        driver_url = "http://127.0.0.1:9999"
        capabilities = {
                "desiredCapabilities": {
                    "browserName": "chrome",
                    "marionette": True,
                    "acceptInsecureCerts": True,
                    "pageLoadStrategy": "normal",
                    # uncomment to run in headless mode
                    # "goog:chromeOptions": {"extensions": [], "args": ["--headless"]},
                }
            }
        
        session = await asynchronous.get_session(driver_url, capabilities)

        driver_info = [driver_url, session]

        # Load the webpage
        await asynchronous.go_to_page(*driver_info, url)

        # Scroll down the page to load more poems
        while True:
            # Get the current height of the page
            last_height = await asynchronous.execute_script(*driver_info, "return document.body.scrollHeight")

            # Scroll down to the bottom of the page
            await asynchronous.execute_script(*driver_info, "window.scrollTo(0, document.body.scrollHeight);")

            # Wait for the page to load new poems
            time.sleep(2)

            # Calculate the new height of the page
            new_height = await asynchronous.execute_script(*driver_info, "return document.body.scrollHeight")

            # If the height hasn't changed, we've reached the end of the page
            if new_height == last_height:
                break

            # Otherwise, continue scrolling down the page
            last_height = new_height

        # Get the page source
        content = await asynchronous.get_page_source(*driver_info)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        # Extract all poems
        poems = soup.find_all("div", class_=lambda x: x and x.startswith("orig_"))

        # Create a new folder for today's results if it doesn't already exist
        today = datetime.today().strftime('%Y-%m-%d')
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
                text = text.split('\n')
                text = text[0] + '\n' + '\n'.join([line.lstrip() for line in text[1:]])

                file.write(text + "\n------------------------------------------------------------\n\n")

        # Close the browser
        synchronous.close_session(*driver_info)

        end = time.time()
        print(f"Time: {end-start:.2f} sec")

        # Wait an hour before running again
        time.sleep(60 * 60)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
