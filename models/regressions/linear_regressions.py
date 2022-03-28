import logging as log
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

from common.utils import is_mod_of_x

class PytorchLinearRegression:
    """
    Train the model using gradient descent

        1. Generate predictions
        2. Calculate the loss
        3. Compute gradients w.r.t the weights and biases
        4. Adjust the weights by subtracting a small quantity proportional to the gradient
        5. Reset the gradients to zero
    """

    loss_function = F.mse_loss
    def __init__(self,in_features, out_features, inputs, targets, batch_size=100):
        self._in_features = in_features
        self._out_features = out_features
        self.model = nn.Linear(in_features, out_features)
        self.data_set = TensorDataset(inputs, targets)  
        self.data_loader = DataLoader(self.data_set, batch_size, shuffle=True)
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=1e-5)

    def generate_predictions(self, inputs):
        return self.model(inputs)
    
    def train(self, num_epochs):

        for epoch in range(num_epochs):
            for xb, yb in self.data_loader:
                # generate predictions
                predictions = self.generate_predictions(xb)
                # Calculate Loss
                loss = self.loss_function(predictions, yb)
                # calcuate derivatives
                loss.backward()
                # update parameter context
                self.optimizer.step()

                # Reset Gradients
                self.optimizer.zero_grad()

                if is_mod_of_x(epoch, x=10):
                    log.info(f'Epoch:{epoch}, Loss: {loss.item()}')

class LinearRegression:
    pass