import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        e_x = torch.exp(x - torch.max(x))
        return e_x / e_x.sum()


class Softmax_stable(nn.Module):
    def __init__(self):
        super(Softmax_stable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        e_x = torch.exp(x - c)
        return e_x / e_x.sum()


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

data = torch.Tensor([1, 2, 3])
softmax_stable = Softmax_stable()
output = softmax_stable(data)
print(output)
