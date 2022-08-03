import numpy as np
import matplotlib.pyplot as plt

N=5                                                          # 5 образов для каждого класса (5 точек для каждого)/ 5 dots for

x1=np.random.random(N)                                       #x1 случайное значение
x2=x1+[np.random.randint(10)/10 for i in range(N)]+0.1       #x1 + случайное отклонение +0,1(что-бы точка была точно выше прямой)
C1=[x1,x2]


x1=np.random.random(N)                                       #x1 случайное значение
x2=x1-[np.random.randint(10)/10 for i in range(N)]-0.1       #x1 - случайное отклонение -0,1(что-бы точка была точно ниже прямой)
C2=[x1,x2]


f=[0,1]                                                      #прямая под 45 градусов/straight line with 45 degree angle


w=np.array([-0.3,0.3])                                       #веса для нейрона/synaptic weights
for i in range(N):
    x=np.array([C2[0][i],C2[1][i]])
    y=np.dot(w,x)
    if y>=0:
        print("Class C1")
    else:
        print("Class C2")


plt.scatter(C1[0][:],C1[1][:],s=1,c='red')
plt.scatter(C2[0][:],C2[1][:],s=1,c='blue')
plt.plot(f)
plt.grid(True)
plt.show()