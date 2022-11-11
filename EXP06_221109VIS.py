import EXP06_221109 as val
import matplotlib.pyplot as plt

degree = val.polarAngle

##########
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 01");plt.ylabel('intensity[lux]');plt.xlabel('angle[degree]')

plt.plot(degree, val.result_exp0601['luxMEAN'],'x-r')
plt.plot(degree, val.result_exp0601['theoricalValue'],'x--b')

plt.show()


##########
fig, axs = plt.subplots(2,sharex=True)
fig.suptitle("EXPERIENCE 02(lambda/2)")
fig.supylabel('intensity[lux]');fig.supxlabel('angle[degree]')

axs[0].plot(degree, val.result_exp0602_1['0degMEAN'],'x--r')
axs[0].set_title("0[deg]")
axs[1].plot(degree, val.result_exp0602_1['45degMEAN'],'x--b')
axs[1].set_title("45[deg]")

plt.show()


##########
fig, axs = plt.subplots(3,2,sharex=True)
fig.suptitle("EXPERIENCE 02(lambda/4)")
fig.supylabel('intensity[lux]');fig.supxlabel('angle[degree]')

axs[0,0].plot(degree, val.result_exp0602_2['25degMEAN'],'x--r')
axs[0,0].set_title("25[deg]")
axs[0,1].plot(degree, val.result_exp0602_2['55degMEAN'],'x--y')
axs[0,1].set_title("55[deg]")
axs[1,0].plot(degree, val.result_exp0602_2['70degMEAN'],'x--c')
axs[1,0].set_title("70[deg]")
axs[1,1].plot(degree, val.result_exp0602_2['85degMEAN'],'x--b')
axs[1,1].set_title("85[deg]")
axs[2,0].plot(degree, val.result_exp0602_2['115degMEAN'],'x--g')
axs[2,0].set_title("115[deg]")

plt.show()


##########
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 03");plt.ylabel('intensity[lux]');plt.xlabel('angle[degree]')

# plt.plot(val.result_exp0603.index.values, val.result_exp0603.values,'x-r')

plt.show()

