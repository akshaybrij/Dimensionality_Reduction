import numpy as np
import matplotlib.pyplot as plt
q=np.array([0,0,0])
m=np.array([[1,0,0],[0,1,0],[0,0,1]])
f=np.random.multivariate_normal(q,m,20).T
#print f
q2=np.array([1,1,1])
m2=np.array([[1,0,0],[0,1,0],[0,0,1]])
f2=np.random.multivariate_normal(q,m,20).T
cla=np.concatenate((f,f2),axis=1)
mean_x=np.mean(cla[0,:])
mean_y=np.mean(cla[1,:])
mean_z=np.mean(cla[2,:])
j=np.cov([cla[0,:],cla[1,:],cla[2,:]])
eigv,eig_vec=np.linalg.eig(j)
print eig_vec[0][0]
x=[(eigv[i], eig_vec[i]) for i in range(len(eigv))]
print x
x.sort()
x.reverse()
mt=np.hstack((x[0][1].reshape(3,1),x[1][1].reshape(3,1)))
print mt.shape
k=mt.T.dot(cla)
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.scatter(k[0],k[1],color="green")
plt.show()
