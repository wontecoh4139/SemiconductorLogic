import numpy as np

#Matrix formation, dimension, shape
A = np.array([[1,2,3],[2,3,4]])
print(np.ndim(A))
print(np.shape(A))

B = np.array([1,2,3])
print(np.shape(B))
print("----------------------------------------")

#Neural Network with 3 layers with arbitrary weights and bias, sigmoid activation function
#two values of input x and output y
def give_network():
    network = {}
    network['W1'] = np.array([[1,2,3],[1,2,3]])
    network['W2'] = np.array([[1,2,3],[1,2,3],[1,2,3]])
    network['W3'] = np.array([[1,2],[1,2],[1,2]])

    network['b1'] = np.array([[1,2,3]])
    network['b2'] = np.array([[1,2,3]])
    network['b3'] = np.array([[1,2]])
    
    return network


def sigmoid(x):
    return 1/(1+np.exp(-x))

def identity_function(x):
    return x

def calculation(network, x):

    W1 = network['W1']
    W2 = network['W2']
    W3 = network['W3']

    b1 = network['b1']
    b2 = network['b2']
    b3 = network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)    
    a3 = np.dot(z2,W3) + b3
    y = identity_function(a3)

    return y

x = np.array([1,2])
Network = give_network()
y = calculation(Network, x)
print(y)
print("-----------------------------------------")

#Softmax function for probability computation, two input values

def softmax_function(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    y =  exp_x/sum_exp_x
    
    return y

print(softmax_function([1,2]))



