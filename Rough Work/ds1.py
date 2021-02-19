import pandas as pd
k1 = [1,2,3]
k2 = ['b','v','m']

l1 = pd.Series(k1+k2)
d1 = {'Tiger':'India','Goat':'Pakistan','Dragon':'China'}
l2 = pd.Series(d1)
print(l2[0])
print(l2['Tiger'])

print(l2.iloc[2])
print(l2.loc['Goat'])
