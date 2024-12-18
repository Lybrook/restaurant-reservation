#!/usr/bin/env python3

from faker import Faker
import random
from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Table, Reservation

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///hotel_reservation.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Reservation).delete()
    session.query(Table).delete()
    session.query(Customer).delete()

    fake = Faker()

  
    tables = []
    for table_number in range(1, 21):
        table = Table(
            table_number=table_number,
            capacity=random.choice([2, 4, 6, 8]) 
        )
        session.add(table)
        session.commit()
        tables.append(table)

  
    customers = []
    for _ in range(50): 
        customer = Customer(
            name=fake.name(),
            phone=fake.phone_number(),
        )
        session.add(customer)
        session.commit()
        customers.append(customer)

   
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
