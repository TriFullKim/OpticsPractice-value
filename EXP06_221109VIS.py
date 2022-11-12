import EXP06_221109 as val
import matplotlib.pyplot as plt

degree = val.polarAngle

##########
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 01");plt.ylabel('intensity[lux]');plt.xlabel('angle[degree]')

plt.plot(degree, val.result_exp0601['luxMEAN'],'x-r',linewidth=0.8)
plt.plot(degree, val.result_exp0601['theoricalValue'],'x--b',linewidth=0.8)


plt.grid(True)
plt.show()


##########
fig, axs = plt.subplots(2,sharex=True)
fig.suptitle("EXPERIENCE 02(lambda/2)")
fig.supylabel('intensity[lux]');fig.supxlabel('angle[degree]')

axs[0].plot(degree, val.result_exp0602_1['0degMEAN'],'x--r',linewidth=0.8)
axs[0].set_title("0[deg]")
axs[1].plot(degree, val.result_exp0602_1['45degMEAN'],'x--b',linewidth=0.8)
axs[1].set_title("45[deg]")

for i in range(2):
    axs[i].grid(True)
plt.show()


##########
fig, axs = plt.subplots(3,2,sharex=True)
fig.suptitle("EXPERIENCE 02(lambda/4)")
fig.supylabel('intensity[lux]');fig.supxlabel('angle[degree]')

axs[0,0].plot(degree, val.result_exp0602_2['25degMEAN'],'x--r',linewidth=0.8)
axs[0,0].set_title("25[deg]")
axs[0,1].plot(degree, val.result_exp0602_2['55degMEAN'],'x--y',linewidth=0.8)
axs[0,1].set_title("55[deg]")
axs[1,0].plot(degree, val.result_exp0602_2['70degMEAN'],'x--c',linewidth=0.8)
axs[1,0].set_title("70[deg]")
axs[1,1].plot(degree, val.result_exp0602_2['85degMEAN'],'x--b',linewidth=0.8)
axs[1,1].set_title("85[deg]")
axs[2,0].plot(degree, val.result_exp0602_2['115degMEAN'],'x--g',linewidth=0.8)
axs[2,0].set_title("115[deg]")

for x in range(3):
    for y in range(2):
        axs[x,y].grid(True)
plt.show()


##########
box1 = {'boxstyle': 'square',
        'ec': (0.5, 0.5, 1.0),
        'fc': (0.8, 0.8, 1.0),
        'linestyle': '-'}
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 03");plt.ylabel('intensity[lux]');plt.xlabel('angle[degree]')

plt.plot(val.result_exp0603.index.values, val.result_exp0603['1차'],'x--r',linewidth=0.8)
plt.plot(val.result_exp0603.index.values, val.result_exp0603['2차'],'x--b',linewidth=0.8)

exp0603_1_MIN = val.result_exp0603['1차'].min()
exp0603_1_MINDEX = val.result_exp0603['1차'].idxmin()
exp0603_2_MIN = val.result_exp0603['2차'].min()
exp0603_2_MINDEX = val.result_exp0603['2차'].idxmin()

plt.vlines(exp0603_1_MINDEX,exp0603_1_MIN-6,exp0603_1_MIN+6,'red','-','attempt 1',linewidth=1.1)
plt.vlines(exp0603_2_MINDEX,exp0603_2_MIN-6,exp0603_2_MIN+6,'blue','-','attempt 2',linewidth=1.1)
plt.text(50,exp0603_1_MIN+10,f'at {exp0603_1_MINDEX}[deg] and {exp0603_2_MINDEX}[deg]\ndetected mininum intensity',bbox=box1)


plt.grid(True)
plt.show()


