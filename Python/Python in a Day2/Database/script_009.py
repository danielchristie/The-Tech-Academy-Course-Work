import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')
cursor = conn.execute

# Create the table
conn.execute("CREATE TABLE IF NOT EXISTS SIMPSON_INFO( \
     ID INTEGER PRIMARY KEY AUTOINCREMENT, \
     NAME           TEXT        NOT NULL,\
     GENDER         TEXT        NOT NULL,\
     AGE            INT         NOT NULL,\
     OCCUPATION     TEXT        NOT NULL \
     );")

# Save changes
conn.commit()

# Add Data to the table
conn.execute('''INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Bart Simpson', 'Male', 10, 'Student')''')
conn.execute('''INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Homer Simpson', 'Male', 42, 'Parent')''')
conn.execute('''INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Lisa Simpson', 'Female', 8, 'Student')''')
conn.execute('''INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Marge Simpson', 'Female', 40, 'Parent')''')

# Save changes
conn.commit()

# Print number of changes
changes = conn.total_changes
print "Number of changes: ",changes

# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Extract data from cursor
rows = cursor.fetchall()
print rows

# Searching for females
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where GENDER='Female'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Females:'
print rows

# Searching for students
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where OCCUPATION='Student'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Students:'
print rows

# Searching by character name
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where NAME='Homer Simpson'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Homer Simpson:'
print rows

# Close the Database Connection
conn.close()
