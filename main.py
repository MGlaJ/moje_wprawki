import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# #prawda - każda liczba większa od zera
# #fałsz - zero
# #range(a,b), generowane są liczby z zakresu [a,b)
#
# #tabliczka mnożenia
# # for i in range(6):
# #     for j in range(6):
# #         print(i, '*', j, '=', i*j)
#
# #adres ziennej, python traktuje wszystko jako obiekty
# # a = 5
# # b = a
# # print(id(a))
# # print(id(b))
#
# #a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #print(a[:]) #drukuje wszystkie elementy
# #print(a[::2]) #drukuje co drugi element
# #
# # a = np.array([1, 2, 3, 4])
# # b = np.array([[2, 3, 4, 5],[6, 7, 8, 9]])
# # print(a)
# # print(a.ndim)
# # print(a.shape)
# # print(b)
# # print(b.ndim)
# # print(b.shape)
#
# df = pd.read_csv('pokemon_data.csv')
# # print(df.columns)#nagłówki kolumn
# #print(df['Name'])#drukuje zadaną kolumnę
# #print(df['Name'][0:10])#drukuje pierwsze 10 rekordów z zadanej kolumny(bez 10.)[0,10)
# #print(df[['Name', 'Type 1', 'HP']][0:11])
# #print(df.iloc[1])#drukuje zadany wiersz lub wiersze
# #print(df.iloc[1:5])
# #print(df.iloc[2,1])#drukuje zadaną lokalizację
#
# # for index, row in df.iterrows():
# #     print(index, row['Name'])
#
# #print(df.loc[df['Type 1'] == 'Fire'])
#
# #print(df.describe())
#
# #print(df.sort_values('Name'))#kolejność rosnąca
# #print(df.sort_values('Name', ascending=False))#kolejność malejąca
#
# #print(df.sort_values(['Type 1', 'HP'], ascending=[0, 1]))#pierwsza kolumna rosnąco, druga malejąco
# #df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#
# #print(df.head(5))
# #df.drop(columns=['Total'])
#
# #print(df)
# df['Total'] = df.iloc[:,4:10].sum(axis=1)
# cols = list(df.columns.values)
# #df = df[['Total', 'HP', 'Defense']]#nowy porządek kolumn
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# #print(df.columns.values)
# #print(df['Total'])
# # df.to_csv('modified.csv', index=False)
# # df.to_excel('modified.xlsx', index=False)
# #df.to_csv('modified.txt', index=False, sep='\t')
#
# #print(df.loc[df['Type 1']=='Grass'])
# #print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')])
# #print(df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison')])
# #print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)])
# # new_df = df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)]
# # print(new_df)
# # #new_df = new_df.reset_index()
# # new_df = new_df.reset_index(drop=True)#jeżeli nie chcemy nowego dataframe'u, to trzeba dopisać inplace=True
# # print(new_df)
#
# #print(df.loc[df['Name'].str.contains('Mega')])
# #print(df.loc[~df['Name'].str.contains('Mega')])
# import re
# #regular expressions
# #print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])
# #print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
# #print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])
#
# #df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Ogień'
# ##df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
# #print(df)
#
# df = pd.read_csv('modified.csv')
# #print(df.groupby(['Type 1']).mean())
# #print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))
# #print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))
# #print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))
# #print(df.groupby(['Type 1']).sum())
# df['count'] = 1
# #print(df.groupby(['Type 1']).count()['count'])
# #print(df.groupby(['Type 1', 'Type 2']).count()['count'])
#
# new_df = pd.DataFrame(columns=df.columns)
# # for df in pd.read_csv('modified.csv', chunksize=5):
# #     print('CHUNK DF')
# #     print(df)
#
# for df in pd.read_csv('modified.csv', chunksize=5):
#     results = df.groupby(['Type 1']).count()
#
#     new_df = pd.concat([new_df, results])
#
#
# x = [0, 1, 2, 3, 4]
# y = [0, 2, 4, 6, 8]
# plt.figure(figsize=(5,3), dpi=300)
# plt.plot(x, y, 'b^--', label='2x')
# x2 = np.arange(0, 4.5, 0.5)
#
# plt.plot(x2[:6],x2[:6]**2,'r', label='x^2')
# plt.plot(x2[5:],x2[5:]**2, 'r--')
# plt.title('Our first graph', fontdict={'fontname':'Comic Sans MS', 'fontsize': 18})
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.xticks([1,2,3,4])
# #plt.yticks([1,2,3,4,5])
# plt.legend()
# plt.savefig('mygraph.png', dpi=300)
# plt.show()
#
# ##słupkowy
# labels = ['a', 'b', 'c']
# values = [1,4,2]
# bars = plt.bar(labels, values)
# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')
# plt.figure(figsize=(6,4))
# plt.show()
#
# gas = pd.read_csv('gas_prices.csv')
#
# #print(gas)
# plt.figure(figsize=(8,5))
# plt.title('Gas Prices Over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize':18,  })
#
# plt.plot(gas.Year, gas.USA, 'b.-', label='USA')
# plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
# plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')
# #
# # for country in gas:
# #     if country != 'Year':
# #         plt.plot(gas.Year, gas[country], marker='.', label='')
#
# plt.xticks(gas.Year[::3])
# plt.xlabel('Year')
# plt.ylabel('US Dollars')
# plt.legend()
# plt.show()
#
#fifa = pd.read_csv('fifa_data.csv')
# bins = [40,50,60,70,80,90,100]
# plt.hist(fifa.Overall, bins=bins)
# plt.xticks(bins)
# plt.ylabel('Number of players')
# plt.xlabel('Skill level')
# plt.title("Players' skill level")
# plt.show()

# ##kołowy
# fifa = pd.read_csv('fifa_data.csv')
# left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
# right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
# labels = ['Left', 'Right']
# colors = ['#abcdef', '#aabbcc']
# print(left)
# print(right)
# plt.pie([left, right], labels = labels, colors = colors, autopct='%.2f %%')
# plt.title('Foot Preference of FIFA Players')
# plt.show()
#

### kołowy2
fifa = pd.read_csv('fifa_data.csv')
fifa.Weight = [x.strip('lbs') if type(x)==str else x for x in fifa.Weight]
plt.style.use('ggplot')
#print(fifa.Weight[0])
light = fifa.loc[(fifa.Weight < '125')].count()[0]
medium_light = fifa.loc[(fifa.Weight >= '125') & (fifa.Weight < '150')].count()[0]
medium = fifa.loc[(fifa.Weight >= '150') & (fifa.Weight < '175')].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >= '175') & (fifa.Weight < '200')].count()[0]
heavy = fifa.loc[(fifa.Weight >= '200')].count()[0]
# print(light)
# print(medium_light)
# print(medium)
# print(medium_heavy)
# print(heavy)

weights = [light, medium_light, medium, medium_heavy, heavy]
labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
explode = (.4, .1, 0, 0, .4)
plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)
plt.title('Weight Distribution of FIFA Players')
plt.show()