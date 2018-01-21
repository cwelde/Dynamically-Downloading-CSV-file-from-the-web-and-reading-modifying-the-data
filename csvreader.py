from urllib import request #to download from web
import pandas as pd #to access excel
import numpy as np #for using cosine on dataframe




hayes_url = 'http://rapid-hub.org/data/angles_UCI_CS.csv'

def download_csvfile(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    
    csv_str = csv.decode('utf-8')
    csv_str = csv_str.replace("\r\n", "\n")
    lines = csv_str

    dest_url = r'angles_UCI_CS.csv'

    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line)

    fx.close()
    

download_csvfile(hayes_url)

df = pd.read_csv('angles_UCI_CS.csv')

print('Printing before adding the third column')

print(df)

print('Printing after adding a third column with the computed cosine value')



df['angle_cosine'] = np.cos(df[' angle_degrees'])

print(df)





