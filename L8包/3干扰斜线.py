
from PIL import Image,ImageDraw,ImageFont,ImageFilter
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

# 随机背景颜色  颜色微浅
def random_color2():
    return (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120))

# 生成空白背景涂层
width = 60*4
height = 60
image = Image.new('RGB',(width,height),color=(255,255,255))
# 生成绘制对象
draw = ImageDraw.Draw(image)
# 字体对象，字体、字号
font = ImageFont.truetype('arial.ttf',36)

#  循环像素点并填充颜色
# for x in range(0,240):
#     for y in range(0,60):
#         draw.point(xy=(x,y),fill = random_color2())

def gene_line():
  size = (240,60)
  begin = (random.randint(12, width), random.randint(5, height))
  end = (random.randint(3, width), random.randint(7, height))
  draw.line([begin, end], fill = (225,0,0))

for i in range(8):
    gene_line()

# 生成文字
for t in range(0,4):
    draw.text((60*t+20,10),random_char(),font=font,fill=random_color())

# 加模糊滤镜
image = image.filter(ImageFilter.BLUR)

# 保存
image.save('demo3.jpg','jpeg')

