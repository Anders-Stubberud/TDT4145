from oppgaver.utils import query, insert, insert_return_rowID


'''
Vi ønsker å lage et query i SQL som finner hvilke (navn på) skuespillere som
opptrer i de forskjellige teaterstykkene. Skriv ut navn på teaterstykke, navn på
skuespiller og rolle
'''
# stykke, skuespiller rolle

# def skuespillere_i_stykker():
#     data = query(f'SELECT navnPaStykke, fornavn, etternavn, navn FROM Teaterstykke NATURAL JOIN Rolle NATURAL JOIN SpillerRolle NATURAL JOIN Skuespiller')
#     for navn_på_stykke, fornavn, etternavn, rolle_navn in data:
#         print(f'{ fornavn } { etternavn } spiller { rolle_navn } i { navn_på_stykke }')


def skuespillere_i_stykker():
    data = query('SELECT navnPaStykke, fornavn, etternavn, navn FROM Teaterstykke NATURAL JOIN Rolle NATURAL JOIN SpillerRolle NATURAL JOIN Skuespiller ORDER BY navnPaStykke')

    # Organize data by play
    stykker_med_skuespillere = {}
    for navn_på_stykke, fornavn, etternavn, rolle_navn in data:
        fullt_navn = f'{fornavn} {etternavn}'
        if navn_på_stykke not in stykker_med_skuespillere:
            stykker_med_skuespillere[navn_på_stykke] = []
        stykker_med_skuespillere[navn_på_stykke].append((fullt_navn, rolle_navn))

    # Prepare and print the header
    header = f'{"Forestilling":<35} {"Skuespiller":<25} {"Rolle":<30}'
    print(header)
    print('-' * len(header))

    # Print the organized data with spacing between different plays
    plays = list(stykker_med_skuespillere.keys())
    for i, stykke in enumerate(plays):
        for j, (skuespiller, rolle) in enumerate(stykker_med_skuespillere[stykke]):
            if j == 0:
                # For the first actor of each play, add a newline if it's not the first play
                if i > 0:
                    print()  # Adds a newline for spacing between plays
                print(f'{stykke:<35} {skuespiller:<25} {rolle:<30}')
            else:
                print(f'{" ":<35} {skuespiller:<25} {rolle:<30}')

# skuespillere_i_stykker()

# print(query(f''))

