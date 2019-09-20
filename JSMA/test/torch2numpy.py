"""
pytorch相当于神经网络中的numpy，它是以tensor的形式表示
"""
import torch
import numpy as np

# convert numpy to tensor or vise versa
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)  # numpy转换为torch
tensor2array = torch_data.numpy()  # torch转换为numpy
print(
    '\nnumpy array:', np_data,
    '\ntorch tensor:', torch_data,
    '\ntensor to array:', tensor2array,
)