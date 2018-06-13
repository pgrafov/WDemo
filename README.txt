Testing locally:

1. git clone https://github.com/pgrafov/WDemo.git
2. cd WDemo
3. Create a virtual enviroment for Python 3 and install dependencies:
  python3 -m venv venv
  ./venv/bin/pip install -r requirements.txt
4. Install postgresql. Create user "8fit" with password "8fit", create a database "8fit" and grant user all permissions on this database.
Also make sure that the user can create databases - this is needed for testing purposes.
5. Run  tests: ./venv/bin/python manage.py test
6. Create tables: ./venv/bin/python manage.py migrate
7. Load some data (one promotion page and two promotions):
   ./venv/bin/python manage.py loaddata some_data_p1.json
   ./venv/bin/python manage.py loaddata some_data_p2.json
8. Start server: ./venv/bin/python manage.py runserver

After that you will be able to point your browser to http://127.0.0.1:8000/ and see empty page.

There is one user in the system, it has 'eightfit' as username and 'eightfit' as password. This is a superuser.

At http://127.0.0.1:8000/admin/ a designer can create promotion pages from existing blocks (I created only three types of blocks and they don't look that pretty but you get the idea). This is the default Wagtail functionality.

At http://127.0.0.1:8000/django-admin/home/ a marketer can create  different promotions - with different prices, different descriptions, maybe different billing cycles and so on. At the same page a promotion can be linked to a promotion page. To link a promotion to a promotion page
I introduced a separate entity called PromoUrl. Promourls allow for multiple pages to sell the same promotion or to sell different promotions without having to create a separate page for every promotion. Take a look at http://127.0.0.1:8000/promo/please-please-buy-it/ and
http://127.0.0.1:8000/promo/this-one-is-even-better/. These two urls point to the same page, but the promotion is different ($49 for 12 months vs $26 for 6 months).