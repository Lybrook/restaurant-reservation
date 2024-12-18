from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Table, Reservation
from datetime import datetime

engine = create_engine("sqlite:///hotel_reservation.db")
Session = sessionmaker(bind=engine)
session = Session()



def init_db():
    
    Base.metadata.create_all(engine)
    print("Database Initialized")

def get_session():
    return Session()

def close_session(session):
    session.close()


def create_customer(name, phone):
    
    customer = Customer(name=name, phone=phone)
    session.add(customer)
    session.commit()
    return customer


def update_customer(customer_id, name, phone):
    
    customer = session.get(Customer, customer_id)
    if customer:
        customer.name = name or customer.name
        customer.phone = phone or customer.phone
        session.commit()
        return customer
    return None


def delete_customer(customer_id):
   
    customer = session.get(Customer, customer_id)
    if customer:
        session.delete(customer)
        session.commit()
        return True
    return False


def create_table(table_number, capacity):
   
    new_table = Table(table_number=table_number, capacity=capacity)
    session.add(new_table)
    session.commit()
    return new_table


def create_reservation(customer_id, table_id, date_str):
    
    customer = session.get(Customer, customer_id)
    table = session.get(Table, table_id)

    if customer and table:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        reservation = Reservation(customer_id=customer_id, table_id=table_id, date=date_obj)
        session.add(reservation)
        session.commit()
        return reservation
    return None


def update_reservation(reservation_id, customer_id=None, table_id=None, date_str=None):
   
    reservation = session.get(Reservation, reservation_id)
    if reservation:
        if customer_id:
            reservation.customer_id = customer_id
        if table_id:
            reservation.table_id = table_id
        if date_str:
            reservation.date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        session.commit()
        return reservation
    return None


def delete_reservation(reservation_id):
    
    reservation = session.get(Reservation, reservation_id)
    if reservation:
        session.delete(reservation)
        session.commit()
        return True
    return False


def list_customers():
    
    return session.query(Customer).all()


def list_tables():
    
    return session.query(Table).all()


def list_reservations():
    
    return session.query(Reservation).all()
