# book_store<br>
Simple implementation of some functionality of goodreads.com/<br>
Users can register and leave reviews on Book. <br>
Defined session-based Cart for purchase purposes.<br>
When customer buy book, they receive email receipt.<br>
Every saturday at 11:55 admin receives email report for of each order.<br>

commands: <br>
pip install -r requirements.txt<br>
celery -A store worker -B -l info<br>
celery -A store flower<br>
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management <br>
python manage.py runserver<br>