import asyncio
import os
import re

import aiohttp
import requests
from bs4 import BeautifulSoup

from crawler import Crawler


# The WikimediaCrawler class is a Python class that crawls images from Wikimedia Commons using asyncio
# and aiohttp libraries.
class WikimediaCrawler(Crawler):

    url = "https://commons.wikimedia.org/w/api.php"

    def __init__(self, input_file: str, output_dir: str, prefix: str):
        super().__init__(input_file, output_dir, prefix)
        self.session = requests.Session()
        self.read_input_file()
        self.sem = asyncio.Semaphore(10)

    def crawl_images(self):
        asyncio.run(self.__crawl_images_async())

    async def __crawl_images_async(self):
        """
        This is an asynchronous function that crawls images from Wikimedia Commons categories and
        downloads them.
        """
        tasks = []
        for category in self.categories:
            parameters = {
                "action": "query",
                "format": "json",
                "list": "categorymembers",
                "cmtitle": "Category:" + category,
                "cmlimit": "500",
                "cmtype": "file"
            }
            request = self.session.get(url=self.url, params=parameters)
            data = request.json()
            images = data["query"]["categorymembers"]
            category_output_dir = self.dir_exists(self.output_dir, category)

            for image in images:
                image_title = image["title"].replace(" ", "_")
                image_url = "https://commons.wikimedia.org/wiki/" + image_title
                # print("Log: Image url: ", image_url)
                # print("Log: Image title: ", image_title)
                task = self.download_image(image_url, re.sub(
                    r'[<>:"/\\|?*]', "", image_title).replace(" ", "_"), category_output_dir)
                tasks.append(task)
        await asyncio.gather(*tasks)

    def read_input_file(self):
        """
        This function reads the contents of an input file, splits it by newline character, and assigns
        the resulting list to the "categories" attribute of the object.
        """
        with open(self.input_file, mode="r", encoding="utf-8") as f:
            self.categories = f.read().split("\n")[:-1]

    async def download_image(self, url: str, title: str, output_dir: str):
        """
        This is an async function that downloads an image from a given URL and saves it to a specified
        output directory.
        
        :param url: The URL of the webpage containing the image to be downloaded
        :param title: The title of the image file that will be saved to the output directory
        :param output_dir: The directory where the downloaded image will be saved
        """
        output_file = os.path.join(output_dir, title)
        async with self.sem:
            async with aiohttp.ClientSession() as aio_session:
                try:

                    async with aio_session.get(url) as response:
                        if response.status == 200:
                            chunks = ""
                            while True:
                                chunk = await response.content.read(1024)
                                if not chunk:
                                    break
                                else:
                                    chunks += chunk.decode("utf-8")
                            # print(f"Log: HTML page downloaded successfully: {output_file}")
                            soup = BeautifulSoup(chunks, "html.parser")
                            image_url = soup.find("img")["src"]
                            # print(f"Log: Image url extracted from HTML page: {image_url}")
                        else:
                            print(f"Error: Failed to download HTML page from {url}. Status code: {response.status}")

                    async with aio_session.get(image_url) as response:
                        if response.status == 200:
                            with open(output_file, "wb") as file:
                                while True:
                                    chunk = await response.content.read(1024)
                                    if not chunk:
                                        break
                                    file.write(chunk)
                            # print(f"Log: Image downloaded successfully: {output_file}")
                        else:
                            print(f"Error: Failed to download image page from {image_url}. Status code: {response.status}")

                except Exception as e:
                    print(f"Error: Failed to download HTML page from {url}. Error: {e}")
