import numpy as np

#   IMPORTANT NOTICE
#
#   This specific setup is credited to Dr. Michael J Garbade, as it was presented
#   on the webite kdnuggets.com.
#   
#   In order to adapt the script to work for the purposes of this project, training data
#   and test data values were modified. 
#
#   Source: https://www.kdnuggets.com/2018/10/simple-neural-network-python.html

class NeuralNetwork():
    
    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)
        
        #converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        #applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        #computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        
        #training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            #siphon the training data via  the neuron
            output = self.think(training_inputs)

            #computing error rate for back-propagation
            error = training_outputs - output
            
            #performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        #passing the inputs via the neuron to get output   
        #converting values to floats
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

while True:
    if __name__ == "__main__":

        #initializing the neuron class
        neural_network = NeuralNetwork()

        print("Beginning Randomly Generated Weights: ")
        print(neural_network.synaptic_weights)

        #training data consisting of 4 examples--3 input values and 1 output
        training_inputs = np.array([[0.732,0.585,0.524],
                                    [0.488,0.585,0.646],
                                    [0.646,0.695,0.622],
                                    [0.549,0.366,0.415],
                                    [0.61,0.512,0.5],
                                    [0.61,0.512,0.402],
                                    [0.366,0.402,0.488],
                                    [0.817,0.89,0.817],
                                    [0.683,0.5,0.671],
                                    [0.683,0.646,0.622],
                                    [0.256,0.207,0.317],
                                    [0.451,0.585,0.5],
                                    [0.5,0.402,0.512],
                                    [0.195,0.354,0.378],
                                    [0.463,0.256,0.244],
                                    [0.207,0.39,0.378],
                                    [0.305,0.427,0.354],
                                    [0.463,0.549,0.512],
                                    [0.22,0.122,0.341],
                                    [0.476,0.28,0.293],
                                    [0.622,0.537,0.5],
                                    [0.354,0.402,0.39],
                                    [0.671,0.817,0.744],
                                    [0.549,0.671,0.573],
                                    [0.598,0.683,0.622],
                                    [0.463,0.488,0.622],
                                    [0.671,0.512,0.524],
                                    [0.561,0.5,0.598],
                                    [0.39,0.537,0.451],
                                    [0.402,0.585,0.439]])

        training_outputs = np.array([[0.293, 0.671, 0.61, 0.585, 0.329, 0.293, 0.561, 0.707, 0.793, 0.512, 0.427, 0.537, 0.537, 0.573, 0.341, 0.354, 0.305, 0.585, 0.634, 0.256, 0.598, 0.329, 0.573, 0.585, 0.72, 0.585, 0.268, 0.524, 0.476, 0.439]]).T

        #training taking place
        neural_network.train(training_inputs, training_outputs, 250000)

        print("Ending Weights After Training: ")
        print(neural_network.synaptic_weights)

        user_input_one = str(input("Season One Win %: "))
        user_input_two = str(input("Season Two Win %: "))
        user_input_three = str(input("Season Three Win %: "))
        
        print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
        print("Projected Win %: ")
        print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
        print("Wow, we did it!")
