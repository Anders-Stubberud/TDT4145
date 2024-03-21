from utils import query, insert

'''
Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner
hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og
hvilket skuespill det skjedde.
'''

def spiller_i_samme_akt(fornavn, etternavn):

    # Med eller uten duplikater? spiller jo i samme akt med flere av folkene flere ganger, inkludere hvilken akt det var?
    stykke_fornavn_og_etternavn_for_de_som_har_spilt_i_samme_stykke =query(f'''
        SELECT DISTINCT navnPaStykke, fornavn, etternavn
        FROM (
            SELECT navnPaStykke, nummer
            FROM
            Skuespiller NATURAL JOIN spillerRolle NATURAL JOIN Rolle NATURAL JOIN rolleIAkt NATURAL JOIN Akt
            WHERE fornavn = "{ fornavn }" AND etternavn = "{ etternavn }"                    
        )
        NATURAL JOIN rolleIAkt NATURAL JOIN Rolle NATURAL JOIN spillerRolle NATURAL JOIN Skuespiller
        WHERE NOT (fornavn = "{ fornavn }" AND etternavn = "{ etternavn }")
    ''')

    for navn_på_stykke, fornavn_medskuespiller, etternavn_medskuespiller in stykke_fornavn_og_etternavn_for_de_som_har_spilt_i_samme_stykke:
        print(f'{fornavn} {etternavn} spilte i samme akt som {fornavn_medskuespiller} {etternavn_medskuespiller} i {navn_på_stykke}')

spiller_i_samme_akt("Jo", "Saberniak")
        
