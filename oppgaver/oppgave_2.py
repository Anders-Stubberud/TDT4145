import os
from oppgaver.utils import query, insert, insert_return_rowID
from random import randint

def insert_solgte_stoler_hovedscenen():

    mobilnummer = randint(1, 10000000000)
    insert('Kundeprofil', ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
            (mobilnummer, 'dummy_fornavn', 'dummy_etternavn', '0010', 'slottsplassen', 1, 'Ordinær')
    )

    # oppretter kundeprofil billettKjøp registeres mot
    # oppretter ett billettkjøp som alle billetter registreres mot
    kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', mobilnummer))

    lines = None
    with open(os.path.join(os.path.dirname(__file__), '../filer/hovedscenen.txt'), 'r') as file:
        lines = file.readlines()
    stoler_fra_nummer_en = ''.join([rad.strip() for rad in lines[lines.index('Parkett\n') + 1:]][::-1])
    solgte_stoler = [stolindex + 1 for stolindex, solgt in enumerate(stoler_fra_nummer_en) if solgt == '1']
    stol_IDer_solgte_stoler_hovedscenen_tupler = query(f'SELECT stolID FROM Stol WHERE (stolnummer IN ({", ".join(map(str, solgte_stoler))}) AND salnavn = "Hovedscenen")')
    stol_IDer_solgte_stoler_hovedscenen = [solgt_stol[0] for solgt_stol in stol_IDer_solgte_stoler_hovedscenen_tupler]
    forestillingID_tuppel = query(f'SELECT forestillingID FROM (Teaterstykke NATURAL JOIN Forestilling) where dato = "2024-02-03" AND salnavn ="Hovedscenen"')
    forestillingID = forestillingID_tuppel[0][0]
    for solgt_stol_ID in stol_IDer_solgte_stoler_hovedscenen:
        billettID = insert_return_rowID('Billett', ('stolID', 'forestillingID', 'kjopsID'), (solgt_stol_ID, forestillingID, kjøpsID))
        insert('bestiltStol', ('billettID', 'stolID'), (billettID, solgt_stol_ID))

def insert_solgte_stoler_gamle_scene():

    mobilnummer = randint(1, 10000000000)
    insert('Kundeprofil', ('mobilnummer', 'fornavn', 'etternavn', 'postnummer', 'gatenavn', 'gatenummer', 'gruppenavn'), 
            (mobilnummer, 'dummy_fornavn', 'dummy_etternavn', '0010', 'slottsplassen', 1, 'Ordinær')
    )

    kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-02', '12:00', mobilnummer))

    # oppretter ett billettkjøp som alle billetter registreres mot
    # kjøpsID = insert_return_rowID('BillettKjop', ('dato', 'tid', 'mobilnummer'), ('2024-01-01', '12:00', mobilnummer))
    lines = None
    with open(os.path.join(os.path.dirname(__file__), '../filer/gamle-scene.txt'), 'r') as file:
        lines = file.readlines()

    galleri = [rad.strip() for rad in lines[lines.index('Galleri\n') + 1 : lines.index('Balkong\n')]][::-1]
    balkong = [rad.strip() for rad in lines[lines.index('Balkong\n') + 1 : lines.index('Parkett\n')]][::-1]
    parkett = [rad.strip() for rad in lines[lines.index('Parkett\n') + 1 : ]][::-1]

    solgte_stoler = (
        [('Gamle scene', 'Galleri', rad_index + 1, stol_index + 1) for rad_index, rad in enumerate(galleri) for stol_index, solgt in enumerate(rad) if solgt == '1'] +
        [('Gamle scene', 'Balkong', rad_index + 1, stol_index + 1) for rad_index, rad in enumerate(balkong) for stol_index, solgt in enumerate(rad) if solgt == '1'] +
        [('Gamle scene', 'Parkett', rad_index + 1, stol_index + 1) for rad_index, rad in enumerate(parkett) for stol_index, solgt in enumerate(rad) if solgt == '1']
    )

    formatted_strings = [f'("{row[0]}", "{row[1]}", {row[2]}, {row[3]})' for row in solgte_stoler]
    comma_separated_string = ", ".join(formatted_strings)
    forestillingID_tuppel = query(f'SELECT forestillingID FROM (Teaterstykke NATURAL JOIN Forestilling) where dato = "2024-02-03" AND salnavn ="Gamle scene"')
    forestillingID = forestillingID_tuppel[0][0]
    ID_solgte_stoler_gamle_scene_tupler = query(f'SELECT stolID FROM (Stol NATURAL JOIN Omraade) WHERE (salnavn, omraadenavn, radnummer, stolnummer) IN ({comma_separated_string})')
    ID_solgte_stoler_gamle_scene = [solgt_stol[0] for solgt_stol in ID_solgte_stoler_gamle_scene_tupler]
    for solgt_stol_ID in ID_solgte_stoler_gamle_scene:
        billettID = insert_return_rowID('Billett', ('stolID', 'forestillingID', 'kjopsID'), (solgt_stol_ID, forestillingID, kjøpsID))
        insert('bestiltStol', ('billettID', 'stolID'), (billettID, solgt_stol_ID))

# insert_solgte_stoler_hovedscenen()
# insert_solgte_stoler_gamle_scene()
