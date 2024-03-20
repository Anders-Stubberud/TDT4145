from utils import query, insert, insert_return_rowID


'''
Vi ønsker å lage et query i SQL som finner hvilke (navn på) skuespillere som
opptrer i de forskjellige teaterstykkene. Skriv ut navn på teaterstykke, navn på
skuespiller og rolle
'''
# stykke, skuespiller rolle

def skuespillere_i_stykker():
    data = query(f'SELECT navnPaStykke, fornavn, etternavn, navn FROM Teaterstykke NATURAL JOIN Rolle NATURAL JOIN SpillerRolle NATURAL JOIN Skuespiller')
    for navn_på_stykke, fornavn, etternavn, rolle_navn in data:
        print(f'{ fornavn } { etternavn } spiller { rolle_navn } i { navn_på_stykke }')

skuespillere_i_stykker()

# print(query(f''))

