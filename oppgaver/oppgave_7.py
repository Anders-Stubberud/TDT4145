from utils import query, insert

'''
Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner
hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og
hvilket skuespill det skjedde.
'''

def spiller_i_samme_akt(fornavn, etternavn):
    stykke_fornavn_og_etternavn_for_de_som_har_spilt_i_samme_stykke =query(f'''
        SELECT navnPaStykke, fornavn, etternavn
        FROM (
            SELECT navnPaStykke, nummer 
            FROM Skuespiller 
            NATURAL JOIN SpillerIAkt 
            WHERE fornavn = "{fornavn}" AND etternavn = "{etternavn}"
        )
        NATURAL JOIN SpillerIAkt NATURAL JOIN Skuespiller
        WHERE NOT (fornavn = "{fornavn}" AND etternavn = "{etternavn}")
    ''')
