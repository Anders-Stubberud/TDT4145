import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect('../database/database.db')
cursor = conn.cursor()

# Function to insert data into the database
def insert(table, columns, values):
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in values])
    query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
    cursor.execute(query, values)
    conn.commit()

# Function to insert data and return the row ID
def insert_return_rowID(table, columns, values):
    columns_str = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in values])
    query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
    cursor.execute(query, values)
    conn.commit()
    return cursor.lastrowid

# Function to execute SQL queries
def query(sql):
    cursor.execute(sql)
    return cursor.fetchall()

# Function to insert sold seats for Hovedscenen
def insert_solgte_stoler_hovedscenen():
    # Read sold seats data from file
    with open(os.path.join(os.path.dirname(__file__), '../filer/hovedscenen.txt'), 'r') as file:
        lines = file.readlines()
    # Extract sold seats
    sold_seats = ''.join([line.strip() for line in lines[lines.index('Parkett\n') + 1:]])[::-1]
    # Get the performance ID
    performance_id = query("SELECT forestillingID FROM (Teaterstykke NATURAL JOIN Forestilling) WHERE dato = '2024-02-03' AND salnavn = 'Hovedscenen'")[0][0]
    # Get seat IDs for sold seats
    sold_seat_ids = query(f"SELECT stolID FROM Stol WHERE stolnummer IN ({', '.join([str(i+1) for i, seat in enumerate(sold_seats) if seat == '1'])}) AND salnavn = 'Hovedscenen'")
    # Get purchase ID
    purchase_id = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', 12345678))
    # Insert sold seats
    for seat_id in sold_seat_ids:
        insert('Billett', ('stolID', 'forestillingID', 'kjopsID'), (seat_id[0], performance_id, purchase_id))

# Function to purchase tickets for Gamle scene
def purchase_tickets_gamle_scene():
    # SQL query to find available seats on the same row for Størst av alt er kjærligheten
    available_seats_query = """
        SELECT stolnummer
        FROM Billett AS b
        JOIN Stol AS s ON b.stolID = s.stolID
        JOIN Forestilling AS f ON b.forestillingID = f.forestillingID
        WHERE f.dato = '2024-02-03' AND f.tid = '18:30' AND f.navnPaStykke = 'Størst av alt er kjærligheten'
        GROUP BY s.radnummer
        HAVING COUNT(*) >= 9
    """

    # SQL query to calculate total cost
    total_cost_query = """
        SELECT COUNT(*) * pris AS total_cost
        FROM (
            SELECT stolnummer
            FROM Billett AS b
            JOIN Stol AS s ON b.stolID = s.stolID
            JOIN Forestilling AS f ON b.forestillingID = f.forestillingID
            WHERE f.dato = '2024-02-03' AND f.tid = '18:30' AND f.navnPaStykke = 'Størst av alt er kjærligheten'
            GROUP BY s.radnummer
            HAVING COUNT(*) >= 9
        ) AS available_seats
        JOIN Pris ON 1 = 1
    """

    # Execute the SQL queries
    cursor.execute(available_seats_query)
    available_seats = cursor.fetchall()

    cursor.execute(total_cost_query)
    total_cost = cursor.fetchone()[0]

    # Print the result
    print("Available seats:", available_seats)
    print("Total cost:", total_cost)

# Call functions to insert sold seats for Hovedscenen and purchase tickets for Gamle scene
insert_solgte_stoler_hovedscenen()
purchase_tickets_gamle_scene()

# Close the connection
conn.close()