# Artstyle Detector

To make an artstyle detector, I first had to find enough images for the training.
The following are the list of the sources I *used* or at least tried to use to gather a bunch of images.

## Google Images

The first approach may not always be the best (it's never). To crawl Google Images I had to use [Google API](https://console.cloud.google.com/apis/library), make a custom [Programmable Search engine](https://developers.google.com/custom-search) and also be under a limit of requests. I didn't look at it further but made a test run.

## Wikimedia

Example of wikimedia categories *Impressionist_paintings*. The way I crawled this was pretty stupid but honest (bs4s, asyncio classic). Why? I could try an approach using SPARQL queries at [Wikidata Query Service](https://query.wikidata.org/). I may implement it in the future.

## Wikiart

As the wikimedia images were not enough ?!, I tried another approach. I found Wikiart which seemed to have an adequate amount of images at first glance. Luckily, there was a [repository](https://github.com/asahi417/wikiart-image-dataset) working on this, so I downloaded the datasets by the links provided.

## Detecting style

To train the model I used [ImageAI](https://github.com/OlafenwaMoses/ImageAI/tree/master). After writing some functionalities to construct the directory structure, training was pretty straightforward.

I was not satisfied with the accuracy it achieved but it was probably because of the dataset similarities. I'll try to use more categories in the future.

Truth is, a painting can have multiple arstyles. I tested some pictures, as welll as some of my own, and the results were okayish, but with not high confidence most of the times.

## Objects prevalent in each style

Not yet implemented

## Palette extractor

I used [color-thief](https://github.com/fengsp/color-thief-py) to extract paletters and dominant colors from the images. I am still not sure what to do with this information but it was cool. I thought about organizing the images to clusters according to their palette range.
