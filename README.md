# Medarbetarpuls

## 1. Installation & Setup

### Prerequisites
Before installing packages, ensure you have the following installed:

- **Python** (Recommended version: 3.10+)
- **Redis** 

### Installation steps

1. **Create a virtual environment**
```sh
python -m venv venv
```

2. **Activate the virtual environment:**
```sh
source venv/bin/activate
```

2.1. **To deactivate the virtual environment:**
```sh
deactivate
```

#### **Warning: From here on the virtual environment needs to be activated!**

If the virtual environment is deactivate or the terminal is restarted the
venv needs to be activated again!

3. **Upgrade/install pip:**
```sh
python -m pip install --upgrade pip
```

4. **Install required packages:**
```sh
python -m pip install -r requirements.txt --quiet --no-cache-dir
```

5. **Verify installation:**
```sh
django-admin --version
```
Here a version of Django should be printed in the terminal!

### Running the server

1. **Change directory to Django-project one:** 
```sh
cd Medarbetarpuls
```

2. **Migrate the database:**
```sh
python manage.py migrate
```

3. Start Redis server (note that this requires sudo privileges): 
```sh
sudo systemctl start redis
```

3.1. Optionally enable Redis to be started on boot:  
```sh
sudo systemctl enable redis
```

#### **Warning: Redis should be configured with a separate systemd profile for security reasons**

4. **Start the Django and Redis servers:**
```sh
python manage.py runserver & celery -A Medarbetarpuls beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -l info
```

**Now, you can visit the host (http://127.0.0.1:8000/ if unspecified) to see the website!**
