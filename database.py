from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Employee, MenuItem, MenuItemType, Menu, Table

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create an employee
    employee = Employee(name="Margot", employee_number=1234, password="password")

    # Create menu item types
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    # Create menus
    breakfast = Menu(name="Breakfast")
    lunch = Menu(name="Lunch")
    dinner = Menu(name="Dinner")
    drinks = Menu(name="Drinks")
    specials = Menu(name="Specials")
    kids = Menu(name="Kids")
    appetizers = Menu(name="Appetizers")
    salads = Menu(name="Salads")
    soups = Menu(name="Soups")

    # Create menu items
    fries = MenuItem(name="French fries", price=3.50, menu_type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, menu_type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, menu_type=entrees, menu=dinner)
    pancakes = MenuItem(name="Pancakes", price=5.99, menu_type=entrees, menu=breakfast)
    coffee = MenuItem(name="Coffee", price=2.50, menu_type=beverages, menu=breakfast)
    burger = MenuItem(name="Burger", price=8.99, menu_type=entrees, menu=lunch)
    salad = MenuItem(name="Caesar Salad", price=7.99, menu_type=entrees, menu=salads)
    soup = MenuItem(name="Tomato Soup", price=4.99, menu_type=entrees, menu=soups)
    steak = MenuItem(name="Steak", price=25.99, menu_type=entrees, menu=dinner)
    
    table1 = Table(number=1, capacity=4)
    table2 = Table(number=1, capacity=4)
    table3 = Table(number=1, capacity=4)
    table4 = Table(number=1, capacity=4)
    table5 = Table(number=1, capacity=4)
    table6 = Table(number=1, capacity=4)
    table7 = Table(number=1, capacity=4)
    table8 = Table(number=1, capacity=4)
    table9 = Table(number=1, capacity=4)
    table10 = Table(number=1, capacity=4)


    # Add all instances to the session
    db.session.add(employee)
    db.session.add(beverages)
    db.session.add(entrees)
    db.session.add(sides)
    db.session.add(breakfast)
    db.session.add(lunch)
    db.session.add(dinner)
    db.session.add(drinks)
    db.session.add(specials)
    db.session.add(kids)
    db.session.add(appetizers)
    db.session.add(salads)
    db.session.add(soups)
    db.session.add(fries)
    db.session.add(drp)
    db.session.add(jambalaya)
    db.session.add(pancakes)
    db.session.add(coffee)
    db.session.add(burger)
    db.session.add(salad)
    db.session.add(soup)
    db.session.add(steak)
    
    db.session.add(table1)
    db.session.add(table2)
    db.session.add(table3)
    db.session.add(table4)
    db.session.add(table5)
    db.session.add(table6)
    db.session.add(table7)
    db.session.add(table8)
    db.session.add(table9)
    db.session.add(table10)

    # Commit the session to save the data to the database
    db.session.commit()