# How to install torch and torchvision on Windows 10

Worked as 4/1/21

## Find instructions

[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

Filter, do not use conda

## Which version of CUDA do I have?

`nvcc --version`

## pip install torch and torchvision

`pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html`




