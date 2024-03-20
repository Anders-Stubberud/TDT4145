import sqlite3
from utils import insert

# stol_id_counter = 1  # Initialize a counter for stol_id

def insert_stoler_Hovedscenen():
    row = 1
    for seat in range(1, 505):
        if (466 < seat and seat < 471) or (494 < seat < 499):
            continue
        insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, 'Hovedscenen', 1))
        row = row + 1 if seat  % 28 == 0 else row

def insert_stoler_Parkett(sal, rows_parkett):
    for row in range(1, rows_parkett + 1):
        if row in [1, 4, 5, 7]:
            seats = 18
        elif row == 2:
            seats = 16
        elif row == 10:
            seats = 14
        else:
            seats = 17
        for seat in range(1, seats + 1):
            insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, sal, 1))

def insert_stoler_Balkong(sal, rows_balkong):
    for row in range(1, rows_balkong + 1):
        if row == 1:
            seats = 28
        elif row == 2:
            seats = 27
        elif row == 3:
            seats = 22
        else:
            seats = 17
        for seat in range(1, seats + 1):
            insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, sal, 2))

def insert_stoler_Galleri(sal, rows_galleri):
    for row in range(1, rows_galleri + 1):
        if row == 1:
            seats = 33
        elif row == 2:
            seats = 18
        else:
            seats = 17
        for seat in range(1, seats + 1):
            insert('Stol', ('stolnummer', 'radnummer', 'salnavn', 'omraadeID'), (seat, row, sal, 3))

def insert_teaterstykker():
    teaterstykke_data = [('Kongsemnene', 'Hovedscenen', '19:00'), ('Størst av alt er kjærligheten', 'Gamle scene', '18:30')]
    for stykke, sal, tid in teaterstykke_data:
        insert('Teaterstykke', ('navnPaStykke', 'salnavn', 'klokkeslett'), (stykke, sal, tid))


def insert_roller():
    rolle_data_kongsemnene = [
        'Haakon Haakonssønn', 'Inga fra Vartejg', 'Skule jarl', 'Fru Ragnhild', 'Margrete',
        'Sigrid', 'Biskop Nikolas', 'Gregorius Jonssønn', 'Paal Flida', 'Trønder', 'Baard Bratte',
        'Jatgeir Skald', 'Dagfinn Bonde', 'Peter'
    ]
    rolle_data_størst_av_alt_er_kjærligheten = [
    'Sunniva Du Mond Nordal', 'Jo Saberniak', 'Marte M. Steinholt', 'Tor Ivar Hagen', 'Trond-Ove Skrødal',
    'Natalie Grøndahl Tangen', 'Åsmund Flaten'
    ]
    for rolle in rolle_data_størst_av_alt_er_kjærligheten:
        insert('Rolle', ('navn', 'navnPaStykke'), (rolle, 'Størst av alt er kjærligheten'))
    for rolle in rolle_data_kongsemnene:
        insert('Rolle', ('navn', 'navnPaStykke'), (rolle, 'Kongsemnene'))


def insert_skuespiller():
    skuespiller_data_kongsemene = [
        ('Arturo', 'Scotti'), ('Ingunn Beate Strige', 'Øyen'), ('Hans Petter', 'Nilsen'), ('Madeleine Brandtzæg', 'Nilsen'),
        ('Synnøve Fossum', 'Eriksen'), ('Emma Caroline', 'Deichmann'), ('Thomas Jensen', 'Takyi'), ('Per Bogstad', 'Gulliksen'),
        ('Isak Holmen', 'Sørensen'), ('Fabian Heidelberg', 'Lunde'), ('Emil', 'Olafsson'), ('Snorre Ryen', 'Tøndel')
    ]
    Skuespiller_data_størst_av_alt_er_kjærligheten = [
        ('Sunniva Du Mond', 'Nordal'), ('Jo', 'Saberniak'), ('Marte M.', 'Steinholt'), ('Tor Ivar', 'Hagen'), ('Trond-ove', 'Skrødal'),
        ('Natalie Grøndahl', 'Tangen'), ('Åsmund', 'Flaten')
    ]
    for fornavn, etternavn in skuespiller_data_kongsemene:
        insert('Skuespiller', ('fornavn', 'etternavn'), (fornavn, etternavn))
    for fornavn, etternavn in Skuespiller_data_størst_av_alt_er_kjærligheten:
        insert('Skuespiller', ('fornavn', 'etternavn'), (fornavn, etternavn))

