import numpy as np
import matplotlib.pylab as plt

#AND Logic
def AND(x1, x2):
    w1,w2,theta = 0.5,0.5,0.6
    a = x1*w1+x2*w2
    if a > theta:
        return 1
    else:
        return 0

#NAND Logic
def NAND(x1,x2):
    w1,w2,theta = -0.5,-0.5,-0.6
    a = x1*w1+x2*w2
    if a > theta:
        return 1
    else:
        return 0

#OR Logic
def OR(x1,x2):
    w1,w2,theta = 0.6,0.6,0.5
    a = x1*w1+x2*w2
    if a > theta:
        return 1
    else:
        return 0

#XOR Logic
def XOR(x1,x2):
    a = NAND(x1,x2)
    b = OR(x1,x2)
    return AND(a,b)

#Step function singval
def StepFunction(x):
    if x > 0:
        return 1
    else:
        return 0

#Step function array
def StepFunction2(x):
    y = x>0
    return y.astype(int)

#Plotting the Graph of Step Function
x = np.arange(-5.0,5.0,0.1)
y= StepFunction2(x)
plt.figure("Step Function")
plt.plot(x,y)
plt.ylim(-0.1,1.1)



#Plotting the Graph of Sigmoid Function
def Sigmoid(x):
    return 1/(1+np.exp(-x))
a = np.arange(-5.0,5.0,0.1)
b = Sigmoid(a)
plt.figure("Sigmoid Function")
plt.plot(a,b)
plt.ylim(-0.1,1.1)


#Plotting the Graph of ReLU Function
def ReLU(x):
    return np.maximum(0,x)
c = np.arange(-5.0,5.0,0.1)
d = ReLU(c)
plt.figure("ReLU Function")
plt.plot(c,d)
plt.ylim(-0.1,5.1)



plt.show()

x1 = int(input("x1 : "))
x2 = int(input("x2 : "))

print("AND:", AND(x1, x2))
print("NAND:", NAND(x1, x2))
print("OR:", OR(x1, x2))
print("XOR:", XOR(x1, x2))