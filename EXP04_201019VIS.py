import EXP04_221019 as val
import matplotlib.pyplot as plt
# 실험 1
'''
# 실험값 가시화
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 01")
plt.ylabel('[lux]')
# 실제거리를 나타내기
plt.xlabel('d(= 10 + n * delta_d )[cm]')
plt.plot(range(11), val.exp04_01.iloc[:, 0], label='delta_d = 3cm')
plt.plot(range(11), val.exp04_01.iloc[:, 1], label='delta_d = 4cm')
# 단계로만 나타내기
# plt.xlabel('n (at d = 10 + n * delta_d )')
# plt.plot(val.exp04_01.loc[:,'D_3[cm]'],val.exp04_01.iloc[:,0],label='delta_d = 3cm')
# plt.plot(val.exp04_01.loc[:,'D_4[cm]'],val.exp04_01.iloc[:,1],label='delta_d = 4cm')

# 선형성 가시화
plt.figure(figsize=(5, 5), layout='constrained')
# I(밝기)와 1/d^2의 선형성확인
plt.title("EXPERIENCE 01");plt.xlabel('1/d^2');plt.ylabel('[lux]')
plt.plot(1/(val.exp04_01.loc[:, 'D_3[cm]']**2), val.exp04_01.loc[:, 'delta_3cm[lux]'], label='delta_d = 3cm')
plt.plot(1/(val.exp04_01.loc[:, 'D_4[cm]']**2), val.exp04_01.loc[:, 'delta_4cm[lux]'], label='delta_d = 4cm')
# I*d^2가 상수임을 확인
# plt.title("EXPERIENCE 01");plt.xlabel('step');plt.ylabel('I*d^2')
# plt.plot(range(11),val.exp04_01.loc[:,'delta_3cm[lux]']*(val.exp04_01.loc[:,'D_3[cm]']**2),label='delta_d = 3cm')
# plt.plot(range(11),val.exp04_01.loc[:,'delta_4cm[lux]']*(val.exp04_01.loc[:,'D_4[cm]']**2),label='delta_d = 4cm')

#######################
plt.show()
'''



# 실험2
'''
plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 02");plt.xlabel('theta[degree]');plt.ylabel('sr[cd/m^2]')
plt.xlim(0,90);plt.ylim(0,150)
plt.xticks([i*10 for i in range(10)]);plt.yticks([i*10 for i in range(16)])

# plt.plot([0,30,60,85], val.result.iloc[0,:], label='mean(1.0[sr])', linestyle='',linewidth=0.6,marker='o',markersize=2)
# plt.plot([0,30,60,85], val.result.iloc[3,:], label='theorical_mean(1.0[sr])',linestyle='',linewidth=0.6,marker='x',markersize=4)
# plt.plot([0,30,60,85], val.result.iloc[1,:], label='mean(0.2[sr])',linestyle='',linewidth=0.6,marker='o',markersize=2)
# plt.plot([0,30,60,85], val.result.iloc[4,:], label='theorical_mean(0.2[sr])',linestyle='',linewidth=0.6,marker='x',markersize=4)
plt.plot([0,30,60,85], val.result.iloc[2,:], label='mean(0.1[sr])',linestyle='',linewidth=0.6,marker='o',markersize=2)
plt.plot([0,30,60,85], val.result.iloc[5,:], label='theorical_mean(0.1[sr])',linestyle='',linewidth=0.6,marker='x',markersize=4)

plt.show()'''
