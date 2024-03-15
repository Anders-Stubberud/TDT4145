-- Følgende restriksjoner må håndteres i applikasjonsprogrammet
-- Forestillingene til de ulike stykkene skal gå på bestemte datoer og klokkeslett
-- Det skal kun være mulig å sette opp stykkene «Kongsemnene» og «Størst av alt er kjærligheten.»
-- Prisen til billettene skal avgjøres basert på kundens gruppe. 
-- Billettene tilhørende et billettkjøp hører til samme forestilling.
-- Barn skal ikke kunne kjøpe billetter til  «Kongsemnene».
-- Hvorvidt tittelen til en ansatt er gyldig.

CREATE TABLE IF NOT EXISTS Teatersal (
    salnavn TEXT NOT NULL,
    PRIMARY KEY (salnavn)
);

CREATE TABLE IF NOT EXISTS Teaterstykke (
    navnPaStykke TEXT NOT NULL,
    salnavn TEXT NOT NULL,
		klokkeslett TIME NOT NULL,
    PRIMARY KEY (navnPaStykke),
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
    rolleID INTEGER AUTO_INCREMENT NOT NULL,
    navn TEXT NOT NULL,
    navnPaStykke TEXT NOT NULL,
    PRIMARY KEY (rolleID),
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
    skuespillerID INTEGER AUTO_INCREMENT NOT NULL,
    fornavn TEXT NOT NULL,
    etternavn TEXT NOT NULL,
    PRIMARY KEY (skuespillerID)
);

CREATE TABLE IF NOT EXISTS spillerRolle (
    rolleID INTEGER AUTO_INCREMENT NOT NULL,
    skuespillerID INTEGER NOT NULL,
    PRIMARY KEY (rolleID, skuespillerID),
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
    omraadeID INTEGER AUTO_INCREMENT NOT NULL,
    omraadenavn TEXT NOT NULL,
    PRIMARY KEY (omraadeID)
);

CREATE TABLE IF NOT EXISTS Stol (
    stolID INTEGER AUTO_INCREMENT NOT NULL,
    stolnummer INTEGER NOT NULL,
    radnummer INTEGER NOT NULL,
    salnavn TEXT NOT NULL,
    omraadeID INTEGER NOT NULL,
    PRIMARY KEY (stolID),
    FOREIGN KEY (salnavn)
        REFERENCES Teatersal (salnavn)
            ON UPDATE CASCADE,
    FOREIGN KEY (omraadeID)
        REFERENCES Omraade (omraadeID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Forestilling (
    forestillingID INTEGER AUTO_INCREMENT NOT NULL,
    dato DATE NOT NULL,
    navnPaStykke TEXT NOT NULL,
    PRIMARY KEY (forestillingID),
    FOREIGN KEY (navnPaStykke)
        REFERENCES Teaterstykke (navnPaStykke)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Kundegruppe (
    gruppenavn TEXT NOT NULL,
    PRIMARY KEY (gruppenavn)
);

CREATE TABLE IF NOT EXISTS Kundeprofil (
    mobilnummer INTEGER NOT NULL,
    navn TEXT NOT NULL,
    adresse TEXT NOT NULL,
    gruppenavn TEXT NOT NULL,
    PRIMARY KEY (mobilnummer),
    FOREIGN KEY (gruppenavn)
        REFERENCES Kundegruppe (gruppenavn)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Pris (
    prisID INTEGER AUTO_INCREMENT NOT NULL,
    pris FLOAT NOT NULL,
    PRIMARY KEY (prisID)
);

CREATE TABLE IF NOT EXISTS KostnadForGruppe (
    gruppenavn TEXT NOT NULL,
    prisID INTEGER NOT NULL,
    PRIMARY KEY (gruppenavn, prisID),
    FOREIGN KEY (gruppenavn)
        REFERENCES Kundegruppe (gruppenavn)
            ON UPDATE CASCADE,
    FOREIGN KEY (prisID)
        REFERENCES Pris (prisID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS KostnadForForestilling (
    navnPaStykke TEXT NOT NULL,
    prisID INTEGER NOT NULL,
    PRIMARY KEY (navnPaStykke, prisID),
    FOREIGN KEY (navnPaStykke)
        REFERENCES Teaterstykke (navnPaStykke)
            ON UPDATE CASCADE,
    FOREIGN KEY (prisID)
        REFERENCES Pris (prisID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS BillettKjøp (
    kjøpsID INTEGER AUTO_INCREMENT NOT NULL,
    dato DATE NOT NULL,
    tid TIME NOT NULL,
    mobilnummer INTEGER NOT NULL,
    PRIMARY KEY (kjøpsID),
    FOREIGN KEY (mobilnummer)
        REFERENCES Kundeprofil (mobilnummer)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Billett (
    billettID INTEGER AUTO_INCREMENT NOT NULL,
    stolID INTEGER NOT NULL,
    forestillingID INTEGER NOT NULL,
    kjøpsID INTEGER NOT NULL,
    PRIMARY KEY (billettID),
    FOREIGN KEY (forestillingID)
        REFERENCES Forestilling (forestillingID)
            ON UPDATE CASCADE,
    FOREIGN KEY (kjøpsID)
        REFERENCES BillettKjøp (kjøpsID)
            ON UPDATE CASCADE,
    FOREIGN KEY (stolID)
        REFERENCES Stol (stolID)
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Oppgave (
    oppgavetittel TEXT NOT NULL,
    PRIMARY KEY (oppgavetittel)
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
    personIdentifikator INTEGER NOT NULL,
    epostadresse TEXT UNIQUE,
    navn TEXT NOT NULL,
    ansattstatus TEXT,
    PRIMARY KEY (personIdentifikator)
);

CREATE TABLE IF NOT EXISTS utførerOppgave (
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