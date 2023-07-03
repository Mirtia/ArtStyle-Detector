import argparse

from image_upscaler import ImageUpscaler
from wikimedia_crawler import WikimediaCrawler
from model import StyleModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upscale", action="store_true", help="Enable upscaling")
    parser.add_argument("-c", "--crawl", action="store_true", help="Enable crawling")
    parser.add_argument("-t", "--train", action="store_true", help="Train model")
    parser.add_argument("-i", "--input", dest="input", help="Specify input image to test model")
    parser.add_argument("-f", "--file", dest="file", help="Specify input file", required=True)
    parser.add_argument("-o", "--output", dest="output", help="Specify output file", required=True)
    args = parser.parse_args()

    if args.crawl:
        crawler = WikimediaCrawler(args.file, args.output, "wikimedia")
        crawler.crawl_images()
    
    if args.upscale:
        upscaler = ImageUpscaler(args.output + "wikimedia")
        upscaler.upscale_images()

    if args.train:
        model = StyleModel(args.file, args.output)
        model.train()

    if args.input:
        model = StyleModel(args.file, args.output)
        model.classify(args.input)

if __name__ == "__main__":
    main()
