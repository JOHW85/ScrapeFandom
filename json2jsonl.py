# Modified from thaalesalves#8854 from NovelAI Discord
import json
import os
import re
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help='Directory with wiki json files')
parser.add_argument('output', help='Txt file output')
args = parser.parse_args()
# Remove URLs from the text field using regex
url_regex = r'&lt;a href="(.*?)"&gt;(.*?)&lt;/a&gt;'

# Get all directories in input_dir
directories = os.listdir(args.input_dir)
counter = 0
with open(args.output, 'w') as fout:
    for directory in tqdm(directories):
        for filename in tqdm(os.listdir(os.path.join(args.input_dir, directory)), desc="Processing "+directory):
            if not filename.startswith('wiki'):
                continue

            path = os.path.join(os.path.join(args.input_dir, directory), filename)
            with open(path, 'r') as fin:
                for line in fin:
                    data = json.loads(line)

                    # remove non-processed templates
                    if data['text'] == "":
                        continue
                    else:
                        # Output to JSON in "text" field
                        title = "#"+data['title']+"\n"
                        text = re.sub(url_regex, r'\2', data['text'])
                        text = re.sub(r'\(\s+', '(', text)
                        output_json = { "meta": data["url"],
                                        "text": title+text.replace('()', '').replace("\u00a0"," ").replace(" , ", ", ")
                                    }
                        counter += 1
                        fout.write(json.dumps(output_json) + '\n')
print(counter)
