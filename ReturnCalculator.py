
import pandas as pd
import numpy as np

def calre (file):
    df = pd.read_csv(file)
    df.replace('.',np.NaN,inplace=True)
    l = df.shape[0]
    replace = np.zeros(l)
    #calculate return
    for i in range(1,l):
        replace[i] = (float(df.iloc[i,1]) - float(df.iloc[i-1,1]))/float(df.iloc[i-1,1])
    #replace
    df.iloc[:,1]=replace
    #drop first row
    df.drop([0],inplace=True)
    #write to excel
    df.to_csv("R_"+file,index=False)
    print('done')

files = ['NASDAQ100.csv','NASDAQCOM.csv','RU1000TR.csv','RU2000TR.csv','RU3000TR.csv']
for file in files:
    calre(file)
