import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('COVID19_line_list_data.csv')

dataset['sum'] = '1'

sorted_by_country = dataset.groupby(['gender']).sum().reset_index()

colors = ['pink','lightblue']

#Pi chart for male female cases 
plt.pie(sorted_by_country['sum'], labels=sorted_by_country['gender'], colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()



#Pi chart for the countries from where corona is mostly transmited from wuhann
country_sort = dataset.groupby(['country']).sum().reset_index()
wuhan_case = country_sort[country_sort['visiting Wuhan'] != 0]

x = wuhan_case['country']
y = wuhan_case['visiting Wuhan']
porcent = 100.*y/y.sum()

patches, texts = plt.pie(y,  startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))

plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

plt.show()

#top 10 countries with corona cases confirmed

dataset_1 = pd.read_csv('covid_19_data.csv')
total_country = dataset_1.groupby(['Country/Region']).sum().reset_index().sort_values('Confirmed',ascending = False).reset_index(drop = True)
total_country_1 = total_country.head(10)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
ax.bar(total_country_1['Country/Region'],total_country_1['Confirmed'])
plt.show()

#top 10 countries with corona cases death
total_country_death = dataset_1.groupby(['Country/Region']).sum().reset_index().sort_values('Deaths',ascending = False).reset_index(drop = True)
total_country_death_1 = total_country_death.head(10)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
ax.bar(total_country_death_1['Country/Region'],total_country_death_1['Deaths'])
plt.show()

#top 10 countries with corona cases recovered
total_country_rec = dataset_1.groupby(['Country/Region']).sum().reset_index().sort_values('Recovered',ascending = False).reset_index(drop = True)
total_country_rec_1 = total_country_rec.head(10)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
ax.bar(total_country_rec_1['Country/Region'],total_country_rec_1['Recovered'])
plt.show()


