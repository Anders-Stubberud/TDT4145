# import sqlite3
# from oppgaver.utils import query, insert, insert_return_rowID
# from random import randint

# def kjøpe_ni_voksenbilletter():

#     mobilnummer = randint(1, 100000000) # mulig sette inn denne profilen i SQL, og deretter hente den ut her?
#     insert('Kundeprofil', ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
#             (mobilnummer, 'dummy_fornavn', 'dummy_etternavn', '0010', 'slottsplassen', 1, 'Ordinær')
#     )

#     forestillingID = query(f'SELECT * FROM Forestilling WHERE navnPaStykke = "Størst av alt er kjærligheten" AND dato = "2024-02-03"')[0][0]
#     stykke = query(f'SELECT navnPaStykke FROM Forestilling NATURAL JOIN Teaterstykke WHERE forestillingID = { forestillingID }')[0][0]
#     sal = query(f"SELECT salnavn FROM Teaterstykke NATURAL JOIN Teatersal WHERE navnPaStykke = '{stykke}'")[0][0]
#     alle_ledige_stolIDer_og_ders_rad = query(f'SELECT stolID, radnummer FROM Stol Where stolID NOT IN (SELECT stolID from bestiltStol)')
#     radTilIDMapper = {}
#     ni_stoler = None
#     for stolID, rad in alle_ledige_stolIDer_og_ders_rad:
#         radTilIDMapper.setdefault(rad, []).append(stolID)
#         if radTilIDMapper[rad] and len(radTilIDMapper[rad]) == 9:
#             ni_stoler = radTilIDMapper[rad]
#             break
#     pris_voksenbillett = query(f'SELECT pris FROM kostnadForStykke WHERE gruppenavn = "Ordinær" AND navnPaStykke = "{ stykke }"')[0][0]
#     kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', mobilnummer))
#     for solgt_stol in ni_stoler:
#         billettID = insert_return_rowID('Billett', ('stolID', 'forestillingID', 'kjopsID'), (solgt_stol, forestillingID, kjøpsID))
#         insert('bestiltStol', ('billettID', 'stolID'), (billettID, solgt_stol))
#     print(f'Prisen for dine 9 voksenbilletter til { stykke } er: { 9 * pris_voksenbillett }')

# kjøpe_ni_voksenbilletter()

from oppgaver.utils import query, insert, insert_return_rowID
from random import randint

# Mulig implementasjon
def kjøpe_ni_voksenbilletter():
    mobilnummer = randint(1, 100000000)
    # Inserting a dummy customer profile directly
    insert('Kundeprofil', 
           ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
           (mobilnummer, 'dummy_fornavn', 'dummy_etternavn', '0010', 'slottsplassen', 1, 'Ordinær'))
    
    # Fetching details necessary for the ticket purchase
    forestilling_details = query('''
        SELECT f.forestillingID, ts.salnavn, k.pris
        FROM Forestilling f
        JOIN Teaterstykke ts ON f.navnPaStykke = ts.navnPaStykke
        JOIN kostnadForStykke k ON ts.navnPaStykke = k.navnPaStykke
        WHERE f.navnPaStykke = "Størst av alt er kjærligheten" 
        AND f.dato = "2024-02-03" 
        AND k.gruppenavn = "Ordinær"
    ''')[0]
    forestillingID, salnavn, pris_voksenbillett = forestilling_details
    
    # Selecting any nine available seats rather than finding nine consecutive seats
    available_seats = query('''
        SELECT stolID FROM Stol 
        WHERE stolID NOT IN (SELECT stolID FROM bestiltStol)
        LIMIT 9
    ''')

    if len(available_seats) < 9:
        print("Not enough available seats for the purchase.")
        return
    
    # Proceed with the purchase
    kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', mobilnummer))
    
    for stolID_tuple in available_seats:
        stolID = stolID_tuple[0]
        # Insert a ticket for each of the nine seats
        billettID = insert_return_rowID('Billett', ('stolID', 'forestillingID', 'kjopsID'), (stolID, forestillingID, kjøpsID))
        insert('bestiltStol', ('billettID', 'stolID'), (billettID, stolID))

    total_price = 9 * pris_voksenbillett
    print(f'Prisen for dine 9 voksenbilletter til forestillingen er: {total_price}')

# kjøpe_ni_voksenbilletter_optimized()
