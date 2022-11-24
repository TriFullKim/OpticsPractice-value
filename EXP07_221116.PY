import pandas as pd
def copy(DataFrame=pd.DataFrame()):
    DataFrame.to_clipboard();

rd_exp0701 = pd.read_csv('RAW_DATA/exp07/VALUE221116EXP0701.csv')
rd_exp0702 = pd.read_csv('RAW_DATA/exp07/VALUE221116EXP0702.csv')
rd_exp0703 = pd.read_csv('RAW_DATA/exp07/VALUE221116EXP0703.csv')

rd_exp0701 = rd_exp0701.set_index(keys=rd_exp0701.columns[0])
rd_exp0702 = rd_exp0702.set_index(keys=rd_exp0702.columns[0])
rd_exp0703 = rd_exp0703.set_index(keys=rd_exp0703.columns[0])

trim_exp0701 = pd.DataFrame(columns=rd_exp0701.columns)
for index in sorted(set(rd_exp0701.index)):
    trim_exp0701.loc[index,:]=rd_exp0701.loc[index:index,:].mean()
result_exp0701 = pd.DataFrame()
for i in range(len(trim_exp0701.index)):
    for j in range(3):
        result_exp0701.loc[list(trim_exp0701.index)[i],j+1] = (trim_exp0701.iloc[i,2-j]+trim_exp0701.iloc[i,4+j])/2

copy(result_exp0701)


trim_exp0702 = pd.DataFrame(columns=rd_exp0702.columns)
for i in range(4):
    index = rd_exp0702.index[i*3]
    trim_exp0702.loc[f'{index}[{i+1}]',:] = rd_exp0702.iloc[i*3:(i+1)*3,:].mean()
result_exp0702 = pd.DataFrame()
for i in range(len(trim_exp0701.index)):
    for j in range(3):
        result_exp0702.loc[list(trim_exp0702.index)[i],j+1] = (trim_exp0702.iloc[i,3-j]+trim_exp0702.iloc[i,5+j])/2

copy(result_exp0702*10)



trim_exp0703 = pd.DataFrame(columns=rd_exp0703.columns)
for i in range(4):
    index = rd_exp0703.index[i*3]
    trim_exp0703.loc[f'{index}[{i+1}]',:] = rd_exp0703.iloc[i*3:(i+1)*3,:].mean()
result_exp0703 = pd.DataFrame()
for i in range(len(trim_exp0701.index)):
    for j in range(3):
        result_exp0703.loc[list(trim_exp0703.index)[i],j+1] = (trim_exp0703.iloc[i,3-j]+trim_exp0703.iloc[i,5+j])/2

copy(result_exp0703*10)



# UNIT [mm]
const_L=[800,835,890]
const_k=[1,2,3]
const_d1=[0.02,0.04,0.08,0.16]
const_d2=['0.04[1]','0.04[2]','0.08[3]','0.08[4]']
const_d3=['0.04[1]','0.04[2]','0.04[3]','0.04[4]']


lambda_RED=635/10**6







d_exp0701 = pd.DataFrame(columns=const_k)
for d in const_d1:
    for k in const_k:
        d_exp0701.loc[d,k] = const_L[0]*2*(k)*lambda_RED/(result_exp0701.loc[d,k]*10)
    d_exp0701.loc[d,'MEAN'] = d_exp0701.loc[d,:].mean()
copy(d_exp0701)

d_exp0702 = pd.DataFrame(columns=const_k)
for d in const_d2:
    for k in const_k:
        d_exp0702.loc[d,k] = const_L[2]*(k)*lambda_RED/(result_exp0702.loc[d,k]*10)
    d_exp0702.loc[d,'MEAN'] = d_exp0702.loc[d,:].mean()
copy(d_exp0702)   


d_exp0703 = pd.DataFrame(columns=const_k)
for d in const_d3:
    for k in const_k:
        d_exp0703.loc[d,k] = const_L[2]*(k)*lambda_RED/(result_exp0703.loc[d,k]*10)
    d_exp0703.loc[d,'MEAN'] = d_exp0703.loc[d,:].mean()
d_exp0703     
copy(d_exp0703)

