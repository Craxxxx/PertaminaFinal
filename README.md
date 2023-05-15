# PertaminaFinal

Aplikasi Monitoring CCTV Multivendor Berbasis Web

Yang diperlukan:

Python Latest Stable
Library Flask
Library Mysqldb
Xampp
Library Mysqldb.connector
Library OpenCV
Library Pandas
bisa diinstall dengan menjalankan pip install -r requirements.txt (pastikan python sudah terinstall terlebih dahulu)

Yang terInstall di Device Developer:

Package                Version
---------------------- --------
alembic                1.9.2
bcrypt                 4.0.1
click                  8.1.3
colorama               0.4.6
Flask                  2.2.2
Flask-Login            0.6.2
Flask-Migrate          4.0.2
Flask-MySQLdb          1.0.1
Flask-SQLAlchemy       3.0.2
greenlet               2.0.1
itsdangerous           2.1.2
Jinja2                 3.1.2
Mako                   1.2.4
MarkupSafe             2.1.2
mysql-connector-python 8.0.32
mysqlclient            2.1.1
numpy                  1.24.1
opencv-python          4.7.0.68
pandas                 1.5.3
pip                    22.3.1
protobuf               3.20.3
python-dateutil        2.8.2
pytz                   2022.7.1
setuptools             65.5.0
six                    1.16.0
SQLAlchemy             1.4.46
SQLAlchemy-Utils       0.39.0
var-dump               1.2
Werkzeug               2.2.2

Apabila file tidak bisa di run sesuaikan package python dengan yang terinstall di device developer

How to Run?

Put all item in one Folder
Install XAMPP, run MySQL & Apache
Using browser go to localhost/phpmyadmin

1. Make new database with name pertamina
2. Run app.py
3. Open Terminal and input flask db migrate
4. Open PHPmyAdmin and create new user for the user table with email,username,password,Permission
5. Put Admin inside the permission Section
6. Restart app.py 
Make sure you use same network with the cctv otherwise, it won't work
