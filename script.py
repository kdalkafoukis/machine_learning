#!/usr/bin/env python3.5

import requests
import html2text
import re

r = requests.get('https://google.com')

text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
text_maker.ignore_images = True

text = text_maker.handle(r.text)

splitted_text = text.split()
print(splitted_text)

final_text = []

for i in splitted_text:
    temp  = re.sub("[^A-Za-z]", "", i)
    if(temp!= ''):
        final_text.append(temp)

print(final_text)