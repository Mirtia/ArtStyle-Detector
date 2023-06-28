import argparse

from google_crawler import GoogleCrawler
from image_upscaler import ImageUpscaler
from wikimedia_crawler import WikimediaCrawler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upscale", action="store_true", help="Enable upscaling")
    parser.add_argument("-c", "--crawl", action="store_true", help="Enable crawling")
    parser.add_argument("-f", "--file", dest="file", help="Specify input file", required=True)
    parser.add_argument("-o", "--output", dest="output", help="Specify output file", required=True)
    args = parser.parse_args()
    # Example parameters
    # --file input/wikimedia_input
    # --output output

    if args.crawl:
        crawler = WikimediaCrawler(args.output, args.file, "wikimedia")
        crawler.crawl_images()
    
    if args.upscale:
        upscaler = ImageUpscaler(args.output + "wikimedia")
        upscaler.upscale_images()


if __name__ == "__main__":
    main()
