import torch
from torch.autograd import Variable
from torch.autograd import grad
# import torch.autograd.numpy as np 
a = Variable(torch.Tensor([[1,2],[3,4]]), requires_grad=True)
print(a)
y = torch.sum(a**2)
y.backward() 
print(a.grad)
print(y)
print(a)