import sqlite3

def kjop_billetter():
    conn = sqlite3.connect('./database/database.db')
    cursor = conn.cursor()

    # Find available seats in the same row with at least 9 seats available
    cursor.execute("""
        SELECT stolnummer, radnummer
        FROM Stol
        WHERE salnavn = 'Hovedscenen'
        GROUP BY radnummer
        HAVING COUNT(*) >= 9
        ORDER BY radnummer
        LIMIT 1
        """)
    seat_row = cursor.fetchone()
    if seat_row is None:
        print("Det er ingen rad med minst 9 ledige seter.")
        conn.close()
        return

    stolnummer, radnummer = seat_row
    print(f"Radnummer med minst 9 ledige seter: {radnummer}")

    # Find the price ID for the specified show
    cursor.execute("""
        SELECT prisID
        FROM KostnadForForestilling
        WHERE navnPaStykke = 'Størst av alt er kjærligheten'
        """)
    pris_id = cursor.fetchone()
    if pris_id is None:
        print("Det er ingen pris definert for denne forestillingen.")
        conn.close()
        return

    pris_id = pris_id[0]

    # Find the price for the show
    cursor.execute("SELECT pris FROM Pris WHERE prisID = ?", (pris_id,))
    pris = cursor.fetchone()
    if pris is None:
        print("Det er ingen pris definert for denne forestillingen.")
        conn.close()
        return

    pris = pris[0]

    total_pris = pris * 9

    conn.close()

    return total_pris

# Kjøp 9 voksenbilletter til forestillingen "Størst av alt er kjærligheten" den 3. februar
total_pris = kjop_billetter()
if total_pris is not None:
    print(f"Totalpris for 9 voksenbilletter: {total_pris} kr")
