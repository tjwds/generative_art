def generate_art():
    from PIL import Image, ImageDraw
    import random

    img = Image.open('sample.jpg')
    img = img.convert('RGBA')
    width, height = img.size
    start_point = random.randint(1, width-50)
    end_point = start_point + 50

    random_color = (random.choice(range(256)), random.choice(range(256)), random.choice(range(256)), 0)

    back = Image.new('RGBA', (512,512), random_color)
    poly = Image.new('RGBA', (512,512))
    pdraw = ImageDraw.Draw(poly)
    pdraw.polygon(((0,0), (500,0), (500,500), (0, 500)), fill=(255,255,255,127), outline=(255,255,255,0))
    back.paste(poly,mask=poly)

    crop_area = (start_point, start_point, end_point, end_point)
    crop_img = img.crop(crop_area)
    blowup = crop_img.resize((500,500))

    blowup.paste(back, mask=back)

    return(blowup.convert('RGB'))