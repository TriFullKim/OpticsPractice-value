from math import radians, cos
import pandas as pd

rd_exp0601 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0601.csv')
rd_exp0602_1 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0602.1.csv')
rd_exp0602_2 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0602.2.csv')
rd_exp0603 = pd.read_csv('RAW_DATA/exp06/VALUE221102EXP0603.csv')

rd_exp0601 = rd_exp0601.set_index(keys=rd_exp0601.columns[0])
rd_exp0602_1 = rd_exp0602_1.set_index(keys=rd_exp0602_1.columns[0])
rd_exp0602_2 = rd_exp0602_2.set_index(keys=rd_exp0602_2.columns[0])
rd_exp0603 = rd_exp0603.set_index(keys=rd_exp0603.columns[0])


polarAngle = [i*10 for i in range(19)]
luxReferPoint = 3


# EXP0601 ###################
trim_exp0601 = pd.DataFrame()
trim_exp0601 = rd_exp0601 - luxReferPoint

trim_exp0601.loc[:, 'luxMEAN'] = trim_exp0601.mean(axis=1)
for degree in polarAngle:
    trim_exp0601.loc[degree, 'theoricalValue'] = trim_exp0601.loc[0, 'luxMEAN'] * cos(radians(degree)) ** 2
trim_exp0601.loc[:, 'ERROR'] = abs(trim_exp0601.loc[:, 'theoricalValue'] - trim_exp0601.loc[:, 'luxMEAN'])
# EXP0601_result ############
result_exp0601 = trim_exp0601.loc[:, 'luxMEAN':'ERROR']
# END #######################


angle0602_1 = ['0deg', '45deg']
# EXP0602_1 #################
trim_exp0602_1 = pd.DataFrame()
trim_exp0602_1 = rd_exp0602_1 - luxReferPoint
for degree in angle0602_1:
    trim_exp0602_1.loc[:, f'{degree}MEAN'] = trim_exp0602_1.loc[:,f'{degree}1':f'{degree}2'].mean(axis=1)
# EXP0602_1_result ############
result_exp0602_1 = trim_exp0602_1.loc[:,f'{angle0602_1[0]}MEAN':f'{angle0602_1[len(angle0602_1)-1]}MEAN']
# END #######################


angle0602_2 = ['25deg', '55deg', '70deg', '85deg', '115deg']
# EXP0602_2 #################
trim_exp0602_2 = pd.DataFrame()
trim_exp0602_2 = rd_exp0602_2 - luxReferPoint
for degree in angle0602_2:
    trim_exp0602_2.loc[:, f'{degree}MEAN'] = trim_exp0602_2.loc[:,f'{degree}1':f'{degree}2'].mean(axis=1)
# EXP0602_2_result ############
result_exp0602_2 = trim_exp0602_2.loc[:,f'{angle0602_2[0]}MEAN':f'{angle0602_2[len(angle0602_2)-1]}MEAN']
# END #######################


# EXP0603 #################
trim_exp0603 = pd.DataFrame()
trim_exp0603.loc[:,'MEAN'] = (rd_exp0603 - luxReferPoint).mean(axis=1)
# EXP0603_result ############
result_exp0603 = trim_exp0603
# END #######################
