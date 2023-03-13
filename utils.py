import numpy as np
import torch
from PIL import Image
import cv2 as cv
import os
import matplotlib.pyplot as plt



def getLabelValue(label):
    if label == "banana":
        return torch.LongTensor(np.array([0], dtype=np.int64))
    elif label == "book":
        return torch.LongTensor(np.array([1], dtype=np.int64))
    elif label == "bread":
        return torch.LongTensor(np.array([2], dtype=np.int64))
    elif label == "candy cane":
        return torch.LongTensor(np.array([3], dtype=np.int64))
    elif label == "candy corn":
        return torch.LongTensor(np.array([4], dtype=np.int64))
    elif label == "cannon":
        return torch.LongTensor(np.array([5], dtype=np.int64))
    elif label == "carrot":
        return torch.LongTensor(np.array([6], dtype=np.int64))
    elif label == "cheese":
        return torch.LongTensor(np.array([7], dtype=np.int64))
    elif label == "cherry":
        return torch.LongTensor(np.array([8], dtype=np.int64))
    elif label == "chest piece":
        return torch.LongTensor(np.array([9], dtype=np.int64))
    elif label == "clock":
        return torch.LongTensor(np.array([10], dtype=np.int64))
    elif label == "diamond":
        return torch.LongTensor(np.array([11], dtype=np.int64))
    elif label == "egg":
        return torch.LongTensor(np.array([12], dtype=np.int64))
    elif label == "fire":
        return torch.LongTensor(np.array([13], dtype=np.int64))
    elif label == "fish":
        return torch.LongTensor(np.array([14], dtype=np.int64))
    elif label == "frog":
        return torch.LongTensor(np.array([15], dtype=np.int64))
    elif label == "ghost":
        return torch.LongTensor(np.array([16], dtype=np.int64))
    elif label == "grapes":
        return torch.LongTensor(np.array([17], dtype=np.int64))
    elif label == "gun":
        return torch.LongTensor(np.array([18], dtype=np.int64))
    elif label == "hat":
        return torch.LongTensor(np.array([19], dtype=np.int64))
    elif label == "helmet":
        return torch.LongTensor(np.array([20], dtype=np.int64))
    elif label == "house":
        return torch.LongTensor(np.array([21], dtype=np.int64))
    elif label == "key":
        return torch.LongTensor(np.array([22], dtype=np.int64))
    elif label == "lemon":
        return torch.LongTensor(np.array([23], dtype=np.int64))
    elif label == "mushroom":
        return torch.LongTensor(np.array([24], dtype=np.int64))
    elif label == "necklace":
        return torch.LongTensor(np.array([25], dtype=np.int64))
    elif label == "pear":
        return torch.LongTensor(np.array([26], dtype=np.int64))
    elif label == "pepper":
        return torch.LongTensor(np.array([27], dtype=np.int64))
    elif label == "pie":
        return torch.LongTensor(np.array([28], dtype=np.int64))
    elif label == "piece of meat":
        return torch.LongTensor(np.array([29], dtype=np.int64))
    elif label == "pineapple":
        return torch.LongTensor(np.array([30], dtype=np.int64))
    elif label == "pretzel":
        return torch.LongTensor(np.array([31], dtype=np.int64))
    elif label == "pumpkin":
        return torch.LongTensor(np.array([32], dtype=np.int64))
    elif label == "rose":
        return torch.LongTensor(np.array([33], dtype=np.int64))
    elif label == "strawberry":
        return torch.LongTensor(np.array([34], dtype=np.int64))
    elif label == "treasure chest":
        return torch.LongTensor(np.array([35], dtype=np.int64))
    elif label == "watermelon":
        return torch.LongTensor(np.array([36], dtype=np.int64))
    elif label == "empty bottle":
        return torch.LongTensor(np.array([37], dtype=np.int64))
    elif label == "orange":
        return torch.LongTensor(np.array([38], dtype=np.int64))
    elif label == "crown":
        return torch.LongTensor(np.array([39], dtype=np.int64))
    else:
        print(label)
        c = input('new item')



        
class simmmoDataset:
    """Custom Dataset for loading UTKFace face images"""

    def __init__(self, img_files_dir, total_len, transform=None):

        self.img_files_dir = img_files_dir
        self.transform = transform
        self.total_len = total_len

    def __getitem__(self, index):
        
        files = os.listdir(self.img_files_dir)
        counter = index + 1
        for fl in files:
            im = os.listdir(os.path.join(self.img_files_dir, fl))
            if counter > len(im):
                counter = counter - len(im)
                continue
            label = fl
            img = Image.open(os.path.join(self.img_files_dir, fl, str(counter) + '.png'))
            if len(img.split()) == 4:
                r, g, b, a = img.split()
            elif len(img.split()) == 3:
                r, g, b = img.split()
            img = Image.merge("RGB", (r, g, b))
            

            break

        img = img.resize((224, 224), Image.ANTIALIAS)
        
        if self.transform is not None:
            img = self.transform(img)
        label = getLabelValue(label)
        return img, label

    def __len__(self):
        return self.total_len
