import argparse
import collections
import csv
import json
import glob
import math
import os
import pandas as pd
import re
import requests
import string
import sys
import time
import xml

if __name__ == '__main__':
    url = input("Enter url:")
    # df = pd.read_json(url)
    # df.to_csv(r'C:\Users\YOUYANG ZHOU\Desktop\Data science 1656\project1-ruy16\output.csv',index=None,header=True)
    info = json.loads(requests.get(url,verify = False).content)
    result = 0
    for data in info['data']['stations']:
        result += data['num_bikes_available']
    print(result)