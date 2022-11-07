import pandas as pd
rd_exp0501 = pd.read_csv('RAW_DATA/exp05/VALUE221102EXP0501.csv')
rd_exp0502 = pd.read_csv('RAW_DATA/exp05/VALUE221102EXP0502.csv')
rd_exp0503 = pd.read_csv('RAW_DATA/exp05/VALUE221102EXP0503.csv')
rd_exp0501 = rd_exp0501.set_index(keys=rd_exp0501.columns[0])
rd_exp0502 = rd_exp0502.set_index(keys=rd_exp0502.columns[0])
rd_exp0503 = rd_exp0503.set_index(keys=rd_exp0503.columns[0])
# rd_exp0501;rd_exp0502;rd_exp0503

# # EXP0501 ###################
# 90-abs(rd_exp0501.loc[:,'O'] - rd_exp0501.loc[:,'left'])
# 90-abs(rd_exp0501.loc[:,'O'] - rd_exp0501.loc[:,'right'])
# # EXP0502_result

# ##########################END

# EXP0502 ###################
trim_exp0502 = pd.DataFrame()
color0502=['yellow','green','blue','violet']
for i in range(4):
    trim_exp0502.loc[:,f'{color0502[i]}'] = rd_exp0502.loc[:,'O']-rd_exp0502.loc[:,f'{color0502[i]}']
# EXP0502_result
result_exp0502 = trim_exp0502
result_exp0502.loc['MEAN',:] = trim_exp0502.mean()
##########################END

# EXP0503 ###################
trim_exp0503 = pd.DataFrame()
color0503=['V','B','T','G','Y'];side0503=['r','l']
for i in range(5):
    trim_exp0503.loc[:,f'{color0503[i]}{side0503[0]}'] = rd_exp0503.loc[:,'O']-rd_exp0503.iloc[:,i+1]
for i in range(5):
    trim_exp0503.loc[:,f'{color0503[i]}{side0503[1]}'] = abs(rd_exp0503.loc[:,'O']-rd_exp0503.iloc[:,i+6])
# EXP0503_result
result_exp0503 = pd.DataFrame()
for i in range(5):
    result_exp0503.loc[:,f'MEAN_{color0503[i]}']=(trim_exp0503.loc[:,f'{color0503[i]}{side0503[0]}']+trim_exp0503.loc[:,f'{color0503[i]}{side0503[1]}'])/2
result_exp0503.loc['MEAN',:] = result_exp0503.mean()
##########################END
