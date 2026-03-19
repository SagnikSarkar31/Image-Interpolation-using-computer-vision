# 🖼️ Image Interpolation using Computer Vision

This project demonstrates the implementation of **Bilinear and Bicubic Image Interpolation** from scratch using Python, along with a comparison to optimized OpenCV methods.

---

## 🚀 Features

- 🔹 Manual implementation of **Bilinear Interpolation**
- 🔹 Manual implementation of **Bicubic Interpolation**
- 🔹 Image resizing (upscaling)
- 🔹 Output image saving functionality
- 🔹 Comparison with OpenCV optimized interpolation

---

## 🧠 Concepts Covered

- Pixel coordinate mapping  
- Bilinear interpolation using 4 nearest pixels  
- Bicubic interpolation using 16 neighboring pixels  
- Trade-off between **image quality vs computation time**  
- Performance limitations of Python loops  

---

## ⚙️ Technologies Used

- Python  
- NumPy  
- OpenCV  

---


---

## 📊 Performance Comparison

| Method | Pixels Used | Quality | Speed |
|--------|------------|--------|------|
| Nearest Neighbor | 1 | Low | Fast |
| Bilinear | 4 | Medium | Moderate |
| Bicubic | 16 | High | Slow |
| OpenCV (Optimized) | - | High | Very Fast |

---

## ⚠️ Important Note

Manual implementations using Python loops are computationally expensive for large images.  
Bicubic interpolation, in particular, is significantly slower due to multiple pixel calculations and function calls.

For real-world applications, optimized libraries like OpenCV are recommended.

---

## ▶️ How to Run

```bash
pip install opencv-python numpy
python bilinear_interpolation.py
python bicubic.py
