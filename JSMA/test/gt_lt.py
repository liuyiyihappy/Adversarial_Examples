"""
pytorch相当于神经网络中的numpy，它是以tensor的形式表示
"""
import torch
import numpy as np

a = torch.Tensor([[1, 2], [3, 4]])
b = torch.Tensor([[1, 1], [4, 4]])
result1 = torch.gt(a, b).byte()
result2 = torch.lt(a, b).byte()

print(result1)
print(result2)