# Nozimbek Portfolio — Django

Terminal uslubidagi shaxsiy portfolio.

## Tuzilishi

- `config/` — Django project konfiguratsiyasi
- `portfolio/` — asosiy Django app
- `templates/` — HTML template fayllari
- `static/` — CSS va JavaScript
- `manage.py` — Django boshqaruv fayli

## Ishga tushirish

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Keyin:

- Sayt: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Admin paneldan `Projects` va `Articles` qo'shishingiz mumkin.
