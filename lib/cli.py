import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Customer, Table, Reservation
from datetime import datetime

DATABASE_URL = "sqlite:///hotel_reservation.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def init_db():
    """Initialize the database."""
    Base.metadata.create_all(engine)
    print("Database Initialized")


def create_customer():
    """Create a new customer."""
    name = input("Enter customer name: ")
    phone = input("Enter customer phone: ")
    customer = Customer(name=name, phone=phone)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' created with ID {customer.id}")


def update_customer():
    """Update an existing customer's details."""
    customer_id = int(input("Enter Customer ID to update: "))
    customer = session.get(Customer, customer_id)
    if not customer:
        print(f"Customer with ID {customer_id} does not exist.")
        return
    customer.name = input(f"Enter new name (current: {customer.name}): ") or customer.name
    customer.phone = input(f"Enter new phone (current: {customer.phone}): ") or customer.phone
    session.commit()
    print(f"Customer ID {customer_id} updated successfully")


def delete_customer():
    """Delete a customer."""
    customer_id = int(input("Enter Customer ID to delete: "))
    customer = session.get(Customer, customer_id)
    if not customer:
        print(f"Customer with ID {customer_id} does not exist.")
        return
    session.delete(customer)
    session.commit()
    print(f"Customer ID {customer_id} deleted successfully")


def create_table():
    """Create a new table."""
    table_number = int(input("Enter table number: "))
    capacity = int(input("Enter table capacity: "))
    new_table = Table(table_number=table_number, capacity=capacity)
    session.add(new_table)
    session.commit()
    print(f"Table {table_number} created with capacity {capacity}")


def create_reservation():
    """Create a new reservation."""
    customer_id = int(input("Enter Customer ID: "))
    table_id = int(input("Enter Table ID: "))
    date = input("Enter reservation date and time (YYYY-MM-DD HH:MM:SS): ")

    customer = session.get(Customer, customer_id)
    table = session.get(Table, table_id)

    if not customer:
        print(f"Customer with ID {customer_id} does not exist.")
        return
    if not table:
        print(f"Table with ID {table_id} does not exist.")
        return

    date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    reservation = Reservation(customer_id=customer_id, table_id=table_id, date=date_obj)
    session.add(reservation)
    session.commit()
    print(f"Reservation created with ID {reservation.id}")


def update_reservation():
    """Update an existing reservation."""
    reservation_id = int(input("Enter Reservation ID to update: "))
    reservation = session.get(Reservation, reservation_id)

    if not reservation:
        print(f"Reservation with ID {reservation_id} does not exist.")
        return

    customer_id = input(f"Enter new Customer ID (current: {reservation.customer_id}): ")
    table_id = input(f"Enter new Table ID (current: {reservation.table_id}): ")
    date = input(f"Enter new reservation date (current: {reservation.date}, format: YYYY-MM-DD HH:MM:SS): ")

    if customer_id:
        reservation.customer_id = int(customer_id)
    if table_id:
        reservation.table_id = int(table_id)
    if date:
        reservation.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    session.commit()
    print(f"Reservation ID {reservation_id} updated successfully")


def delete_reservation():
    """Delete a reservation."""
    reservation_id = int(input("Enter Reservation ID to delete: "))
    reservation = session.get(Reservation, reservation_id)
    if not reservation:
        print(f"Reservation with ID {reservation_id} does not exist.")
        return
    session.delete(reservation)
    session.commit()
    print(f"Reservation ID {reservation_id} deleted successfully")


def list_customers():
    """List all customers."""
    customers = session.query(Customer).all()
    if not customers:
        print("No customers found.")
    for customer in customers:
        print(customer)


def list_tables():
    """List all tables."""
    tables = session.query(Table).all()
    if not tables:
        print("No tables found.")
    for table in tables:
        print(table)


def list_reservations():
    """List all reservations."""
    reservations = session.query(Reservation).all()
    if not reservations:
        print("No reservations found.")
    for reservation in reservations:
        print(reservation)


def main_menu():
    """Display the main menu."""
    while True:
        print("\nWelcome to the Hotel Reservation System. What would you like to do?")
        print("1. Create Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Create Table")
        print("5. Create Reservation")
        print("6. Update Reservation")
        print("7. Delete Reservation")
        print("8. List Customers")
        print("9. List Tables")
        print("10. List Reservations")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            update_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            create_table()
        elif choice == "5":
            create_reservation()
        elif choice == "6":
            update_reservation()
        elif choice == "7":
            delete_reservation()
        elif choice == "8":
            list_customers()
        elif choice == "9":
            list_tables()
        elif choice == "10":
            list_reservations()
        elif choice == "11":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    init_db()
    main_menu()
