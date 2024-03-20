import os
from utils import query, insert, insert_return_rowID

def insert_solgte_stoler_hovedscenen():

    # oppretter ett billettkjøp som alle billetter registreres mot
    kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', 12345678))

    lines = None
    with open(os.path.join(os.path.dirname(__file__), '../filer/hovedscenen.txt'), 'r') as file:
        lines = file.readlines()
    stoler_fra_nummer_en = ''.join([rad.strip() for rad in lines[lines.index('Parkett\n') + 1:]][::-1])
    solgte_stoler = [stolindex + 1 for stolindex, solgt in enumerate(stoler_fra_nummer_en) if solgt == '1']
    stol_IDer_solgte_stoler_hovedscenen_tupler = query(f'SELECT stolnummer FROM Stol WHERE (stolnummer IN ({", ".join(map(str, solgte_stoler))}) AND salnavn = "Hovedscenen")')
    stol_IDer_solgte_stoler_hovedscenen = [solgt_stol[0] for solgt_stol in stol_IDer_solgte_stoler_hovedscenen_tupler]
    forestillingID_tuppel = query(f'SELECT forestillingID FROM (Teaterstykke NATURAL JOIN Forestilling) where dato = "2024-02-03" AND salnavn ="Hovedscenen"')
    forestillingID = forestillingID_tuppel[0][0]
    for solgt_stol_ID in stol_IDer_solgte_stoler_hovedscenen:
        billettID = insert_return_rowID('Billett', ('stolID', 'forestillingID', 'kjopsID'), (solgt_stol_ID, forestillingID, kjøpsID))
        insert('bestiltStol', ('billettID', 'stolID'), (billettID, solgt_stol_ID))

insert_solgte_stoler_hovedscenen()
