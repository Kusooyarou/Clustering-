# hsecg

**для начала следует склонировать данный репозиторий к себе на устройство с помощью команды:**

```bash
git clone https://git.miem.hse.ru/anvibabenko/hsecg.git
```

### если запускать через виртуальное окружение

**нужно создать виртуальное окружение:**

## для Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## для macOS и Linux:

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

### если запускать через Docker

**для начала нужно убедиться, что на устройстве установлен Docker**. Затем следуйте этим шагам:

1. соберите Docker-образ с помощью команды:
   
   ```bash
   docker build -t hsecg .
   ```

2. после сборки запустите контейнер:

   ```bash
   docker run -it --rm hsecg
   ```

3. если хотите запустить проект с использованием Docker Compose, выполните команду:

   ```bash
   docker-compose up
   ```

**теперь проект запустится в контейнере и будет доступен через WSL или напрямую в терминале Docker**.
