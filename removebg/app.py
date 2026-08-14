from rembg import remove
from PIL import Image
import os

folder = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(folder, "resim.jpg")

girdi = Image.open(file)
sonuc = remove(girdi)
sonuc.save()