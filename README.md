# hsecg

**для начала следует склонировать данный репозиторий к себе на устройство с помощью команды:**

```bash
git clone https://git.miem.hse.ru/anvibabenko/hsecg.git
```

### запуск через виртуальное окружение

**нужно создать виртуальное окружение:**

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

**для работы проекта необходимо установить библиотеки из файла** `requirements.txt` **с помощью команды:**

```bash
pip install -r requirements.txt
```

**дапустить программу из файла** `main.py`:

```bash
python main.py
```

### дапуск через Docker

**убедитесь, что Docker установлен на вашем устройстве.** Далее следуйте инструкциям:

1. если образ ещё не собран, выполните команду для сборки Docker-образа:
   
   ```bash
   docker build -t hsecg .
   ```

2. после сборки образа запустите контейнер с проектом:

   ```bash
   docker run -it --rm hsecg
   ```

3. если используете Docker Compose, выполните команду:

   ```bash
   docker-compose up
   ```

**ееперь проект запустится в контейнере и будет доступен через WSL или в терминале Docker.**

### источники

алгоритм для нахождения доминирующего цвета был взят с сайта [https://qna.habr.com/q/542007].
