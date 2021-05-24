# Scrape Fandom
Fandom.com provides Wiki dumps at https://*.fandom.com/wiki/Special:Statistics, but most of the dumps are outdated, and require contacting an admin to produce a new dump.

This script scrapes Fandom.com for an updated Wiki dump. It scrapes the Special:AllPages to get a list of article names and requests a wiki dump from Special:Export.

Works only for English fandom sites. Some slight modifications are needed for other languages.

# Notes
The requirements.txt file should list all Python libraries that your notebooks depend on, and they will be installed using:

> pip install -r requirements.txt

# Usage
> python3 ScrapeFandom.py NAME_OF_FANDOM

For example, NAME_OF_FANDOM will be `harrypotter` for `https://harrypotter.fandom.com`

To subsequently extract the WikiDump, one can use the fork: https://github.com/ujiuji1259/wikiextractor/tree/fix_colon

Instructions from thaalesalves#8854 from NovelAI:
1. Clone the extractor locally (https://github.com/ujiuji1259/wikiextractor/tree/fix_colon)
2. Open the terminal and cd  your way to the repo dir
3. Run python3 setup.py install
4. After it finishes, you'll be able to use the extractor. Run wikiextractor fandom_name.xml --no-templates --json --o extracted_files
5. extracted_files folder will be created. cd into it and run the converter
6. python3 json2txt.py extracted_files/AA output_file.txt 
