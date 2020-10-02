import numpy as np
def sig(x):
    return 1/(1+np.exp(-x))

def dsig(x):
    return x*(1-x)


training_inputs = np.array([[0, 0, 1],
                           [1, 1, 1],
                           [1, 0, 1],
                           [0, 1, 1]])
training_outputs = np.array([[0, 1, 1, 0]]).T
np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

print("Random starting synaptic_weights: ", synaptic_weights)

for element in range(10000):
    input_layer = training_inputs
    outputs = sig(np.dot(input_layer, synaptic_weights))
    error = training_outputs - outputs
    adjustments = error * dsig(outputs)
    synaptic_weights += np.dot(input_layer.T, adjustments)

print("Synaptic weights after training: ")
print(synaptic_weights)

print("Outputs after training: ")
print(outputs)