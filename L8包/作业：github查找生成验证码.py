from PIL import Image,ImageFont,ImageDraw,ImageFilter
# import matplotlib.pyplot as plt
# from pylab import *
import random
import string

def get_random_char():
    return (range.choice(string.letters)for _ in range(4))

def get_random_color():
    return(random.randint(20,100),random.randint(20,100),random.randint(20,100))

def get_digit_pic():
    width = 320
    height = 100
    im = Image.new('RGB',(width,height),(180,180,180))

    fontstyle = "arial.ttf"
    fontsize = min(im.size)/2
    font = ImageFont.truetype(fontstyle,fontsize)
    # 生成四个随机数字
    digits = get_random_char()
    # 绘制数字
    for i in range(4):
        ImageDraw.Draw(im).text(((i+1)*max(im.size)/6,0),font=font,fill=get_random_color())
    # 添加影响
    for _ in range(random.randint(3000,5000)):
        ImageDraw.Draw(im).point((random.randint(0,width),random.randint(0,height)),fill=get_random_color())
    # 模糊图像
    im = im.filter(ImageFilter.BLUR)
    # 保存
    im.save('github.jpg','jepg')


