#!/bin/bash

# These urls are provided by https://github.com/asahi417/wikiart-image-dataset @asahi417
urls=(
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/abstract_expressionism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/abstract_expressionism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/ecole_de_paris.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/expressionism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/impressionism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/naive_art_primitivism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/neo_impressionism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/post_impressionism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/pre_raphaelite_brotherhood.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/realism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/rococo.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/romanticism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/surrealism.zip"
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/symbolism.zip"
 )

output_dir=$1
mkdir -p "${output_dir}"

 for url in "${urls[@]}"; do
    basename=$(basename "${url}")
    curl -O -L "${url}"
    unzip "${basename}" -d "${output_dir}"
    rm "${basename}"
done
