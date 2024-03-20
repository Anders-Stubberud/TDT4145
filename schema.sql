-- Følgende restriksjoner må håndteres i applikasjonsprogrammet
-- Forestillingene til de ulike stykkene skal gå på bestemte datoer og klokkeslett
-- Det skal kun være mulig å sette opp stykkene «Kongsemnene» og «Størst av alt er kjærligheten.»
-- Prisen til billettene skal avgjøres basert på kundens gruppe. 
-- Billettene tilhørende et billettkjøp hører til samme forestilling.
-- Barn skal ikke kunne kjøpe billetter til  «Kongsemnene».
-- Hvorvidt tittelen til en ansatt er gyldig.

CREATE TABLE IF NOT EXISTS Teatersal (
    salnavn TEXT NOT NULL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Teaterstykke (
    navnPaStykke TEXT PRIMARY KEY,
    salnavn TEXT NOT NULL,
    klokkeslett TIME NOT NULL,
    FOREIGN KEY (salnavn)
        REFERENCES Teatersal (salnavn)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Akt (
    navnPaStykke TEXT NOT NULL,
    nummer INTEGER NOT NULL,
    navn TEXT,
    PRIMARY KEY (navnPaStykke, nummer),
    FOREIGN KEY (navnPaStykke)
        REFERENCES Teaterstykke (navnPaStykke)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Rolle (
    rolleID INTEGER PRIMARY KEY,
    navn TEXT NOT NULL,
    navnPaStykke TEXT NOT NULL,
    FOREIGN KEY (navnPaStykke)
        REFERENCES Teaterstykke (navnPaStykke)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS rolleIAkt (
    navnPaStykke TEXT NOT NULL,
    nummer INTEGER NOT NULL,
    rolleID INTEGER NOT NULL,
    PRIMARY KEY (navnPaStykke, nummer, rolleID),
    FOREIGN KEY (navnPaStykke, nummer)
        REFERENCES Akt (navnPaStykke, nummer)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (rolleID)
        REFERENCES Rolle (rolleID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Skuespiller (
    skuespillerID INTEGER PRIMARY KEY,
    fornavn TEXT NOT NULL,
    etternavn TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS spillerRolle (
    rolleID INTEGER PRIMARY KEY,
    skuespillerID INTEGER NOT NULL,
    FOREIGN KEY (rolleID)
        REFERENCES Rolle (rolleID)
            ON UPDATE CASCADE,
    FOREIGN KEY (skuespillerID)
        REFERENCES Skuespiller (skuespillerID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS spillerIAkt (
    navnPaStykke TEXT NOT NULL,
    nummer INTEGER NOT NULL,
    skuespillerID INTEGER NOT NULL,
    PRIMARY KEY (navnPaStykke, nummer, skuespillerID),
    FOREIGN KEY (navnPaStykke, nummer)
        REFERENCES Akt (navnPaStykke, nummer)
            ON UPDATE CASCADE,
    FOREIGN KEY (skuespillerID)
        REFERENCES Skuespiller (skuespillerID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Omraade (
    omraadeID INTEGER PRIMARY KEY,
    omraadenavn TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Stol (
    stolID INTEGER PRIMARY KEY,
    stolnummer INTEGER NOT NULL,
    radnummer INTEGER NOT NULL,
    salnavn TEXT NOT NULL,
    omraadeID INTEGER NOT NULL,
    FOREIGN KEY (salnavn)
        REFERENCES Teatersal (salnavn)
            ON UPDATE CASCADE,
    FOREIGN KEY (omraadeID)
        REFERENCES Omraade (omraadeID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Forestilling (
    forestillingID INTEGER PRIMARY KEY,
    dato DATE NOT NULL,
    tid TIME NOT NULL,
    navnPaStykke TEXT NOT NULL,
    FOREIGN KEY (navnPaStykke)
        REFERENCES Teaterstykke (navnPaStykke)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Kundegruppe (
    gruppenavn TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Kundeprofil (
    mobilnummer INTEGER PRIMARY KEY,
    fornavn TEXT NOT NULL,
    etternavn TEXT NOT NULL,
    postnummer TEXT NOT NULL,
    gatenavn TEXT NOT NULL,
    gatenummer INTEGER NOT NULL,
    gruppenavn TEXT NOT NULL,
    FOREIGN KEY (gruppenavn)
        REFERENCES Kundegruppe (gruppenavn)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Pris (
    prisID INTEGER PRIMARY KEY,
    pris FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS KostnadForGruppe (
    gruppenavn TEXT PRIMARY KEY,
    prisID INTEGER NOT NULL,
    FOREIGN KEY (gruppenavn)
        REFERENCES Kundegruppe (gruppenavn)
            ON UPDATE CASCADE,
    FOREIGN KEY (prisID)
        REFERENCES Pris (prisID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS KostnadForForestilling (
    navnPaStykke TEXT PRIMARY KEY,
    prisID INTEGER NOT NULL,
    FOREIGN KEY (navnPaStykke)
        REFERENCES Teaterstykke (navnPaStykke)
            ON UPDATE CASCADE,
    FOREIGN KEY (prisID)
        REFERENCES Pris (prisID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS BillettKjop (
    kjopsID INTEGER PRIMARY KEY,
    dato DATE NOT NULL,
    tid TIME NOT NULL,
    mobilnummer INTEGER NOT NULL,
    FOREIGN KEY (mobilnummer)
        REFERENCES Kundeprofil (mobilnummer)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Billett (
    billettID INTEGER PRIMARY KEY,
    stolID INTEGER NOT NULL,
    forestillingID INTEGER NOT NULL,
    kjopsID INTEGER NOT NULL,
    FOREIGN KEY (forestillingID)
        REFERENCES Forestilling (forestillingID)
            ON UPDATE CASCADE,
    FOREIGN KEY (kjopsID)
        REFERENCES BillettKjop (kjopsID)
            ON UPDATE CASCADE,
    FOREIGN KEY (stolID)
        REFERENCES Stol (stolID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Oppgave (
    oppgavetittel TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS oppgaveIStykke (
    oppgavetittel TEXT NOT NULL,
    navnPaStykke TEXT NOT NULL,
    PRIMARY KEY (oppgavetittel, navnPaStykke),
    FOREIGN KEY (oppgavetittel)
        REFERENCES Oppgave (oppgavetittel)
            ON UPDATE CASCADE,
    FOREIGN KEY (navnPaStykke)
        REFERENCES Teaterstykke (navnPaStykke)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS MedvirkendePerson (
    personID INTEGER PRIMARY KEY,
    epostadresse TEXT UNIQUE,
    navn TEXT NOT NULL,
    ansattstatus TEXT
);

CREATE TABLE IF NOT EXISTS bestiltStol (
    billettID INTEGER PRIMARY KEY,
    stolID INTEGER NOT NULL,
    FOREIGN KEY (stolID)
        REFERENCES Stol (stolID)
            ON UPDATE CASCADE,
    FOREIGN KEY (billettID)
        REFERENCES Billett (billettID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS utforerOppgave (
    oppgavetittel TEXT NOT NULL,
    personIdentifikator INTEGER NOT NULL,
    PRIMARY KEY (oppgavetittel, personIdentifikator),
    FOREIGN KEY (oppgavetittel)
        REFERENCES Oppgave (oppgavetittel)
            ON UPDATE CASCADE,
    FOREIGN KEY (personIdentifikator)
        REFERENCES MedvirkendePerson (personIdentifikator)
            ON UPDATE CASCADE
);
