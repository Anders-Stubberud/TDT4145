import sqlite3

def kjop_billetter():
    conn = sqlite3.connect('./database/database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT forestillingID FROM Forestilling WHERE navnPaStykke = 'Størst av alt er kjærligheten' AND dato = '2024-02-03'")
    forestilling_result = cursor.fetchone()
    if forestilling_result is None:
        print("Det er ingen forestilling som matcher kriteriene.")
        conn.close()
        return

    forestilling_id = forestilling_result[0]

    cursor.execute("SELECT prisID FROM KostnadForForestilling WHERE navnPaStykke = 'Størst av alt er kjærligheten'")
    pris_result = cursor.fetchone()
    if pris_result is None:
        print("Det er ingen pris definert for denne forestillingen.")
        conn.close()
        return

    pris_id = pris_result[0]

    cursor.execute("SELECT pris FROM Pris WHERE prisID = ?", (pris_id,))
    pris = cursor.fetchone()[0]

    total_pris = pris * 9

    conn.close()

    return total_pris

# Kjøp 9 voksenbilletter til forestillingen "Størst av alt er kjærligheten" den 3. februar
total_pris = kjop_billetter()
print(f"Totalpris for 9 voksenbilletter: {total_pris} kr")