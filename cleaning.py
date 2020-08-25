
# Dropping columns that are irrelevant for the dataset --> drop title column?

data = data.drop("price_estimated", axis=1)
data = data.drop("lot_number", axis=1)

# Quantifying binary columns using LabelEncoder --> pretty much done/re-check

data["stamped"].value_counts()
data["signed"].value_counts()
data["with_premium"].value_counts()
data["img available"].value_counts()
data["inscribed"].value_counts()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(data['stamped'])
data['stamped'] = le.transform(data['stamped'])

le.fit(data['signed'])
data['signed'] = le.transform(data['signed'])

le.fit(data['with_premium'])
data['with_premium'] = le.transform(data['with_premium'])

le.fit(data['img available'])
data['img available'] = le.transform(data['img available'])

le.fit(data['inscribed'])
data['inscribed'] = le.transform(data['inscribed'])

# Strip the "size" column and create height and width columns --> not done yet 

def get_size(column):
    new_size = column.split(" ")[-4:]
    #new_size = new_size.strip('( )', "cm", "x")
    return new_size

data['new_size'] = data["size"].apply(get_size)
data['new_size'].astype(str)


#def artist_cleaning(column_name):
    #data.loc[:,column_name] = data[column_name].str.replace("\r\n ", "")
    #return data

def get_country(name):
    splitted_name = name.split(' ')[-4:]
    return splitted_name

#def get_lifetime(name):
    #lifetime = name.split(' ')[-2:]
    #lifetime = lifetime.strip('( )')
    #return lifetime

#def del_countryandlifetime(column):
    #newlist= column.split(' ')[0:-2]
    #return ' '.join(newlist)

#print(del_countryandlifetime(name))


# Cleaning the target variable: Auction Result -> needs FX conversion into one currency / eliminate EUR/US labels / convert to float o. string

data = data[data.auction_result != "Unsold"]
data = data.reset_index(drop=True)


# Drop artists below threshold
from matplotlib import pyplot as plt

dict_ = dict(data["artist"].value_counts())

for key in dict_:
    if dict_[key] < 6:
        dict_[key] = 'drop'

to_drop = []

for artist in dict_:
    if dict_[artist] == 'drop':
        to_drop.append(artist)

new_data = data[~data['artist'].isin(to_drop)]

# Distribution of Auction Houses to the number of paintings sold at their location --> same as above

