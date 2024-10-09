from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import os
import shutil  # импортируем shutil для копирования файлов
from ModulesFolder.color import get_dominant_color, is_similar_color
from ModulesFolder.page_generator import generate_html

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
DATAFRAME_FOLDER = 'DataFrame'  # Директория для изображений, по которым идёт фильтрация
OUTPUT_HTML_PATH = 'static/output.html'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


# загрузка изображения и фильтрация по цвету
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # сохранение загруженного изображения
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # определение доминирующего цвета загруженного изображения
    image = np.array(Image.open(file_path))
    example_dominant_color = get_dominant_color(image)

    # фильтрация изображений по доминирующему цвету
    filtered_images = []
    for filename in os.listdir(DATAFRAME_FOLDER):
        if filename.endswith(".jpg"):
            image_path = os.path.join(DATAFRAME_FOLDER, filename)
            image = np.array(Image.open(image_path))
            dominant_color = get_dominant_color(image)
            if is_similar_color(dominant_color, example_dominant_color):
                # Копирование изображения в папку uploads
                dest_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                shutil.copy(image_path, dest_path)  # Копируем файл
                filtered_images.append('uploads/' + filename)  # Сохранение относительных путей к файлам

    # генерация HTML страницы с результатами
    generate_html(filtered_images, OUTPUT_HTML_PATH)

    # отображение страницы с результатами фильтрации
    return render_template('result.html', images=filtered_images, html_path=OUTPUT_HTML_PATH)


if __name__ == '__main__':
    app.run()
