import argparse
import src.scrapefandom as scrapefandom


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_fandom', help='Fandom\'s name')
    args = parser.parse_args()
    fandom_site = args.input_fandom
    scrapefandom.scrape(fandom_site)
