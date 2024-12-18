from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///hotel_reservation.db')


Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

   
    reservations = relationship('Reservation', back_populates='customer')

    def __repr__(self):
        return f'Customer(id={self.id}, name={self.name}, phone={self.phone})'

class Table(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)
    table_number = Column(Integer, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    
    reservations = relationship('Reservation', back_populates='table')

    def __repr__(self):
        return f'Table(id={self.id}, table_number={self.table_number}, capacity={self.capacity})'

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    table_id = Column(Integer, ForeignKey('tables.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    customer = relationship('Customer', back_populates='reservations')
    table = relationship('Table', back_populates='reservations')

    def __repr__(self):
        return f'Reservation(id={self.id}, customer_id={self.customer_id}, table_id={self.table_id}, date={self.date})'


Base.metadata.create_all(engine)
