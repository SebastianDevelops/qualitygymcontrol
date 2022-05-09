#!Django-Gym-Member-Manager\venv
pip install -r requirements.txt

python manage.py collectstatic
python manage.py migrate