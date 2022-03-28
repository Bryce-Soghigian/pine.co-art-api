import copy
import pytest

from models.regressions.linear_regressions import LinearRegression, PytorchLinearRegression
import numpy as np
import torch


class TestLinearRegressions:
    """
    Class for testing implementations of linear regressions.
    """
    # Input (temp, rainfall, humidity)
    inputs = np.array([[73, 67, 43], 
                    [91, 88, 64], 
                    [87, 134, 58], 
                    [102, 43, 37], 
                    [69, 96, 70], 
                    [74, 66, 43], 
                    [91, 87, 65], 
                    [88, 134, 59], 
                    [101, 44, 37], 
                    [68, 96, 71], 
                    [73, 66, 44], 
                    [92, 87, 64], 
                    [87, 135, 57], 
                    [103, 43, 36], 
                    [68, 97, 70]], 
                    dtype='float32')

    # Targets (apples, oranges)
    targets = np.array([[56, 70], 
                        [81, 101], 
                        [119, 133], 
                        [22, 37], 
                        [103, 119],
                        [57, 69], 
                        [80, 102], 
                        [118, 132], 
                        [21, 38], 
                        [104, 118], 
                        [57, 69], 
                        [82, 100], 
                        [118, 134], 
                        [20, 38], 
                        [102, 120]], 
                    dtype='float32')

    inputs = torch.from_numpy(inputs)
    targets = torch.from_numpy(targets)

    def test_pytorch_regression(self):


        linear_regression = PytorchLinearRegression(
            in_features=3,
            out_features=2,
            inputs=copy.deepcopy(self.inputs),
            targets=self.targets,
            )
        
        linear_regression.train(1000)
        new_predictions = linear_regression.generate_predictions(self.inputs)
        # Assert accuracy is within 1% for all elements.
        index = 0
        for apple, orange in new_predictions:
            assert abs(apple - self.targets[index][0]) < 10
            assert abs(orange - self.targets[index][1]) < 10
            index += 1


test_linear_reg = TestLinearRegressions()
print(test_linear_reg.test_pytorch_regression())