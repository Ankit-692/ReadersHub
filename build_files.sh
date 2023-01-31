echo " BUILD START"
python3.10.5 install -r requirements.txt
python3.10.5 manage.py collectstatic
echo " BUILD END"