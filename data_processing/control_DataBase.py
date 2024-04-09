from data_processing.modules import connect, exists

def Data_Base():
    # Check if the database file exists
    if not exists('gym.db'):
        # Create a new database file and connect to it
        conn = connect('gym.db')
        c = conn.cursor()

        # Create a users table
        c.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone TEXT,
                gender TEXT,
                birth_date TEXT,
                address TEXT,
                height REAL,
                weight REAL,
                duration INTEGER,
                date TEXT
            )
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    else:
        # If the database file exists, connect to it
        conn = connect('gym.db')
        c = conn.cursor()

        # Close the connection
        conn.close()