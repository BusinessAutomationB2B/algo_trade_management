import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mpl20171012.csv", header = 1)
print(df)

df = pd.read_csv("mpl20171012.csv",skiprows=2, header=None,
                 names=['time','price','volume','value','condition'])


 


#### price_group= df.groupby(['price','volume'])

"""
price_group= df.groupby('price')    # or['price']
pg = price_group.size()
print("pg data type:")
print(type(pg))

volume_group= df.groupby('volume')    # or['price']
vg = volume_group.size()

print("***Print Price level by size***")
print(pg[1])

#print(pg[:,0]) # Error here

import matplotlib.pyplot as plt
x = [3.0,3.01,30.2,3.03,3.04,3.05,3.06,3.07,3.8]
x_pos = [i for i, _ in enumerate(x)]
y = [386,2084,1002,726,322,237,163,300,99]
# plt.bar(pg.iloc[:,0], pg.iloc[:,1])
plt.bar(x_pos,y)
plt.xticks(x_pos,x)
plt.show()

"""

# plt.hist(df['volume'],20,orientation='vertical' )
plt.hist(df['price'],16,orientation='vertical' )

plt.show()
