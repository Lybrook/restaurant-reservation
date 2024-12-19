## Hotel Reservation Application  
- Welcome to my hotel reservation application!  


***

## Introduction


```console
├── cli.py
├── helpers.py
├── models.py helpers.py
├── seed.py
├── Pipfile
├── Pipfile.lock
├── README.md

```


***

## Project Overview - Features  
- Create a Customer  
- Update a Customer  
- Delete a Customer  
- Create a Table  
- Update a Table  
- Delete a Table  
- Create a Reservation  
- Update a Reservation  
- Delete a Reservation  
- Assign Reservation to a Table  
- List Customers  
- List Tables  
- List Reservations  
- View Reservations by Table  
- Exit  

## Technologies Used  
- Python 3  
- SQLAlchemy  
- Alembic  

## Installations 
- git clone 
- cd HOTEL-RESERVATION
- code . To open VScode
- Install the necessary Python dependencies 
    1. pipenv install sqlalchemy
    2. pipenv install alembic

## Migrations
- To setup migrations run alembic init migrations. We ony run this command once
- Modify alembic.ini sqlalchemy.url to the required db i.e test.db
- Modify env.py inside migrations folder and import base model from models file
- To create a migration alembic revision --autogenerate -m "message"
- To apply the generatde migration, run alembic upgrade head    

## Contributions
- If you have any suggestions or you find issues, feel free to reach out or submit a pull requst.All contributions are welcomed!
1. Fork the project
2. Create a branch
3. Commit your changes
4. Push to branch
5. Open a pull request


