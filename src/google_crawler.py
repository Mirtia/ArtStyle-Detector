import os
import json
from dotenv import load_dotenv
from google_images_search import GoogleImagesSearch

from crawler import Crawler

# Unused
# The GoogleCrawler class is a subclass of Crawler that uses the Google Images Search API to crawl and
# download images based on input queries and search parameters. There is a limitation on the number of queries
# so I ended up crawling Wikimedia Commons.
class GoogleCrawler(Crawler):

    def __init__(self, output_dir, input_file, prefix, parameters_file):
        super().__init__(output_dir, input_file, prefix)
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.cx = os.getenv("CX")
        self.gis = GoogleImagesSearch(self.api_key, self.cx)
        self.read_input_file()
        self.read_search_parameters(self.file_exists(parameters_file))

    def crawl_images(self):
        """
        This function crawls images based on a list of queries, downloads and resizes them, and saves
        them to the specified directories.
        """
        for query in self.queries:
            self.search_parameters["q"] = query
            self.gis.search(search_params=self.search_parameters)
            query_dir = self.dir_exists(os.path.join(self.output_dir, query))
            for result in self.gis.results():
                print("Image url: ", result.url)
                result.download(query_dir)
                result.resize(1000, 1000)
                print("Image path: ", result.path)

    def read_input_file(self):
        """
        This function reads the contents of an input file and stores each line as a query in a list.
        """
        with open(self.input_file, mode="r", encoding="utf-8") as f:
            self.queries = f.read().split("\n")

    def read_search_parameters(self, parameters_file):
        """
        This function reads search parameters from a JSON file and stores them in an object attribute.
        
        :param parameters_file: The file path of the JSON file containing the search parameters
        """
        with open(parameters_file, mode="r", encoding="utf-8") as f:
            self.search_parameters = json.load(f)