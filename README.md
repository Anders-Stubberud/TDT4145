# TDT4145 Prosjekt Innlevering 2 Gruppe 21

## Initialisere databasen

For å initialisere databasen, åpner du en terminal og navigerer til rotmappen av prosjektet. Deretter bruker du kommandoen `python main.py`. Da får du følgende spørsmål:

Hvilken oppgave ønsker du å utføre? Skriv:
- `0` for å opprette databasen med startdata'en,
- `[1, 2, 3, 4, 5, 6, 7]` for individuelle oppgaver,
- `8` for å kjøre alle oppgavene,
- `9` for å slette databasen,
- eller `10` for å avslutte.

Her velger du `0`. Dette fører til at Python setter inn tabellene fra `schema.sql`, og fyller inn dataen fra `insert-db.sql`. Dette vil si at teatersaler, teaterstykker, forestillinger, akter, roller, skuespillere, andre medvirkende, og annen data blir registrert i databasen. Stolene blir imidlertid ikke ført inn i dette steget, det tar Python seg av i brukstilfelle 1.

## Utføring av brukstilfellene

På samme måte som ved initialiseringen av databasen, så bruker du kommandoen `python main.py` for å få mulighet til å utføre brukstilfellene. Dersom du ønsker å fullføre brukstilfelle 1 ved å sette inn stolene, så trykker du `1`. Dersom du ønsker å utføre brukstilfelle 2, så trykker du `2`, osv. Dersom du ønsker å fortløpende utføre samtlige brukstilfeller uten å separat trykke på alle tallene, så velger du `8`.

## Tømme databasen

Dersom du ønsker å tømme databasen, så bruker du først kommandoen `python main.py`. Deretter trykker du `9`.

## Komme seg ut av sesjonen

Dersom du ønsker å avslutte sesjonen, så velger du `10`.
