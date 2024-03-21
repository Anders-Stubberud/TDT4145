from oppgaver.utils import query


'''
Vi ønsker å lage et query i SQL som finner hvilke (navn på) skuespillere som
opptrer i de forskjellige teaterstykkene. Skriv ut navn på teaterstykke, navn på
skuespiller og rolle
'''

def skuespillere_i_stykker():
    data = query('SELECT navnPaStykke, fornavn, etternavn, navn FROM Teaterstykke NATURAL JOIN Rolle NATURAL JOIN SpillerRolle NATURAL JOIN Skuespiller ORDER BY navnPaStykke')

    # Organisere data med skuespill
    stykker_med_skuespillere = {}
    for navn_på_stykke, fornavn, etternavn, rolle_navn in data:
        fullt_navn = f'{fornavn} {etternavn}'
        if navn_på_stykke not in stykker_med_skuespillere:
            stykker_med_skuespillere[navn_på_stykke] = []
        stykker_med_skuespillere[navn_på_stykke].append((fullt_navn, rolle_navn))

    # Printe header
    header = f'{"Forestilling":<35} {"Skuespiller":<25} {"Rolle":<30}'
    print(" " * 4 + header)
    print(" " * 4 + '-' * len(header))

    # Printe ut data
    stykker = list(stykker_med_skuespillere.keys())
    for i, stykke in enumerate(stykker):
        for j, (skuespiller, rolle) in enumerate(stykker_med_skuespillere[stykke]):
            if j == 0:
                if i > 0:
                    print()  
                print(" " * 4 + f'{stykke:<35} {skuespiller:<25} {rolle:<30}')
            else:
                print(" " * 4 + f'{" ":<35} {skuespiller:<25} {rolle:<30}')

