# django52

[News of Django 5.2](https://docs.djangoproject.com/en/5.2/releases/5.2/)

## Este projeto foi feito com:

* [Python 3.12.4](https://www.python.org/)
* [Django 5.2.0](https://www.djangoproject.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django52.git
cd django52

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

