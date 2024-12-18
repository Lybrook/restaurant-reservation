
import sys
from models import Customer, Reservation 
from helpers import (
    get_session,
    init_db,
    create_customer,
    update_customer,
    delete_customer,
    create_table,
    create_reservation,
    update_reservation,
    delete_reservation,
    list_customers,
    list_tables,
    list_reservations,
    close_session
)




def main_menu():
    session = get_session()

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
            name = input("Enter customer name: ")
            phone = input("Enter customer phone: ")
            customer = create_customer(name, phone)
            print(f"Customer '{name}' created with ID {customer.id}")
        elif choice == "2":
            customer_id = int(input("Enter Customer ID to update: "))
            customer = session.get(Customer, customer_id)
            if not customer:
                print(f"Customer with ID {customer_id} does not exist.")
                continue
            name = input(f"Enter new name (current: {customer.name}): ") or customer.name
            phone = input(f"Enter new phone (current: {customer.phone}): ") or customer.phone
            updated_customer = update_customer(customer_id, name, phone)
            if updated_customer:
                print(f"Customer ID {customer_id} updated successfully")
            else:
                print(f"Customer with ID {customer_id} does not exist.")
        elif choice == "3":
            customer_id = int(input("Enter Customer ID to delete: "))
            if delete_customer(customer_id):
                print(f"Customer ID {customer_id} deleted successfully")
            else:
                print(f"Customer with ID {customer_id} does not exist.")
        elif choice == "4":
            table_number = int(input("Enter table number: "))
            capacity = int(input("Enter table capacity: "))
            table = create_table(table_number, capacity)
            print(f"Table {table.table_number} created with capacity {table.capacity}")
        elif choice == "5":
            customer_id = int(input("Enter Customer ID: "))
            table_id = int(input("Enter Table ID: "))
            date = input("Enter reservation date and time (YYYY-MM-DD HH:MM:SS): ")
            reservation = create_reservation(customer_id, table_id, date)
            if reservation:
                print(f"Reservation created with ID {reservation.id}")
            else:
                print("Customer or Table not found.")
        elif choice == "6":
            reservation_id = int(input("Enter Reservation ID to update: "))
            reservation = session.get(Reservation, reservation_id)
            if not reservation:
                print(f"Reservation with ID {reservation_id} does not exist.")
                continue
            customer_id = input(f"Enter new Customer ID (current: {reservation.customer_id}): ")
            table_id = input(f"Enter new Table ID (current: {reservation.table_id}): ")
            date = input(f"Enter new reservation date (current: {reservation.date}, format: YYYY-MM-DD HH:MM:SS): ")
            updated_reservation = update_reservation(reservation_id, customer_id or None, table_id or None, date or None)
            if updated_reservation:
                print(f"Reservation ID {reservation_id} updated successfully")
            else:
                print(f"Reservation with ID {reservation_id} does not exist.")
        elif choice == "7":
            reservation_id = int(input("Enter Reservation ID to delete: "))
            if delete_reservation(reservation_id):
                print(f"Reservation ID {reservation_id} deleted successfully")
            else:
                print(f"Reservation with ID {reservation_id} does not exist.")
        elif choice == "8":
            customers = list_customers()
            if not customers:
                print("No customers found.")
            for customer in customers:
                print(customer)
        elif choice == "9":
            tables = list_tables()
            if not tables:
                print("No tables found.")
            for table in tables:
                print(table)
        elif choice == "10":
            reservations = list_reservations()
            if not reservations:
                print("No reservations found.")
            for reservation in reservations:
                print(reservation)
        elif choice == "11":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

    close_session(session)

if __name__ == "__main__":
    init_db()  
    main_menu()
