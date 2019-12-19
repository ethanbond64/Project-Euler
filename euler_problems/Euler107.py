import pandas as pd
import numpy as np

df = pd.read_csv('p107_network.csv',header=None)
for i in range(100):
    # print(df.max())
    print(i)
    print(df.max().idxmax())
    print(df.max().max())
    maxes = df.max()
    maxx = maxes.max()
    # print('size',maxes[maxes == maxx].index.size)
    if maxes[maxes == maxx].index.size > 2:
        # print('triggered')
        for k in range(maxes[maxes == maxx].index.size):
            for j in range(maxes[maxes == maxx].index.size):
                # print(j,k)
                a = maxes[maxes == maxx].index[j]
                b = maxes[maxes == maxx].index[k]
                if df[a][b] == str(int(maxx)):
                    df[a][b] = '-'
                    # print('bing')
                if df[b][a] == str(int(maxx)):
                    df[b][a] = '-'
                    # print('bing')

    elif maxes[maxes == maxx].index.size == 2:
        a = maxes[maxes == maxx].index[0]
        b = maxes[maxes == maxx].index[1]
        df[a][b] = '-'
        df[b][a] = '-'
    else:
        print('What the fuck')
        print(df.max().idxmax())
        print(df.max().max())
print(df)
