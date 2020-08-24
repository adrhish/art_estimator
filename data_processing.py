import pandas as pd

data = pd.read_csv('paintings_df.csv')

def artist_cleaning(column_name):
    data.loc[:,column_name] = data[column_name].str.replace("\r\n ", "")
    return data

name = 'Friedrich Preller D A (1804-1878) Germany'

def get_country(name):
    return name.split(' ')[-1]

data['Country'] = data.artist.apply(get_country)

artist_cleaning('artist')