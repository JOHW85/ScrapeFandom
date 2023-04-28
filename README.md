# Scrape Fandom
Fandom.com provides Wiki dumps at https://*.fandom.com/wiki/Special:Statistics, but most of the dumps are outdated, and require contacting an admin to produce a new dump.

This script scrapes Fandom.com for an updated Wiki dump. It scrapes the Special:AllPages to get a list of article names and requests a wiki dump from Special:Export. Instructions to get a corpus for natural language processing and training is provided.

Works only for English fandom sites. Some slight modifications are needed for other languages.

# Notes
Will require the Chrome browser to be installed on the machine. The most up-to-date Chrome Driver will be handled by `webdriver-manager`.
The requirements.txt file should list all Python libraries that your notebooks depend on, and they will be installed using:

`pip install -r requirements.txt`

# Instructions
1. Clone the extractor locally (https://github.com/JOHW85/wikiextractor) with 
```git clone https://github.com/JOHW85/wikiextractor```
2. Open the terminal and cd  your way to the repo dir: `cd wikiextractor`
4. Run 
```python3 setup.py install```
5. Finally, run `run-me.sh FANDOM1 FANDOM2` in the terminal to get FANDOM1.jsonl and FANDOM2.jsonl in the directory.

Example
```run-me.sh harrypotter finalfantasy```
