import os
import pandas as pd
import numpy as np
from datetime import datetime

path = 'Data/daily_data'
field = []
for one_file in list(os.listdir(path)):
    df = pd.read_csv(path + '/' + one_file)
    df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
    df = df[df['DATE'] > datetime(1990, 1, 1)]
    df.set_index(['DATE'], inplace=True)
    field.append(df)
tot_daily_df = pd.concat(field, axis=1, sort=False)
tot_daily_df.replace('.', np.nan, inplace=True)
tot_daily_df['GoldReturn'] = np.log(
    pd.to_numeric(tot_daily_df['GOLDAMGBD228NLBM']) / pd.to_numeric(tot_daily_df['GOLDAMGBD228NLBM'].shift(1)))
tot_daily_df['DCOILWTICOReturn'] = np.log(
    pd.to_numeric(tot_daily_df['DCOILWTICO']) / pd.to_numeric(tot_daily_df['DCOILWTICO'].shift(1)))
tot_daily_df['NASDAQ100Return'] = np.log(
    pd.to_numeric(tot_daily_df['NASDAQ100']) / pd.to_numeric(tot_daily_df['NASDAQ100'].shift(1)))
tot_daily_df['RU2000PRReturn'] = np.log(
    pd.to_numeric(tot_daily_df['RU2000PR']) / pd.to_numeric(tot_daily_df['RU2000PR'].shift(1)))
tot_daily_df['RU3000TRReturn'] = np.log(
    pd.to_numeric(tot_daily_df['RU3000TR']) / pd.to_numeric(tot_daily_df['RU2000PR'].shift(1)))
tot_daily_df.drop(['GOLDAMGBD228NLBM', 'NASDAQ100', 'RU2000PR', 'RU3000TR', 'DCOILWTICO'], axis=1, inplace=True)


path = 'Data/monthly_data'
field = []
for one_file in list(os.listdir(path)):
    df = pd.read_csv(path + '/' + one_file)
    df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
    df = df[df['DATE'] > datetime(1990, 1, 1)]
    df.set_index(['DATE'], inplace=True)
    field.append(df)
tot_monthly_df = pd.concat(field, axis=1, sort=False)
tot_monthly_df.replace('.', np.nan, inplace=True)
tot_monthly_df['BUSINVReturn'] = np.log(
    pd.to_numeric(tot_monthly_df['BUSINV']) / pd.to_numeric(tot_monthly_df['BUSINV'].shift(1)))
tot_monthly_df['CPIAUCSLReturn'] = np.log(
    pd.to_numeric(tot_monthly_df['CPIAUCSL']) / pd.to_numeric(tot_monthly_df['CPIAUCSL'].shift(1)))
tot_monthly_df.drop(['BUSINV', 'CPIAUCSL'], axis=1, inplace=True)

one_df = pd.concat([tot_daily_df, tot_monthly_df], axis=1, sort=False)
one_df.interpolate(inplace=True)
one_df.to_csv('Data/tot_daily_df_interpolate.csv')
