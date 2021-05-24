# Modified from thaalesalves#8854 from NovelAI Discord
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help='Directory with wiki json files')
parser.add_argument('output', help='Txt file output')
args = parser.parse_args()

for filename in os.listdir(args.input_dir):
    if not filename.startswith('wiki'):
        continue

    path = os.path.join(args.input_dir, filename)
    with open(path, 'r') as fin, open(args.output, 'a') as fout:
        for line in fin:
            data = json.loads(line)

            # remove non-processed templates
            if data['text'] == "":
                continue
            else:
                text = data['text'].replace('()', '')
                fout.write(text)
                fout.write('<|endoftext|>\n')
