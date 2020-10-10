from PIL import Image
from pathlib import Path
import random

num_back = 5
num_head = 6
num_mouth = 5
num_eye = 6
num_nose = 5

def get_path(a, file):
    outpath = Path.cwd()/'images'/a/file
    return outpath


# Выбираем случайное изображение
back = Image.open(get_path('backs', f'back{random.randint(1, num_back)}.png'))
head = Image.open(get_path('heads', f'head{random.randint(1, num_head)}.png'))
mouth = Image.open(get_path('mouths', f'mouth{random.randint(1, num_mouth)}.png'))
eye = Image.open(get_path('eyes', f'eye{random.randint(1, num_eye)}.png'))
nose = Image.open(get_path('noses', f'nose{random.randint(1, num_nose)}.png'))

# Склеиваем изображения
back.paste(head.convert('RGB'), (0,0), head)
back.paste(mouth.convert('RGB'), (0,0), mouth)
back.paste(eye.convert('RGB'), (0,0), eye)
back.paste(nose.convert('RGB'), (0,0), nose)

#Сохраняем 
back.save(get_path('images' , 'result.png'))