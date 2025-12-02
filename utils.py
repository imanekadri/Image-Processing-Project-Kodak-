import cv2
import os 
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim


def list_images(folder):
    exts = ('.png', '.jpg', '.jpeg', '.bmp')
    return sorted([os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(exts)])



def read_images( path , gray = False ):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")
    
    if gray:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Convert BGR to RGB for matplotlib
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)




def show_image(img, title='' ):
    
    if img.ndim == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()


def add_salt_pepper_noise(img, p):  
    noisy = img.copy()
    rand = np.random.rand(*img.shape)
    
    noisy[rand < p/2] = 0        # Poivre
    noisy[rand > 1 - p/2] = 255  # Sel
    
    return noisy


def add_gaussian_noise(img, mean=0, sigma=10):
   
    noisy = img.copy().astype(np.float32)
    gauss = np.random.normal(mean, sigma, img.shape)
    noisy += gauss
    noisy = np.clip(noisy, 0, 255)  # garder les valeurs entre 0 et 255
    return noisy.astype(np.uint8)

def psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return float('inf')
    return 20 * np.log10(255.0 / np.sqrt(mse))




