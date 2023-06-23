from google_crawler import GoogleCrawler
from wikimedia_crawler import WikimediaCrawler

def main():
    crawler = WikimediaCrawler("output", "input/wikimedia_input", "wikimedia")
    # crawler = GoogleCrawler("output", "input/google_input", "google", "parameters.json")
    crawler.crawl_images()

if __name__ == "__main__":
    main()