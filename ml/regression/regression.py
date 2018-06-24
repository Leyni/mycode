
# coding: utf-8

# In[14]:

from numpy import *

def createDataSet():
    dataMat = []
    labelMat = []
    for i in range(100):
        x1 = random.random() * 100
        x2 = random.random() * 100
        y = 5 * x1 + 7 * x2 + (random.random() - 0.5)
        dataMat.append([x1, x2])
        labelMat.append(y)
    return dataMat, labelMat

def loadDataSet(filename):
    numFeat = len(open(filename).readline().split('\t')) - 1 # 样本以\t分割，然后最有一个是目标值，因此-1
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[-1])) # 数值化
        dataMat.append(lineArr) # 增加到样本集中
        labelMat.append(float(curLine[-1])) # 数值化，并增加到目标值中
    return dataMat, labelMat

def standRegres(xArr, yArr):
    xMat = mat(xArr) # 样本矩阵 m*n
    yMat = mat(yArr).T # 目标值矩阵 m*1
    xTx = xMat.T * xMat # 计算通解的一部分 x.T * x，由于这部分需要求逆，因此需要先对这部分进行可逆性的判断
    if linalg.det(xTx) == 0.0: # 解释下：|A^(-1)|= |A|^(-1)，逆矩阵的行列式 = 矩阵的行列式的倒数，因此行列式等于0，则无法计算逆矩阵
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * yMat) # 计算 (x.T * x)^-1 * X.T * y 即完整的通解
    return ws


# In[15]:


# run
xArr, yArr = createDataSet()
ws = standRegres(xArr, yArr)
print ws


# In[39]:


# figure
"""
xMat = mat(xArr)
yMat = mat(yArr)
yHat = xMat * ws
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
xCopy = xMat.copy()
xCopy.sort(0)
yHat = xCopy * ws
ax.plot(xCopy[:,1], yHat)
plt.show()
"""

# In[40]:



from numpy import *

def lwlr(testPoint, xArr, yArr, k = 1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m))) # 初始化一个权重矩阵
    for j in range(m): # 对于每个样本
        diffMat = testPoint - xMat[j,:] # 计算该样本与预测点之间的差值向量
        weights[j, j] = exp(sqrt(diffMat * diffMat.T) / (longfloat(-2.0) * k ** 2)) # 计算样本x[j]所对应的权重
    print weights
    xTx = xMat.T * (weights * xMat) # 计算xTwX这部分，这部分下一步要求逆
    print linalg.det(xTx)
    if linalg.det(xTx) == 0.0: # 判断行列式是否为0，用于判断是否能够求逆
        print "This matrix is isingular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat)) # 计算 xTx^-1 * xT * (w * y) 即最终结果
    return testPoint * ws


# In[41]:


def lwlrTest(testArr, xArr, yArr, k = 1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat


# In[44]:


# run
import matplotlib.pyplot as plt
xArr, yArr = createDataSet()
yHat = lwlrTest(xArr, xArr, yArr, 0.1)
xMat = mat(xArr)
srtInd = xMat[:, 1].argsort(0)
xSort = xMat[srtInd][:,0,:]
fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(xSort[:,1], yHat[srtInd])
#ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s = 2, c = 'red')
#plt.show()


