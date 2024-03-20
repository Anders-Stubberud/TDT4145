import sqlite3
from utils import query, insert, insert_return_rowID

# Connect to the SQLite database
conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

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
        SELECT COUNT(*) * p.pris AS total_cost
        FROM (
            SELECT s.stolnummer
            FROM Billett AS b
            JOIN Stol AS s ON b.stolID = s.stolID
            JOIN Forestilling AS f ON b.forestillingID = f.forestillingID
            WHERE f.dato = '2024-02-03' AND f.tid = '18:30' AND f.navnPaStykke = 'Størst av alt er kjærligheten'
            GROUP BY s.radnummer
            HAVING COUNT(*) >= 9
        ) AS available_seats
        JOIN Teaterstykke AS ts ON ts.navnPaStykke = 'Størst av alt er kjærligheten'
        JOIN Pris AS p ON p.prisID = ts.prisID
    """

    # Execute the SQL queries
    cursor.execute(available_seats_query)
    available_seats = cursor.fetchall()

    cursor.execute(total_cost_query)
    total_cost = cursor.fetchone()[0]

    # Print the result
    print("Available seats:", available_seats)
    print("Total cost:", total_cost)

# Call function to purchase tickets for Gamle scene
purchase_tickets_gamle_scene()

# Close the connection
conn.close()