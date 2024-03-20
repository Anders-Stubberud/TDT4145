import sqlite3
from utils import query, insert, insert_return_rowID
from random import randint

def kjøpe_ni_voksenbilletter():

    mobilnummer = randint(1, 100000000) # mulig sette inn denne profilen i SQL, og deretter hente den ut her?
    insert('Kundeprofil', ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
            (mobilnummer, 'dummy_fornavn', 'dummy_etternavn', '0010', 'slottsplassen', 1, 'Ordinær')
    )

    forestillingID = query(f'SELECT forestillingID FROM Forestilling WHERE navnPaStykke = "Størst av alt er kjærligheten" AND dato = "2024-02-03"')[0][0]
    stykke = query(f'SELECT navnPaStykke FROM Forestilling NATURAL JOIN Teaterstykke WHERE forestillingID = { forestillingID }')[0][0]
    sal = query(f"SELECT salnavn FROM Teaterstykke NATURAL JOIN Teatersal WHERE navnPaStykke = '{stykke}'")[0][0]
    alle_ledige_stolIDer_og_ders_rad = query(f'SELECT stolID, radnummer FROM Stol Where stolID NOT IN (SELECT stolID from bestiltStol)')
    radTilIDMapper = {}
    ni_stoler = None
    for stolID, rad in alle_ledige_stolIDer_og_ders_rad:
        radTilIDMapper.setdefault(rad, []).append(stolID)
        if radTilIDMapper[rad] and len(radTilIDMapper[rad]) == 9:
            ni_stoler = radTilIDMapper[rad]
            break
    pris_voksenbillett = query(f'SELECT pris FROM kostnadForStykke WHERE gruppenavn = "ordinær" AND navnPaStykke = "{ stykke }"')
    kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', mobilnummer))
    for solgt_stol in ni_stoler:
        billettID = insert_return_rowID('Billett', ('stolID', 'forestillingID', 'kjopsID'), (solgt_stol, forestillingID, kjøpsID))
        insert('bestiltStol', ('billettID', 'stolID'), (billettID, solgt_stol))
    print(f'Prisen for dine 9 voksenbilletter til { stykke } er: { 9 * pris_voksenbillett }')

kjøpe_ni_voksenbilletter()