def insertSpillerRolle():
    

def insert_saler():
    insert('Teatersal', ['salnavn'], ['Hovedscenen'])
    insert('Teatersal', ['salnavn'], ['Gamle scene'])

def insert_område():
    områder = ['Parkett', 'Balkong', 'Galleri']
    for område in områder:
        insert('Omraade', ['omraadenavn'], [område])

def insert_forestillinger():
    datoer_kongsemnene = [
        '2024-02-01', '2024-02-02', '2024-02-03', '2024-02-05', '2024-02-06' # YYYY-MM-DD
    ]
    datoer_størst_av_alt_er_kjærligheten = [
        '2024-02-03', '2024-02-06', '2024-02-07', '2024-02-12', '2024-02-13', '2024-02-14'
    ]
    for dato in datoer_kongsemnene:
        insert('Forestilling', ('dato', 'tid', 'navnPaStykke'), (dato, '19:00', 'Kongsemnene'))
    for dato in datoer_størst_av_alt_er_kjærligheten:
        insert('Forestilling', ('dato', 'tid', 'navnPaStykke'), (dato, '18:30', 'Størst av alt er kjærligheten'))

def insert_akter():
    for i in range(1, 6):
        insert('Akt', ('navnPaStykke', 'nummer', 'navn'), ('Kongsemnene', i, 'ukjent'))
    insert('Akt', ('navnPaStykke', 'nummer', 'navn'), ('Størst av alt er kjærligheten', 1, 'ukjent'))

def insert_oppgaver():
    oppgaver = ['Regi', 'Scenografi og kostymer', 'Musikalsk ansvarlig', 'Lysdesign', 'Dramaturg', 'Regi og musikkutvelgelse']
    for oppgave in oppgaver:
        insert('Oppgave', ['oppgavetittel'], [oppgave])

def insert_medvirkende_person():
    medvirkende_personer_størst_av_alt_er_kjærligheten = [
         ('corell@teater.no', 'Jonas Corell Petersen', 'Regi'),
         ('gehrt@teater.no', 'David Gehrt', 'Scenografi og kostymer'),
         ('tønder@teater.no', 'Gaute Tønder', 'Musikalsk ansvarlig'),
         ('mikaelsen@teater.no', 'Magnus Mikaelsen', 'Lysdesign'),
         ('spender@teater.no', 'Kristoffer Spender', 'Dramaturg')
    ]
    medvirkende_personer_kongsemnene = [
         ('butusov@teater.no', 'Yury Butusov', 'Regi og musikkutvelgelse'),
         ('kokusai@teater.no', 'Aleksandr Shishkin-Hokusai', 'Scenografi og kostymer'),
         ('myten@teater.no', 'Eivind Myren', 'lysdesign'),
         ('stokke@teater.no', 'Mina Rype Stokke', 'Dramaturg')
    ]
    for epost, navn, ansattStatus in medvirkende_personer_størst_av_alt_er_kjærligheten:
        insert('MedvirkendePerson', ('epostadresse', 'navn', 'ansattStatus'), (epost, navn, ansattStatus))
    for epost, navn, ansattStatus in medvirkende_personer_kongsemnene:
        insert('MedvirkendePerson', ('epostadresse', 'navn', 'ansattStatus'), (epost, navn, ansattStatus))

insert_stoler_Hovedscenen()
insert_stoler_Parkett('Gamle scene', 10)
insert_stoler_Balkong('Gamle scene', 4)
insert_stoler_Galleri('Gamle scene', 3)
insert_teaterstykker()
insert_roller()
insert_område()
insert_skuespiller()
insert_saler()
insert_forestillinger()
insert_akter()
insert_oppgaver()
insert_medvirkende_person()
