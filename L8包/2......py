from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母:
def rnd_char():
    return chr(random.randint(65, 90))


# 随机颜色:
def rnd_color():
    return random.randint(0, 245), random.randint(0, 245), random.randint(0, 245)


# 生成验证码和图片
def generate_code(file_name='code'):
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象
    font = ImageFont.truetype('arial.ttf', 36)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 随机生成两条直线（一条贯穿上半部，一条贯穿下半部）
    draw.line((0, 0 + random.randint(0, height // 2),
               width, 0 + random.randint(0, height // 2)),
              fill=rnd_color())
    draw.line((0, height - random.randint(0, height // 2),
               width, height - random.randint(0, height // 2)),
              fill=rnd_color())
    # 输出文字
    code_str = ''
    for t in range(4):
        tmp = rnd_char()
        draw.text((60 * t + 10, 10), tmp, font=font, fill=rnd_color())
        code_str += tmp
    #干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rnd_color())
    #干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rnd_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rnd_color())
    #扭曲
    image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
    # 模糊处理
    image = image.filter(ImageFilter.BLUR)
    image.save(file_name + '.png', 'png')
    return code_str, file_name


if __name__ == '__main__':
    for i in range(1):
        generate_code('code%d' % i)
