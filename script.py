#!/usr/bin/env python3.5

import requests
import html2text

r = requests.get('https://google.com')

text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
text_maker.ignore_images = True

text = text_maker.handle(r.text)

print(text.split( ))