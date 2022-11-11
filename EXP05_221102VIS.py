import EXP05_221102 as val
import matplotlib.pyplot as plt

val.color0502
angle0502 = list(val.result_exp0502.loc['MEAN',:])
n_prism = list(val.result_exp0502.loc['n_prism',:])

plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 02");plt.ylabel('n');plt.xlabel('angle of deviation[degree]')

plt.plot(angle0502, n_prism,'x--r')
for color,angle,prism in zip(val.color0502,angle0502,n_prism):
    if color == val.color0502[3]:
        break
    plt.annotate(color,(angle,prism),xytext=(angle+.03,prism-0.0006))
plt.annotate(val.color0502[3],(angle0502[3],n_prism[3]),xytext=(angle0502[3]-.18,n_prism[3]-.0002))
plt.show()

val.color0503
angle0503 = list(val.result_exp0503.loc['MEAN',:])
lambdaValue = list(val.result_exp0503.loc['lambda[mm]',:])

plt.figure(figsize=(5, 5), layout='constrained')
plt.title("EXPERIENCE 03");plt.ylabel('wavelength[nm]');plt.xlabel('angle[degree]')

plt.plot(angle0503, lambdaValue,'x--r')
for color,angle,wavelength in zip(val.color0503,angle0503,lambdaValue):
    plt.annotate(color,(angle,wavelength),xytext=(angle+.1,wavelength-5))
plt.show()