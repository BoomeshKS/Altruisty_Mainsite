set -D errexit

pip install -r requirements.txt

python manage.py migrate