# 🖼️ Image Processing Project – Histogram, Filtering, Morphology & Segmentation

## 📋 Project Overview
This project explores fundamental image processing techniques including histogram analysis, noise filtering, contrast enhancement, morphological operations, and segmentation.  
The goal is to analyze, improve, and extract structures from images using both visual and quantitative evaluation.

## 🎯 Objectives
- Enhance images using Histogram Equalization and CLAHE  
- Add & remove noise (Salt & Pepper, Gaussian)  
- Apply filtering (Median, Gaussian, Bilateral)  
- Perform morphological operations (Erosion, Dilation, Opening, Closing, Top-hat)  
- Segment objects using Thresholding and Otsu  
- Evaluate results visually and quantitatively (PSNR, SSIM, histograms)

## 📊 Dataset
- Input images are located in the `data/` directory  
- Images include grayscale objects used for enhancement, filtering, and segmentation

## 🛠️ Methodology

### 1. Contrast Enhancement
- Histogram Equalization (HE)  
- CLAHE (local contrast enhancement)

### 2. Noise Addition & Filtering
- Added Salt & Pepper noise  
- Filtering methods: Median, Gaussian, Bilateral

### 3. Morphological Operations
- Erosion, Dilation, Opening, Closing, Top-hat

### 4. Segmentation
- Global Thresholding  
- Otsu Automatic Thresholding  
- Optional: Adaptive Thresholding

## 📈 Visual Results

### Full Processing Pipeline
- Original image → Noisy → Filtered → Morphology → Segmented  

### Histogram Comparison
- Overlay of original and segmented image histograms

## 📏 Quantitative Evaluation

| Metric | Value | Interpretation |
|--------|-------|----------------|
| PSNR   | 27.69 | Good reconstruction quality |
| SSIM   | 0.29  | Structure moderately preserved |

## 💡 Conclusion
The project demonstrates a complete workflow for improving and segmenting images.  
Contrast enhancement and filtering improve visual quality, morphological operations refine shapes, and segmentation extracts useful binary structures.  
Quantitative metrics (PSNR, SSIM) confirm the effectiveness of the processing pipeline.

## 💻 Technical Stack
- Python  
- OpenCV  
- NumPy  
- Matplotlib  
- Scikit-image  

## 📁 Project Structure
data/
results/ 
src/
README.md
├── data/
│
│
├── notebooks/  
│
├── results 
│ ├── histograms
│
│ ├── processed
│
├── utils.ipynb
│
└── requirements.txt


## ▶️ Installation
```bash
# Clone the repository
git clone https://github.com/your-username/image-processing-project.git
cd image-processing-project

# Install required packages
pip install opencv-python numpy matplotlib scikit-image

