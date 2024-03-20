import sqlite3
from utils import query, insert  # Removed unnecessary import statement
# from utils import skuespillereIStykkerQuery, forestillingerRangertQuery, forestillingerPaaDatoQuery

con = sqlite3.connect("teater.db")
c = con.cursor()

def kjop_ni_billetter(forestilling_dato="2024-02-03 18:30:00", stykkeID=2, kundegruppeID="O", antall_billetter=9):
    # Identifiser ledige stoler ved å sjekke mot de som allerede er solgt
    c.execute("""
        SELECT Stol.RadNr, Stol.Omrade, COUNT(Stol.StolNr) AS LedigeSeter
        FROM Stol
        LEFT JOIN Billett ON Stol.StolNr = Billett.StolNr AND Stol.RadNr = Billett.RadNr AND Stol.Omrade = Billett.Omrade
        LEFT JOIN BilettKjop ON Billett.ReferanseNr = BilettKjop.ReferanseNr
        LEFT JOIN Forestilling ON BilettKjop.Tidspunkt = Forestilling.Tidspunkt
        WHERE Forestilling.Tidspunkt IS NULL OR Forestilling.Tidspunkt != ?
        AND NOT EXISTS (SELECT * FROM Billett WHERE Billett.RadNr = Stol.RadNr AND Billett.StolNr = Stol.StolNr AND Billett.Omrade = Stol.Omrade AND Billett.SalID = Stol.SalID)
        GROUP BY Stol.RadNr, Stol.Omrade
        HAVING COUNT(Stol.StolNr) - COUNT(Billett.StolNr) >= ?;
    """, (forestilling_dato, antall_billetter))

    ledige_stoler = c.fetchall()
    print(ledige_stoler)

    # Gruppere ledige stoler etter RadNr og finne en rad med minst 9 ledige stoler
    rad_med_ledige_stoler = {}
    for stol in ledige_stoler:
        rad_nr = stol[1]
        rad_med_ledige_stoler.setdefault(rad_nr, []).append(stol)

    rad_for_kjop = None
    for rad_nr, stoler in rad_med_ledige_stoler.items():
        if len(stoler) >= antall_billetter:
            rad_for_kjop = rad_nr
            break

    if not rad_for_kjop:
        print("Fant ikke en rad med nok ledige stoler.")
        return

    # Kjøpe billetter for stolene på valgte rad
    valgte_stoler = rad_med_ledige_stoler[rad_for_kjop][:antall_billetter]
    for stol in valgte_stoler:
        referanse_nr = f"{forestilling_dato.replace('-', '')}{stykkeID}{stol[1]}{stol[0]}"
        c.execute('INSERT INTO BilettKjop (ReferanseNr, Tidspunkt, KundeNr) VALUES (?, ?, ?)',
                  (referanse_nr, forestilling_dato, 1))
        c.execute('INSERT INTO Billett (ReferanseNr, StolNr, RadNr, Omrade, SalID) VALUES (?, ?, ?, ?, ?)',
                  (referanse_nr, stol[0], stol[1], stol[2], stol[3]))

    # Beregne totalprisen for billettene
    c.execute('SELECT Pris FROM TypeBillett WHERE KundegruppeID = ? AND StykkeID = ?', (kundegruppeID, stykkeID))
    pris_per_billett = c.fetchone()[0]
    totalpris = pris_per_billett * antall_billetter

    con.commit()
    print(f"Kjøpte {antall_billetter} billetter til 'Størst av alt er kjærligheten' den {forestilling_dato}. Totalpris: {totalpris} NOK.")

if __name__ == '__main__':
    kjop_ni_billetter()