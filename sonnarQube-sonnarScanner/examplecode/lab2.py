import matplotlib.pyplot as plt
import pandas as pd
import datetime
import io
import requests

if __name__ == '__main__':
    r = io.StringIO(requests.get('http://data.cs1656.org/top12cities.csv', verify=False).content.decode('utf-8'))
    df = pd.read_csv(r, sep=',', engine='python')
    for n in range(df['City'].count()):
