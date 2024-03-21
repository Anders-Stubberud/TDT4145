
from oppgaver.utils import query, insert, insert_return_rowID
from random import randint

'''
Her skal du kjøpe 9 voksenbilletter til forestillingen for Størst av alt er
kjærligheten 3. februar, hvor det er 9 ledige billetter og hvor stolene er på
samme rad. Stolene trenger ikke være ved siden av hverandre. Vi ønsker å få
summert hva det koster å kjøpe disse billettene, men du trenger ikke ta
hensyn til selve betalingen, den antar vi skjer på et annet system som dere
ikke trenger å lage. Denne funksjonen skal implementeres i Python og SQL.
'''

def kjøpe_ni_voksenbilletter():

    # dummy mobilnummer til dummy kundeprofil, ønsker ikke autoincrement ettersom hver bruker skal ha mobilnummer fra før
    mobilnummer = randint(10000000, 99999999)

    insert('Kundeprofil', 
           ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
           (mobilnummer, 'dummy_fornavn', 'dummy_etternavn', '0010', 'slottsplassen', 1, 'Ordinær'))
    
    forestilling_detaljer = query('''
        SELECT f.forestillingID, ts.salnavn, k.pris
        FROM Forestilling f
        JOIN Teaterstykke ts ON f.navnPaStykke = ts.navnPaStykke
        JOIN kostnadForStykke k ON ts.navnPaStykke = k.navnPaStykke
        WHERE f.navnPaStykke = "Størst av alt er kjærligheten" 
        AND f.dato = "2024-02-03" 
        AND k.gruppenavn = "Ordinær"
    ''')[0]
    forestillingID, _, pris_voksenbillett = forestilling_detaljer
    
    ledige_seter = query('''
        SELECT stolID FROM Stol 
        WHERE stolID NOT IN (SELECT stolID FROM bestiltStol)
        AND radnummer = (
            SELECT radnummer FROM (
                SELECT radnummer, COUNT(*) AS available_seats_count 
                FROM Stol 
                WHERE stolID NOT IN (SELECT stolID FROM bestiltStol)
                GROUP BY radnummer
                ORDER BY available_seats_count DESC
                LIMIT 1
            )
        )
        LIMIT 9
    ''')

    if len(ledige_seter) < 9:
        print("Not enough available seats for the purchase.")
        return
    
    kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', mobilnummer))
    
    for stolID_tuple in ledige_seter:
        stolID = stolID_tuple[0]
        billettID = insert_return_rowID('Billett', ('stolID', 'forestillingID', 'kjopsID'), (stolID, forestillingID, kjøpsID))
        insert('bestiltStol', ('billettID', 'stolID'), (billettID, stolID))

    total_price = 9 * pris_voksenbillett
    print(f'    Prisen for dine 9 voksenbilletter til forestillingen er: {total_price}')
