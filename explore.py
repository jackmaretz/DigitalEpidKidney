import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ExportCSV.csv",sep=";")#2016 210
df= df[np.logical_not(pd.to_numeric(df.LocationAbbr, errors='coerce').notnull())]

df = df.dropna(subset=['LocationAbbr'])   #Drop only if NaN in specific column (as asked in the question)
df2 = pd.read_csv("ExportCSV-2.csv",sep=";")
df2 = df2.dropna(subset=['LocationAbbr'])
print("da rimuovere",set(df.LocationAbbr).difference(set(df2.LocationAbbr)))



gk2015 = pd.read_csv("GoogleKidney2015.csv",sep=",")#2015
g = (gk2015[1:])
g = g.convert_objects(convert_numeric=True)
g =g.sort_index()
l =[x[0] for x in g.values]

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

s= []
i=0
for state in g.index:
    if list(states.values())[i] == state:
        s.append(list(states.keys())[i])
    i += 1

st = dict((y,x) for x,y in states.items())
s= []
for state in st:
    s.append(st[state])
print(len(s),len(l))
len(set(l).difference(set(s)))