import os
import webbrowser
from PIL import Image
import numpy as np
from modules_folder.color import get_dominant_color, is_similar_color
from modules_folder.page_generator import generate_html

example_image_path = "example.jpg"
dataframe_folder = "DataFrame"
output_html_path = "output.html"

# определение доминирующего цвета
example_image = np.array(Image.open(example_image_path))
example_dominant_color = get_dominant_color(example_image)

# фильтр дата фрейма
filtered_images = []
for filename in os.listdir(dataframe_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(dataframe_folder, filename)
        image = np.array(Image.open(image_path))
        dominant_color = get_dominant_color(image)
        if is_similar_color(dominant_color, example_dominant_color):
            filtered_images.append(os.path.join(dataframe_folder, filename))


print("Отобранные изображения:")
for img in filtered_images:
    print(img)
print('\n')

generate_html(filtered_images, output_html_path)
print(f"HTML-страница с изображениями сохранена в {output_html_path}")

# для автоматического открытия странички
webbrowser.open(f'file://{os.path.abspath(output_html_path)}')
