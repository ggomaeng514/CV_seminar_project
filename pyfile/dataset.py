from torch. utils.data import Dataset , DataLoader
import cv2
import torch
import torchvision
from torchvision import transforms #이미지데이터 augmentation
import os
import glob

class Custom_dataset(Dataset):
  def __init__(self, root_path, mode, transform= None ):
    self.all_data  = sorted(glob.glob(os.path.join(root_path, mode, '*', '*')))
    self.transform=transform

  def __getitem__(self, index):
    if torch.is_tensor(index):
      index =index.tolist()
    
    #이미지 읽기
    data_path =self.all_data[index]
    image = cv2.imread(data_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #BGR -> RGB

    #Tramsform(augmentation)
    if self.transform is not None:
      augmentation =self.transform(image = image)
      image = augmentation['image']

    #label 만들어주기
    label=[]
    if 'dolphin' in data_path.split('/')[-2]:
      label = 0
    elif 'shark' in data_path.split('/')[-2]:
      label = 1
    else:
      label = 2
    
    return image, label
  

  def __len__(self):
    length = len(self.all_data)
    return length
