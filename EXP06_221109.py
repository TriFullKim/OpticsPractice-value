from math import radians,cos
import pandas as pd
rd_exp0601 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0601.csv')
rd_exp0602_1 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0602.1.csv')
rd_exp0602_2 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0602.2.csv')
rd_exp0603 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0603.csv')

rd_exp0601 = rd_exp0601.set_index(keys=rd_exp0601.columns[0])
rd_exp0602_1 = rd_exp0602_1.set_index(keys=rd_exp0602_1.columns[0])
rd_exp0602_2 = rd_exp0602_2.set_index(keys=rd_exp0602_2.columns[0])
rd_exp0603 = rd_exp0603.set_index(keys=rd_exp0603.columns[0])

polarAngle=[i*10 for i in range(19)]

trim_exp0601 = pd.DataFrame()
trim_exp0601=rd_exp0601
trim_exp0601.loc[:,'MEAN'] = rd_exp0601.mean(axis=1)
for polarAngle in polarAngle:
    trim_exp0601.loc[polarAngle,'theoricalValue'] = trim_exp0601.loc[0,'MEAN'] * cos(radians(polarAngle)) * cos(radians(polarAngle))
trim
for i in range(2):
    trim_exp0601.loc[]
angle0602_1 = [0,45]
angle0602_2 = [25,55,70,85,115]


