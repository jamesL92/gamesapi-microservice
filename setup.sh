if [ -e db.sqlite3 ]
then
    echo removing database.
    rm db.sqlite3
fi
python manage.py migrate
python manage.py loaddata comment game platform publisher user
