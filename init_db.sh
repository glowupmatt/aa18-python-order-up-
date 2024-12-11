#!/bin/sh

# Wait for the database to be ready
sleep 5

# Run the SQL commands
flask db upgrade

# Optionally, you can add more SQL commands here
# For example, to seed the database
python database.py