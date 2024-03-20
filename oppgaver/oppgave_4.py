from utils import query, insert, insert_return_rowID

def forestiller_på_dato():

    dato = input('Hvilken dato for forestillinger og billetter? Format: YYYY-MM-DD, eksempel: 2024-02-03   ')
    data = query(f'SELECT forestillingID, navnPaStykke FROM Forestilling WHERE dato = "{ dato }"')
    forestillingNavnTilIDMapper = {}
    for forestillingID, forestillingNavn in data:
        count = query(f'SELECT COUNT(*) FROM Billett WHERE forestillingID = { forestillingID }')[0][0]
        forestillingNavnTilIDMapper[forestillingNavn] = forestillingNavnTilIDMapper.get(forestillingNavn, 0) + count
    print(f'På datoen { dato } har vi følgende forestillinger:')
    for forestilling, antall_solgte_billetter in forestillingNavnTilIDMapper.items():
        print(f'{forestilling}: {antall_solgte_billetter}')

forestiller_på_dato()
