#!/usr/bin/env python3

from faker import Faker
import random
from datetime import datetime, timedelta
from helpers import get_session, Customer, Table, Reservation

if __name__ == '__main__':
    
    session = get_session()

    
    for reservation in session.query(Reservation).all():
        session.delete(reservation)
    for table in session.query(Table).all():
        session.delete(table)
    for customer in session.query(Customer).all():
        session.delete(customer)

    session.commit() 

    fake = Faker()

   
    tables = []
    for table_number in range(1, 21):
        table = Table(
            table_number=table_number,
            capacity=random.choice([2, 4, 6, 8]) 
        )   
        tables.append(table)

    session.add_all(tables)
    session.commit()

   
    customers = []
    for _ in range(50): 
        customer = Customer(
            name=fake.name(),
            phone=fake.phone_number(),
        )
        customers.append(customer)

    session.add_all(customers)
    session.commit()

   
    reservations = []
    for customer in customers:
        for _ in range(random.randint(1, 3)):
            table = random.choice(tables)
            date = datetime.now() + timedelta(days=random.randint(1, 30))

            existing_reservation = session.query(Reservation).filter(
                Reservation.table_id == table.id,
                Reservation.date == date
            ).first()

            if not existing_reservation:
                reservation = Reservation(
                    customer_id=customer.id,
                    table_id=table.id,
                    date=date
                )
                reservations.append(reservation)

    session.bulk_save_objects(reservations)
    session.commit()
    session.close()

    print(f"Generated {len(customers)} customers, {len(tables)} tables, and {len(reservations)} reservations.")
