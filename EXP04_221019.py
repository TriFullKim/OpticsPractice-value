import pandas as pd
from math import cos, radians

def theoricalAngelCalculation(RawData=pd.DataFrame(),Angle=0):
    resultDF=pd.DataFrame(
        index=[f'1.0 theory({Angle}[deg])',f'0.2 theory({Angle}[deg])',f'0.1 theory({Angle}[deg])'],
        columns=RawData.columns.values
    )

    resultDF.loc[f'1.0 theory({Angle}[deg])':f'0.1 theory({Angle}[deg])', '0[deg]'] = (
        RawData.loc['1.0 mean':'0.1 mean', f'{Angle}[deg]']/cos(radians(Angle))
    ).values
    resultDF.loc[f'1.0 theory({Angle}[deg])':f'0.1 theory({Angle}[deg])', '30[deg]'] = (
        resultDF.loc[f'1.0 theory({Angle}[deg])':f'0.1 theory({Angle}[deg])', '0[deg]'] *cos(radians(30))
    ).values
    resultDF.loc[f'1.0 theory({Angle}[deg])':f'0.1 theory({Angle}[deg])', '60[deg]'] = (
        resultDF.loc[f'1.0 theory({Angle}[deg])':f'0.1 theory({Angle}[deg])', '0[deg]'] *cos(radians(60))
    ).values
    resultDF.loc[f'1.0 theory({Angle}[deg])':f'0.1 theory({Angle}[deg])', '85[deg]'] = (
        resultDF.loc[f'1.0 theory({Angle}[deg])':f'0.1 theory({Angle}[deg])', '0[deg]'] *cos(radians(85))
    ).values

    return resultDF


# GET_RAW
RAWDATA_00 = pd.read_csv('RAW_DATA\exp04\VALUE221019EXP04-01.csv')
exp04_01 = RAWDATA_00.iloc[:, 1:]
exp04_01.index = RAWDATA_00.iloc[:, 0]
# DATA_REFINE
trimDataEXP0401=pd.DataFrame()
trimDataEXP0401.loc[:, 'D_3cm'] = [10+i*3 for i in range(11)]
trimDataEXP0401.loc[:, 'LUX_3cm'] = exp04_01.loc[:, 'delta_3cm[lux]']
trimDataEXP0401.loc[:, 'D_3cm*LUX_3cm^2'] =exp04_01.loc[:, 'delta_3cm[lux]'] * trimDataEXP0401.loc[:, 'D_3cm']**2
trimDataEXP0401.loc[:, 'D_4cm'] = [10+i*4 for i in range(11)]
trimDataEXP0401.loc[:, 'LUX_4cm'] = exp04_01.loc[:, 'delta_4cm[lux]'] * trimDataEXP0401.loc[:, 'D_4cm']**2
trimDataEXP0401.loc[:, 'D_4cm*LUX_4cm^2'] =exp04_01.loc[:, 'delta_4cm[lux]'] * trimDataEXP0401.loc[:, 'D_4cm']**2
trimDataEXP0401.loc['MEAN',:]=trimDataEXP0401.mean(axis=0)
trimDataEXP0401.loc['STD',:]=trimDataEXP0401.std(axis=0)
# exp04_01.loc[:, '3cmResult'].describe()
# exp04_01.loc[:, '4cmResult'].describe()

print(exp04_01.columns)
print(exp04_01)

# GET_RAW
RAWDATA_01 = pd.read_csv('RAW_DATA\exp04\VALUE221019EXP04-02.csv')
exp0402 = RAWDATA_01.iloc[:, 1:] 
exp0402.index = RAWDATA_01.iloc[:, 0]
# DATA_REFINE_01 EXP VALUE
trimDataEXP0402 = pd.DataFrame(index=exp0402.index.values, columns=[ '0[deg]', '30[deg]', '60[deg]','85[deg]'])
trimDataEXP0402.iloc[:, :] = exp0402.values

trimDataEXP0402.loc['1.0 mean', :] = trimDataEXP0402.loc[1.0, :].mean()
trimDataEXP0402.loc['0.2 mean', :] = trimDataEXP0402.loc[0.2, :].mean()
trimDataEXP0402.loc['0.1 mean', :] = trimDataEXP0402.loc[0.1, :].mean()
# DATA_REFINE_02 THEORICAL VALUE 0[DEG]
theoricalValue=(
    theoricalAngelCalculation(trimDataEXP0402,Angle=0)+
    theoricalAngelCalculation(trimDataEXP0402,Angle=30).values+
    theoricalAngelCalculation(trimDataEXP0402,Angle=60).values+
    theoricalAngelCalculation(trimDataEXP0402,Angle=85).values
)/4
trimDataEXP0402.loc['1.0 theory', :] = theoricalValue.iloc[0,:]
trimDataEXP0402.loc['0.2 theory', :] = theoricalValue.iloc[1,:]
trimDataEXP0402.loc['0.1 theory', :] = theoricalValue.iloc[2,:]
# DATA_REFINE_03 ERROR VALUE
result=trimDataEXP0402.loc['1.0 mean':'0.1 theory',:]

error = (
    trimDataEXP0402.loc['1.0 mean':'0.1 mean','0[deg]':'85[deg]']
    - trimDataEXP0402.loc['1.0 theory':'0.1 theory','0[deg]':'85[deg]'].values
)

result.loc['1.0 error',:]=error.iloc[0,:]
result.loc['0.2 error',:]=error.iloc[1,:]
result.loc['0.1 error',:]=error.iloc[2,:]


# OutPut
result.iloc[[0,3],:].to_clipboard()
result.iloc[[1,4],:].to_clipboard()
result.iloc[[2,5],:].to_clipboard()