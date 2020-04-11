# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)



# --------------
#Code starts here

data['Better_Event'] = np.where((data['Total_Summer'] > data['Total_Winter']),'Summer','Winter')
 
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])

better_event = data['Better_Event'].value_counts().idxmax()
 
print(better_event)



# --------------
#Code starts here
top_countries = data.loc[:,['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.iloc[:-1,:]
def top_ten(top_countries,cols):
    country_list=[]
    country_list=(top_countries.nlargest(10,cols)['Country_Name']).tolist()
    return country_list
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common=[]
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
# new list 'common' that stores the common elements between the three lists('top_10_summer', 'top_10_winter' and 'top_10')
print(common)



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
 
winter_df = data[data['Country_Name'].isin(top_10_winter)]
 
top_df = data[data['Country_Name'].isin(top_10)]
 
summer_df.plot(x='Country_Name',y='Total_Summer',kind='bar')
 
winter_df.plot(x='Country_Name',y='Total_Winter',kind='bar')

top_df.plot(x='Country_Name',y='Total_Medals',kind='bar')
 



# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer'] / summer_df['Total_Summer']
 
summer_max_ratio=summer_df['Golden_Ratio'].max()
print(summer_max_ratio)
summer_country_gold=str((summer_df[summer_df['Golden_Ratio']==summer_max_ratio]).loc[:,'Country_Name'].tolist()[0])
print(summer_country_gold)
 
winter_df['Golden_Ratio']=winter_df['Gold_Winter'] / winter_df['Total_Winter']
 
winter_max_ratio=winter_df['Golden_Ratio'].max()
print(winter_max_ratio)
winter_country_gold=str((winter_df[winter_df['Golden_Ratio']==winter_max_ratio]).loc[:,'Country_Name'].tolist()[0])
print(winter_country_gold)
 
top_df['Golden_Ratio']=top_df['Gold_Total'] / top_df['Total_Medals']
 
top_max_ratio=top_df['Golden_Ratio'].max()
print(top_max_ratio)
top_country_gold=str((top_df[top_df['Golden_Ratio']==top_max_ratio]).loc[:,'Country_Name'].tolist()[0])
print(top_country_gold)



# --------------
#Code starts here
data_1=data.iloc[:-1,:]
 
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data['Bronze_Total']*1
 
most_points=data_1['Total_Points'].max()
d=data_1[data_1['Total_Points']==most_points]
best_country=d['Country_Name'].tolist()[0]
 
print(most_points)
print(best_country)




# --------------
#Code starts here

best=data[data['Country_Name']==best_country]
 
best=best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



