# 🖼️ Image Blur and Edge Detection

A Python project to apply **image blurring** and **edge detection** filters to images using the **Pillow (PIL)** library. This tool allows you to download images from URLs, apply filters, and save the results with timestamped filenames.

---

## 📌 Features

- ✅ Download image from a URL
- ✅ Save original image with a timestamp
- ✅ Apply various **blurring filters** (e.g., Gaussian Blur, Box Blur)
- ✅ Apply **edge detection**
- ✅ Save processed images in separate folders

---

## 📁 Folder Structure
```
Image_blur_and_edge_detection/
├── image_blur_and_edge-detection.py # main program/code
├── README.md #Read me file 
├── LICSENSE #MIT LICSENSE
├── original_images #stores downloaded images from url
└── out_images/
    ├── blur_images # processed blurred images
    └── edge_images # processed edge_detected images
```

---

## ⚙️ Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)
---
### ✅ Install dependencies:

```bash
pip install Pillow
```
---
### 🚀 How to Use
**1. Clone the repository:**
```
   git clone https://github.com/SatyamPrakash09/Image_blur_and_edge_detection.git
   cd Image_blur_and_edge_detection
```

**2. Run the script:**
```
   python image_blur_and_edge-detection.py
```
3. Enter the URL of the image when prompted.

**The script will automatically:**
- Save the original image in 'original_images/'
- Apply filters
- Save blurred and edge-detected versions in separate folders
---
## 🧠 Concepts Used
- PIL.Image for image processing
- ImageFilter for built-in filters like GaussianBlur, EDGE_ENHANCE
- datetime for timestamping saved images
- os for creating output folders
- requests and BytesIO for downloading and handling image streams
---
## Input &  Output
  **Original image is saved in original_images folder and Output is saved in two folders separately named blur_images and edge_images**
  
| Original                           | Blurred                          | Edge Detected              |
| ---------------------------------- | -------------------------------- | -------------------------- |

---

## ✍️ Author
Satyam Prakash

**📧 [Gmail](satyamprakash996@gmail.com)**

**[🔗 GitHub Profile](https://github.com/SatyamPrakash09)**

---

# 📜 License
This project is licensed under the MIT License.

Feel free to use, modify, and distribute it!

---
# ⭐ Star the repo
If you find this project useful, give it a ⭐ on GitHub to show support!
```

---

### ✅ What to do next:
- Save this as `README.md` in the root of your repo.
- Add sample images (optional but makes your project look polished).
- If you use OpenCV too, I can modify the README to reflect that.

Would you like me to auto-generate example screenshots with filters applied for a better showcase section?
```
---
