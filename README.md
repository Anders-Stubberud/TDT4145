# TDT4145 Prosjekt innlevering 2 gruppe 21

## Initialisere databasen
Åpne en terminal, og naviger til rotmappen av prosjektet. Deretter benytter du kommandoen «python main.py». Da får du opp dette:

Hvilke(n) oppgave ønsker du å utføre?
Skriv:
0 for å opprette databasen med startdata'en,
[1, 2, 3, 4, 5, 6, 7] for individuelle oppgaver,
8 for å kjøre alle oppgavene,
9 for å slette databasen,
eller 10 for å avslutte. 

Her velger du 0. Dette fører til at python setter inn tabellene fra schema.sql, og fyller inn dataen fra insert-db.sql.
Dette vil si at teatersaler, teaterstykker, forestillinger, akter, roller, skuespillere, andre medvirkende, og øvrig data blir registrert i databasen. Stolene blir imidlertid ikke ført inn i dette steget, det tar av python i brukstilfelle 1.

Utføring av brukstilfellene
På samme måte som ved initialiseringen av databasen, så benytter du kommandoen «python main.py» for å få mulighet til å utføre brukstilfellene. 
Dersom du ønsker ønsker å fullføre brukstilfelle 1 ved å sette inn stolene, så trykker du 1. Dersom du ønsker å utføre brukstilfelle 2, så trykker du 2, osv.
Dersom du ønkser å fortløpende utføre samtlige brukstilfeller uten å separat trykke på alle tallene, så velger du 8.

Tømme databasen
Dersom du ønsker å tømme databasen, så bruker du først kommandoen «python main.py» Deretter trykker du 9.

Komme seg ut av sesjonen
Dersom du ønsker å avslutte sesjonen, så velger du 10.