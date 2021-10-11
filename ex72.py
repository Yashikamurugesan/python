import os
import zipfile
import requests
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import prep

if int(os.environ.get("MODERN_PANDAS_EPUB", 0)):
    headers = {
'Pragma': 'no-cache',
'Origin': 'http://www.transtats.bts.gov',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.8',
'Upgrade-Insecure-Requests': '1',
'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.'
'0.2564.116 Safari/537.36'),
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': ('text/html,application/xhtml+xml,application/xml;q=0.9,'
'image/webp,*/*;q=0.8'),
'Cache-Control': 'no-cache',
'Referer': ('http://www.transtats.bts.gov/DL_SelectFields.asp?Table'
'_ID=236&DB_Short_Name=On-Time'),
'Connection': 'keep-alive',
'DNT': '1', }
    with open('modern-1-url.txt', encoding='utf-8') as f:
        data = f.read().strip()
        os.makedirs('data', exist_ok=True)
        dest = "data/flights.csv.zip"
if not os.path.exists(dest):
    r = requests.post('http://www.transtats.bts.gov/DownLoad_Table.asp?Table_ID=236'
'&Has_Group=3&Is_Zipped=0',headers=headers, data=data, stream=True)
    with open("data/flights.csv.zip", 'wb') as f:
        for chunk in r.iter_content(chunk_size=102400):
            if chunk:
                f.write(chunk)
