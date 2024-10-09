
# hsecg

## Структура проекта

```
hsecg/
│
KG_HSE/
│
├── DataFrame/
│ └── изображения
│
├── ModulesFolder/ # папка с отдельными вспомогательными модулями
│ ├── init.py 
│ ├── color.py # файл для определения основного цвета
│ ├── page_generator.py # файл для создания html
│
├── docker-compose.yml # файл для запуска проекта через Docker Compose
├── Dockerfile # Docker-файл для сборки проекта
├── main.py # главный файл для запуска проекта
├── requirements.txt # зависимости проекта
├── test.py # файл для отдельного определения цвета (для проверки)
```

## Для начала следует склонировать данный репозиторий к себе на устройство с помощью команды:

```bash
git clone https://git.miem.hse.ru/anvibabenko/hsecg.git
```

### Если запускать через виртуальное окружение

**нужно создать виртуальное окружение:**

### для Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### для macOS и Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**для работы проекта необходимо установить библиотеки из файла** `requirements.txt` **с помощью команды:**

```bash
pip install -r requirements.txt
```

**запустить программу из файла** `main.py`:

```bash
python main.py
```

### Если запускать через Docker

**Для начала нужно убедиться, что на устройстве установлен Docker**. Затем следуйте этим шагам:

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

**Теперь проект запустится в контейнере и будет доступен через WSL или напрямую в терминале Docker.**

### Источник алгоритма

Этот алгоритм был взят с сайта [сайт источника]. Также для редактирования этого файла и объяснения кода использовался OpenAI GPT.
