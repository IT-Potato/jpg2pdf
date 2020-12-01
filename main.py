import os, datetime
from PIL import Image, ImageOps

images = os.listdir('./images')

def get_filename(img):
    return img.rsplit('.', 1)[0]

images.sort(key=get_filename)

cover = Image.open(os.path.join('./images', images[0])).convert('RGB')
cover = ImageOps.exif_transpose(cover)

processed_images = []
for index, img in enumerate(images, start=1):
    if index != 1:
        im = Image.open(os.path.join('./images', img)).convert('RGB')
        processed_images.append(ImageOps.exif_transpose(im))

cover.save(f'./pdf/{datetime.datetime.now().strftime("%m%d%Y%H%M%S")}.pdf', save_all=True, append_images=processed_images)