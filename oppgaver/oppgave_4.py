from oppgaver.utils import query, insert, insert_return_rowID

'''
Her skal du implementere et Pythonprogram (med bruk av SQL) som tar inn
en dato og skriver ut hvilke forestillinger som finnes på denne datoen og lister
opp hvor mange billetter (dvs. stoler) som er solgt. Ta også med forestillinger
hvor det ikke er solgt noen billetter.
'''

def forestiller_på_dato():

    dato = input('Hvilken dato for forestillinger og billetter? Format: YYYY-MM-DD, eksempel: 2024-02-03   ')

    data = query(f'''
        SELECT f.navnPaStykke, COUNT(b.forestillingID) AS antall_solgte_billetter
        FROM Forestilling f
        LEFT JOIN Billett b ON f.forestillingID = b.forestillingID
        WHERE f.dato = "{dato}"
        GROUP BY f.forestillingID, f.navnPaStykke
    ''')

    print(f'På datoen { dato } har vi følgende forestillinger:')
    for forestillingNavn, antall_solgte_billetter in data:
        print(f'{forestillingNavn}, med {antall_solgte_billetter} solgte billetter')

# forestiller_på_dato()

