from PIL import Image
import pytesseract

file_path = "./4688102-4215c7aeed3806e2.png"
img = Image.open(file_path)
text = pytesseract.image_to_string(img,lang="chi_sim")
# text = pytesseract.image_to_string(img)
print("输出识别图片内容：",text)

# /Users/fangsu/Desktop/TestSelenium/spider/4688102-4215c7aeed3806e2.png