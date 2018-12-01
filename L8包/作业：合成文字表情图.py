from PIL import Image,ImageDraw,ImageFont

img = Image.open('.\picture.png')
draw = ImageDraw.Draw(img)
ttfront = ImageFont.truetype('msyh.ttf',24)
draw.text((32,180),"我的内心毫无波动\n  甚至还想笑",fill=(0,0,0),font=ttfront)
img.save('.\picture1.png')
