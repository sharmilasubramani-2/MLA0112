import math

# Activation function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network
class NeuralNetwork:
    def __init__(self):
        # Weights and biases (Input:2, Hidden:2, Output:1)
        self.w1 = [[0.5, 0.3], [0.2, 0.8]]  # Input -> Hidden
        self.w2 = [0.7, 0.4]                  # Hidden -> Output
        self.b1 = [0.1, 0.1]                  # Hidden bias
        self.b2 = 0.1                          # Output bias
        self.lr = 0.5                          # Learning rate

    def forward(self, inputs):
        # Hidden layer
        self.hidden = []
        for i in range(2):
            total = self.b1[i]
            for j in range(len(inputs)):
                total += inputs[j] * self.w1[i][j]
            self.hidden.append(sigmoid(total))

        # Output layer
        total = self.b2
        for i in range(2):
            total += self.hidden[i] * self.w2[i]
        self.output = sigmoid(total)
        return self.output

    def train(self, inputs, target):
        # Forward pass
        self.forward(inputs)

        # Output error
        output_error = target - self.output
        output_delta = output_error * sigmoid_derivative(self.output)

        # Hidden error
        hidden_delta = []
        for i in range(2):
            error = output_delta * self.w2[i]
            hidden_delta.append(error * sigmoid_derivative(self.hidden[i]))

        # Update weights Output->Hidden
        for i in range(2):
            self.w2[i] += self.lr * output_delta * self.hidden[i]
        self.b2 += self.lr * output_delta

        # Update weights Hidden->Input
        for i in range(2):
            for j in range(len(inputs)):
                self.w1[i][j] += self.lr * hidden_delta[i] * inputs[j]
            self.b1[i] += self.lr * hidden_delta[i]

# XOR dataset
data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

nn = NeuralNetwork()

print("Neural Network - XOR Problem")
print("=" * 40)
print("Training for 10000 epochs...")

for epoch in range(10000):
    for inputs, target in data:
        nn.train(inputs, target)

print("Training Complete!")
print("=" * 40)
print("Testing:")
for inputs, target in data:
    output = nn.forward(inputs)
    print(f"Input: {inputs} | Target: {target} | Output: {output:.4f} | Predicted: {round(output)}")