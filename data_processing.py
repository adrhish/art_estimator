iimport pandas as pd
pd.set_option('display.max_rows', n)

data_csv = pd.read_csv('paintings_df.csv')
data_csv

data = data_csv.copy()

# Cleaning

## Functions

def clean_artist(name):
    name = name.replace("\r\n ", "")
    name = name.replace("United States of America", "USA")
    name = name.replace("...", ".")
    return name

# getting country column
def get_country(name):
    splitted_name = name.split(' ')[-1]
    return splitted_name

# getting lifetime column
def get_lifetime(name):
    lifetime = name.split(' ')[-2]
    lifetime = lifetime.strip('()')
    return lifetime

# getting name column
def get_name(column):
    newlist= column.split(' ')[0:-2]
    #newlist= newlist.str.replace()
    return ' '.join(newlist).strip()

# getting birth date
def get_birthdate(date):
    splitdate= date.split('-')[0]
    return splitdate

data['artist'] = data.artist.apply(clean_artist)
data['country'] = data.artist.apply(get_country)
data['lifetime'] = data.artist.apply(get_lifetime)
data['name'] = data.artist.apply(get_name)
data['birth_year'] = data.lifetime.apply(get_birthdate)
