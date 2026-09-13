import urllib.request as urequest

from io import BytesIO
from PIL import Image as PImage, ImageDraw as PImageDraw, ImageFont as PImageFont


def show_object_predictions(img, predictions):
  font = PImageFont.load_default(12)
  dimg = img.copy()
  draw = PImageDraw.Draw(dimg)

  for obj in predictions:
    label = obj["label"]
    (x0, y0, x1, y1) = tuple(obj["box"].values())
    draw.rectangle((x0,y0,x1,y1),
                   outline=(10, 220, 10),
                   width=2)
    draw.rectangle((x0,y0-6,x0+6*len(label),y0+6), fill=(0,0,0,160))
    draw.text((x0,y0-6), label, font=font)

  return dimg


def image_from_url(url):
  with urequest.urlopen(url) as response:
    image_data = BytesIO(response.read())
    return PImage.open(image_data)
