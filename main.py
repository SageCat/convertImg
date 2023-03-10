from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from MyConfig import MyConfig
import time


def read_config(conf_file_name):
    config = MyConfig(conf_file_name)
    return config


if __name__ == '__main__':
    # reading configuration from conf.ini file
    conf = read_config('conf.ini')
    image_width = int(conf.get('image', 'image_width'))
    image_height = int(conf.get('image', 'image_height'))
    font_size = int(conf.get('font', 'font_size'))
    font_name = conf.get('font', 'font_name')
    font_color = [int(str.strip(value)) for value in conf.get('font', 'font_color_rgb').split(',')]
    # reading headline list
    df = pd.read_excel('name_list.xlsx')
    for i in df.index:
        with Image.open('bg.png').resize((image_width, image_height)) as bg:
            draw = ImageDraw.Draw(bg)
            # setting font style
            fnt = ImageFont.truetype(r'C:\Windows\Fonts\{}.ttf'.format(font_name), font_size)
            draw.text((int(image_width / 2), int(image_height / 2)),
                      text=df.iloc[i, 0],
                      font=fnt,
                      fill=tuple(font_color),
                      anchor='mm')
            file_name = str(i + 1) + '-' + df.iloc[i, 0] + '.png'
            # export converted image to imgs folder
            bg.save("imgs/" + file_name)
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print('{} is saved successfully in imgs folder'.format(file_name))
    print('==============================')
    print('all images converted done !!!!  bye ~~~~~ (*^▽^*)')
    time.sleep(5)
