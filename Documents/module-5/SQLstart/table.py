

# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     signup_date DATE DEFAULT CURRENT_DATE
# );

# INSERT INTO users (id, name, email) VALUES
# (1, 'Sofia Ramirez', 'sofia.ramirez@example.com'),
# (2, 'Devon Blake', 'devon.blake@example.com');

# UPDATE users
# SET email = 'devon.blake@newdomain.com'
# WHERE id = 2;

# DELETE FROM users
# WHERE name = 'Test User';

import sqlite3
import pandas as pd

con = sqlite3.connect('example.db')
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        signup_date DATE DEFAULT CURRENT_DATE
    );  
""")
cursor.execute("""
    ALTER TABLE users ADD COLUMN phone_number TEXT;
""")

# And to remove a table entirely:

cursor.execute("""
    DROP TABLE users;
""")
con.commit()

con.close()