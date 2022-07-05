# budget-manager
System to allow people to manage their budgets buy creating items, sharing items with others (i.e. friends). 
Users can sent friend request to another user so they can share budgets or items in their budgets. 

## How to run it locally on your machine:
1. Create virtual environment.
2. Activate the virtual environment created in step 1.
3. Clone this repository.
4. Navigate into **budget-manager** folder
5. Install dependencies like so:
  `python -m pip install -r requirements.txt`
6. Make migrations: 
  `python manage.py makemigrations`
7. Apply all migrations: 
  `python manage.py migrate`
8. Start the django server like so: `python manage.py runserver`