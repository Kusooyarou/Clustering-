# hsecg

## cтруктура проекта

```
hsecg/
│
├── KG_HSE/
│   ├── DataFrame/
│   │   └── тут изображения
│   │
│   ├── ModulesFolder/
│   │   ├── __init__.py 
│   │   ├── color.py  # файл для определения основного цвета
│   │   └── page_generator.py  # файл для создания HTML
│   │
│   ├── static/
│   │   └── uploads/
│   │       └── example.jpg
│   │
│   ├── templates/  # шаблоны html страниц
│   │   ├── index.html  # шаблон страницы для загрузки изображения
│   │   └── result.html  # шаблон страницы с отобранными изображениями
│   │
│   ├── main.py  # главный файл для запуска проекта
│   ├── requirements.txt  # зависимости проекта
│   ├── test.py  # файл для отдельного определения цвета (для проверки отдельных изображений)
│   ├── Dockerfile  # Docker-файл для сборки проекта
│   └── docker-compose.yml  # файл для запуска проекта через Docker Compose
│
```

## описание проекта

проект **hsecg** предназначен для загрузки изображений, определения их доминирующего цвета и фильтрации набора изображений на основе этого цвета. основные компоненты проекта включают:

- **ModulesFolder**: содержит вспомогательные модули для определения цвета и генерации HTML-страниц.
- **DataFrame**: хранит изображения, которые будут использоваться для фильтрации.
- **static/uploads**: папка для сохранения загруженных пользователем изображений.
- **templates**: содержит HTML-шаблоны для пользовательского интерфейса.

## установка

### клонирование репозитория

для начала следует склонировать данный репозиторий к себе на устройство с помощью команды:

```bash
git clone https://git.miem.hse.ru/anvibabenko/hsecg.git
```

### если запускать через виртуальное окружение

**создайте виртуальное окружение:**

#### для Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### для macOS и Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**установите библиотеки из файла `requirements.txt` с помощью команды:**

```bash
pip install -r requirements.txt
```

**запустите программу из файла `main.py`:**

```bash
python main.py
```

### если запускать через Docker

**для начала убедитесь, что на устройстве установлен Docker. затем следуйте следующим шагам:**

1. соберите Docker-образ с помощью команды:
   
   ```bash
   docker build -t hsecg .
   ```

2. после сборки запустите контейнер:

   ```bash
   docker run -p 3000:3000 hsecg
   ```

3. если хотите запустить проект с использованием Docker Compose, выполните команду:

   ```bash
   docker-compose up
   ```

**теперь проект запустится в контейнере и будет доступен через WSL или напрямую в терминале Docker.**

## использование

после запуска сервера, откройте веб-браузер и перейдите по адресу `http://localhost:3000`. 

на главной странице нажмите на кнопку **Choose File**, выберите изображение, по которому будет определяться доминирующий цвет, и нажмите на кнопку **Upload Image**. далее подождите, пока программа "подумает", и откроется страница с отобранными изображениями, соответствующими главному цвету загруженного изображения.

### источник алгоритма

алгоритм определения главного цвета был взят с сайта [https://qna.habr.com/q/542007]. Также для редактирования README.md-файла, помощи создания адаптивной вёрстки для html страниц, помощи при поднятии сервера на flask и обхяснением кода использовался OpenAI GPT.