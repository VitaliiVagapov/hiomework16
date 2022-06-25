import datetime
import main

from models import *

db.drop_all()

db.create_all()

for user in main.USERS:
    db.session.add(User(
        id=user['id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        email=user['email'],
        role=user['role'],
        phone=user['phone']
    ))
    db.session.commit()

for order in main.ORDERS:
    month_start, day_start, year_start = [int(o) for o in order['start_date'].split("/")]

    month_end, day_end, year_end = order['end_date'].split("/")

    db.session.add(Order(
        id=order['id'],
        name=order['name'],
        description=order['description'],
        start_date=datetime.date(year=year_start, month=month_start, day=day_start),
        end_date=datetime.date(year=int(year_end), month=int(month_end), day=int(day_end)),
        address=order['address'],
        price=order['price'],
        customer_id=order['customer_id'],
        executor_id=order['executor_id']
    ))
    db.session.commit()

db.session.add_all(
    [Offer(id=offer['id'],order_id=offer['order_id'], executor_id=offer['executor_id']) for offer in main.OFFERS])

db.session.commit()