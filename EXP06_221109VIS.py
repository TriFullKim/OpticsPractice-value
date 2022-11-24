import EXP06_221109 as val
import matplotlib.pyplot as plt

def horizontalMinMax(dataFrame):
    return dataFrame.min(), dataFrame.max()

def horizontalMinMax_IDX(dataFrame):
    return dataFrame.idxmin(), dataFrame.idxmax()

def horizontalCenter(dataFrame):
    MinMax = horizontalMinMax(dataFrame)
    return (MinMax[0]+MinMax[1])/2

degree = val.polarAngle

##########
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 01");plt.ylabel('Intensity');plt.xlabel('polarAngle[degree]')

plt.plot(degree, val.result_exp0601['IntensityMean'],'x-r',label='Measures',linewidth=0.8)
plt.plot(degree, val.result_exp0601['theoricalValue'],'x--b',label='TheoricalValue',linewidth=0.8)
plt.axhline(y=horizontalCenter(val.result_exp0601['IntensityMean']),color='b',linestyle='--',linewidth=0.6)

plt.grid(True)
plt.show()


##########
fig, axs = plt.subplots(2,sharex=True)
fig.suptitle("EXPERIENCE 02(lambda/2)")
fig.supylabel('Intensity');fig.supxlabel('polarAngle[degree]')

axs[0].plot(degree, val.result_exp0602_1['0degMEAN'],'x--r',linewidth=0.8)
axs[0].set_title("0[deg]")
index02_1=horizontalMinMax_IDX(val.result_exp0602_1['0degMEAN'])
axs[0].axhline(y=horizontalCenter(val.result_exp0602_1['0degMEAN']),color='r',linestyle='--',linewidth=0.6)
# axs[0].hlines(
#     y=(horizontalCenter(val.result_exp0602_1['0degMEAN'])),
#     xmin=index02_1[0], xmax=index02_1[1],
#     color='blue',linestyle='-',linewidth=0.8
# )

axs[1].plot(degree, val.result_exp0602_1['45degMEAN'],'x--b',linewidth=0.8)
axs[1].set_title("45[deg]")
index02_2=horizontalMinMax_IDX(val.result_exp0602_1['45degMEAN'])
axs[1].axhline(y=horizontalCenter(val.result_exp0602_1['45degMEAN']),color='b',linestyle='--',linewidth=0.6)
# axs[1].hlines(
#     y=(horizontalCenter(val.result_exp0602_1['45degMEAN'])),
#     xmin=index02_2[0], xmax=index02_2[1],
#     color='red',linestyle='-',linewidth=0.8
# )

for i in range(2):
    axs[i].grid(True)
plt.show()


##########
box1 = {'boxstyle': 'square',
        'ec': (0.5, 0.5, 1.0),
        'fc': (0.8, 0.8, 1.0),
        'linestyle': '-'}
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 03");plt.ylabel('Intensity');plt.xlabel('goniometerAngle[degree]')

plt.plot(val.result_exp0603.loc[10:57,'1차'].index,val.result_exp0603.loc[10:57,'1차'],'x--r',linewidth=0.8)
plt.plot(val.result_exp0603.loc[10:57,'2차'].index,val.result_exp0603.loc[10:57,'2차'],'x--b',linewidth=0.8)

exp0603_1_MIN = val.result_exp0603['1차'].min()
exp0603_1_MINDEX = val.result_exp0603['1차'].idxmin()
exp0603_2_MIN = val.result_exp0603['2차'].min()
exp0603_2_MINDEX = val.result_exp0603['2차'].idxmin()

plt.vlines(exp0603_1_MINDEX,exp0603_1_MIN-6,exp0603_1_MIN+6,'red','-','attempt 1',linewidth=1.1)
plt.vlines(exp0603_2_MINDEX,exp0603_2_MIN-6,exp0603_2_MIN+6,'blue','-','attempt 2',linewidth=1.1)
plt.text(50,exp0603_1_MIN+10,f'at {exp0603_1_MINDEX}[deg] and {exp0603_2_MINDEX}[deg]\ndetected mininum Intensity',bbox=box1)


plt.grid(True)
plt.show()


