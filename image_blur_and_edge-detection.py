from PIL import Image, ImageFilter
from io import BytesIO
import requests
import os
from urllib.parse import urlparse, unquote
import ntpath
# import random
from datetime import datetime

image_url = input("Enter url of image: ")
response = requests.get(image_url , allow_redirects = True)
if response.status_code != 200:
    raise Exception(f"Failed to download image: {response.status_code}")
os.makedirs("out_images/edge_images", exist_ok = True)
os.makedirs("out_images/blur_images", exist_ok = True)
os.makedirs("original_images", exist_ok = True)

parsed_url = urlparse(image_url)
filename = ntpath.basename(parsed_url.path)
filename = unquote(filename)
base_name, ext = os.path.splitext(filename)
time_stamp = datetime.now().strftime("%d-%B-%Y, %I:%M:%S %p")
safe_stamp = time_stamp.translate(str.maketrans({':':'-', '/':'-'}))

if not ext :
    ext = ".jpg"

before = Image.open(BytesIO(response.content))
before.save(f"original_images/{base_name}({safe_stamp}).jpg")
after = before.filter(ImageFilter.FIND_EDGES)
blur = before.filter(ImageFilter.BoxBlur(10))
after.save(f"out_images/edge_images/{base_name}-(edges)-({safe_stamp}).jpg")
blur.save(f"out_images/blur_images/{base_name}-(blur)-({safe_stamp}).jpg")
print(f"image processed succesfully")
