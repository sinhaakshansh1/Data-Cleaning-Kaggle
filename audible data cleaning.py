import pandas as pd
import numpy as np
import re
audible = pd.read_csv("C:/Users/aksha/Downloads/audible_uncleaned.csv")
author_name_data = audible['author']

#eliminating first and second issue
def author_name_clean(name):
    author_name_data = re.sub(r'Writtenby:\s*', '', name)  # Remove "Writtenby:"
    formatted_name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', author_name_data) #insert space
    return formatted_name.strip()

author_name_data = author_name_data.apply(author_name_clean)
print(author_name_data)


#eliminating third and fourth issue
narrator_name_data = audible['narrator']
def narrator_name_clean(narr):
    narrator_name_data = re.sub(r'Narratedby:\s*', '', narr)  # Remove "Writtenby:"
    formatted_name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', narrator_name_data) #insert space
    return formatted_name.strip()


narrator_name_data = narrator_name_data.apply(narrator_name_clean)
print(narrator_name_data)

#eliminating fifth issue
time_data = audible['time']
time = pd.to_timedelta(time_data.str.replace('and ', '').str.replace('hrs','hr').str.replace('mins','min'),errors='coerce')
time =str(time)
time=time.replace('0 days', '')
time = time.strip()
print(time)

#eliminating sixth issue
stars_data = audible['stars']
new_star = stars_data.apply(lambda x: x.split(' out')[0]).replace('Not rated yet', np.nan).astype(np.float16)
new_rating = stars_data.replace('Not rated yet', '0 out of 0 stars0 rating').apply(lambda x:x.split('stars')[1].split()[0]).replace('0', 'No rating')
audible['stars'] = new_star
audible['rating'] = new_rating

print(new_star)
print(new_rating)

#eliminating seventh issue
price_data = audible['price']
price_data = int(price_data.replace(",", ""))
price_data = price_data.astype(float)
print(price_data)


audible.columns.values
audible = audible.loc[:,['name', 'author', 'narrator', 'time', 'releasedate', 'language',
       'stars', 'rating','price']]
audible.to_csv('audible_cleaned.csv', index=False)

