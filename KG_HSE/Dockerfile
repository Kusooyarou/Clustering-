FROM python:3.10-slim

# рабочая директорию
WORKDIR /app

# копируем файлы проекта в контейнер
COPY . .

# устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# команда для запуска приложения
CMD ["python", "main.py"]
