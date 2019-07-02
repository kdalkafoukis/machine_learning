#!/usr/bin/env python3.7

# https://medium.com/@manivannan_data/get-browser-history-chrome-firefox-using-python-in-ubuntu-16-04-fb1c1f7ab546
# a bit edited for supporting modified home name
# needs to have chrome closed
# v0.1 helloworld - print the urls from existing query

import os
from pathlib import Path
import sqlite3

linux_chrome_file = str(Path.home())+'/.config/google-chrome/Default/History'

con = sqlite3.connect(linux_chrome_file)

c = con.cursor()
c.execute("select url, title, visit_count, last_visit_time from urls") #Change this to your prefered query
results = c.fetchall()
for r in results:
    print(r)