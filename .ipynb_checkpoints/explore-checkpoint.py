import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_gt = pd.read_csv("ExportCSV.csv", sep=";")#2016 210
df_gt = df_gt[np.logical_not(pd.to_numeric(df_gt.LocationAbbr, errors='coerce').notnull())]
df_gt = df_gt.dropna(subset=['LocationAbbr'])   #Drop only if NaN in specific column (as asked in the question)

df2_gt = pd.read_csv("ExportCSV-2.csv", sep=";")
df2_gt = df2_gt.dropna(subset=['LocationAbbr'])
print("da rimuovere", set(df_gt.LocationAbbr).difference(set(df2_gt.LocationAbbr)))

gk2015 = pd.read_csv("GoogleKidney2015.csv",sep=",")#2015
g = (gk2015[1:])
g = g.convert_objects(convert_numeric=True)
g = g.sort_index()
google_values = [x[0] for x in g.values]

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

google_states = []
i = 0
for state in g.index:
    if list(states.values())[i] == state:
        google_states.append(list(states.keys())[i])
    i += 1

st = dict((y,x) for x, y in states.items())
index = list(g.index)
google_states = []
for state in st:
    if state in index:
        google_states.append(st[state])
print(len(google_states), len(google_values))
len(set(google_values).difference(set(google_states)))

# select the same states on the GT and the Google data (standardize)
df2_gt = df2_gt[df2_gt['LocationAbbr'].isin(google_states)]

# create a compact ground truth dataframe
df2_gt = pd.DataFrame(data=list(df2_gt.Data_Value), index=list(df2_gt.LocationAbbr), columns=['value'],
                      dtype=np.float)

google_df = pd.DataFrame(data=google_values, index=google_states, columns=['value'], dtype=np.float)

# normalizing
df2_gt = (df2_gt - df2_gt.mean())/df2_gt.std()
google_df = (google_df - google_df.mean())/google_df.std()

# order
df2_gt = df2_gt.sort_index()
google_df = google_df.sort_index()

ax = df2_gt.plot()
google_df.plot(ax=ax)

# google_df.plot()
# df2_gt.plot(color="red")
