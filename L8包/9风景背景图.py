
from PIL import Image,ImageDraw,ImageFont,ImageTk,ImageFilter
import random

# 随机字母
def random_char():
   return chr(random.randint(65,90))

# 随机数字
def random_num():
    return random.randint(0,9)

# 随机字体颜色  微深
def random_color():
    return(random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

# 生成空白背景涂层
images = Image.new('RGB',size=(240,60),color=(255,255,255))
image = Image.open('demo3.jpg')
im = ImageTk.PhotoImage(image)
images.draw_image(120,20,image=im)
# 生成绘制对象
draw = ImageDraw.Draw(image)
# 字体对象，字体、字号
font = ImageFont.truetype('arial.ttf',36)

# 生成文字
for t in range(0,4):
    draw.text((60*t+20,10),random_char(),font=font,fill=random_color())

# 保存
image.save('demo9.jpg','jpeg')

