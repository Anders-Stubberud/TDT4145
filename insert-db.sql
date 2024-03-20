INSERT INTO Teatersal(salnavn) VALUES
('Hovedscenen'),
('Gamle scene');

INSERT INTO Teaterstykke(navnPaStykke, salnavn, klokkeslett)
VALUES 
('Kongsemnene', 'Hovedscenen', '19:00'),
('Størst av alt er kjærligheten', 'Gamle scene', '18:30');

INSERT INTO Skuespiller(fornavn, etternavn)
VALUES 
('Arturo', 'Scotti'), -- Haakon Haakonssønn
('Ingunn Beate', 'Strige Øyen'), -- Inga fra Vartejg
('Hans Petter', 'Nilsen'), -- Skule jarl
('Madeleine Brandtzæg', 'Nilsen'), -- Fru Ragnhild
('Synnøve Fossum', 'Eriksen'), -- Margrete
('Emma Caroline', 'Deichmann'), -- Sigrid
('Thomas Jensen', 'Takyi'), -- Biskop Nikolas
('Per Bogstad', 'Gulliksen'), -- Gregorius Jonssønn
('Isak Holmen', 'Sørensen'), -- Paal Flida / Trønder
('Fabian Heidelberg', 'Lunde'), -- Baard Bratte / Trønder
('Emil', 'Olafsson'), -- Jatgeir Skald / Dagfinn Bonde
('Snorre Ryen', 'Tøndel'); -- Peter

INSERT INTO Omraade(omraadenavn) VALUES
('Parkett'),
('Balkong'),
('Galleri');

INSERT INTO Akt(navnPaStykke, nummer, navn) VALUES
('Kongsemnene', 1, 'Akt 1'),
('Kongsemnene', 2, 'Akt 2'),
('Kongsemnene', 3, 'Akt 3'),
('Kongsemnene', 4, 'Akt 4'),
('Kongsemnene', 5, 'Akt 5');

INSERT INTO SpillerRolle(skuespillerID, rolleID) VALUES
(1, 8), -- Arturo Scotti as Haakon Haakonssønn
(2, 9), -- Ingunn Beate Strige Øyen as Inga fra Vartejg
(3, 10), -- Hans Petter Nilsen as Skule jarl
(4, 11), -- Madeleine Brandtzæg Nilsen as Fru Ragnhild
(5, 12), -- Synnøve Fossum Eriksen as Margrete
(6, 13), -- Emma Caroline Deichmann as Sigrid
(7, 14), -- Thomas Jensen Takyi as Biskop Nikolas
(8, 15), -- Per Bogstad Gulliksen as Gregorius Jonssønn
(9, 16), -- Isak Holmen Sørensen as Paal Flida
(10, 17), -- Fabian Heidelberg Lunde as Trønder
(11, 18), -- Emil Olafsson as Baard Bratte
(12, 19), -- Snorre Ryen Tøndel as Jatgeir Skald / Dagfinn Bonde
(13, 20); -- Peter

INSERT INTO SpillerIAkt(skuespillerID, navnPaStykke, nummer) VALUES
(1, 'Kongsemnene', 1), -- Arturo Scotti in Act 1 of Kongsemnene
(2, 'Kongsemnene', 1), -- Ingunn Beate Strige Øyen in Act 1 of Kongsemnene
(3, 'Kongsemnene', 1), -- Hans Petter Nilsen in Act 1 of Kongsemnene
(4, 'Kongsemnene', 1), -- Madeleine Brandtzæg Nilsen in Act 1 of Kongsemnene
(5, 'Kongsemnene', 1), -- Synnøve Fossum Eriksen in Act 1 of Kongsemnene
(6, 'Kongsemnene', 1), -- Emma Caroline Deichmann in Act 1 of Kongsemnene
(7, 'Kongsemnene', 1), -- Thomas Jensen Takyi in Act 1 of Kongsemnene
(8, 'Kongsemnene', 1), -- Per Bogstad Gulliksen in Act 1 of Kongsemnene
(9, 'Kongsemnene', 1), -- Isak Holmen Sørensen in Act 1 of Kongsemnene
(10, 'Kongsemnene', 1), -- Fabian Heidelberg Lunde in Act 1 of Kongsemnene
(11, 'Kongsemnene', 1), -- Emil Olafsson in Act 1 of Kongsemnene
(12, 'Kongsemnene', 1), -- Snorre Ryen Tøndel in Act 1 of Kongsemnene
(13, 'Kongsemnene', 1); -- Peter in Act 1 of Kongsemnene

INSERT INTO Rolle(navn, navnPaStykke)
VALUES 
('Sunniva Du Mond Nordal', 'Størst av alt er kjærligheten'),
('Jo Saberniak', 'Størst av alt er kjærligheten'),
('Marte M. Steinholt', 'Størst av alt er kjærligheten'),
('Tor Ivar Hagen', 'Størst av alt er kjærligheten'),
('Trond-Ove Skrødal', 'Størst av alt er kjærligheten'),
('Natalie Grøndahl Tangen', 'Størst av alt er kjærligheten'),
('Åsmund Flaten', 'Størst av alt er kjærligheten'),
('Haakon Haakonssønn', 'Kongsemnene'),
('Inga fra Vartejg', 'Kongsemnene'),
('Skule jarl', 'Kongsemnene'),
('Fru Ragnhild', 'Kongsemnene'),
('Margrete', 'Kongsemnene'),
('Sigrid', 'Kongsemnene'),
('Biskop Nikolas', 'Kongsemnene'),
('Gregorius Jonssønn', 'Kongsemnene'),
('Paal Flida', 'Kongsemnene'),
('Trønder', 'Kongsemnene'),
('Baard Bratte', 'Kongsemnene'),
('Jatgeir Skald', 'Kongsemnene'),
('Dagfinn Bonde', 'Kongsemnene'),
('Peter', 'Kongsemnene');

INSERT INTO Rolle(navn, navnPaStykke) VALUES 
('Sunniva Du Mond Nordal', 'Størst av alt er kjærligheten'),
('Jo Saberniak', 'Størst av alt er kjærligheten'),
('Marte M. Steinholt', 'Størst av alt er kjærligheten'),
('Tor Ivar Hagen', 'Størst av alt er kjærligheten'),
('Trond-Ove Skrødal', 'Størst av alt er kjærligheten'),
('Natalie Grøndahl Tangen', 'Størst av alt er kjærligheten'),
('Åsmund Flaten', 'Størst av alt er kjærligheten'),
('Haakon Haakonssønn', 'Kongsemnene'),
('Inga fra Vartejg', 'Kongsemnene'),
('Skule jarl', 'Kongsemnene'),
('Fru Ragnhild', 'Kongsemnene'),
('Margrete', 'Kongsemnene'),
('Sigrid', 'Kongsemnene'),
('Biskop Nikolas', 'Kongsemnene'),
('Gregorius Jonssønn', 'Kongsemnene'),
('Paal Flida', 'Kongsemnene'),
('Trønder', 'Kongsemnene'),
('Baard Bratte', 'Kongsemnene'),
('Jatgeir Skald', 'Kongsemnene'),
('Dagfinn Bonde', 'Kongsemnene'),
('Peter', 'Kongsemnene');

INSERT INTO Forestilling(dato, tid, navnPaStykke) VALUES 
('2024-02-01', '19:00', 'Kongsemnene'),
('2024-02-02', '19:00', 'Kongsemnene'),
('2024-02-03', '19:00', 'Kongsemnene'),
('2024-02-05', '19:00', 'Kongsemnene'),
('2024-02-06', '19:00', 'Kongsemnene'),
('2024-02-03', '18:30', 'Størst av alt er kjærligheten'),
('2024-02-06', '18:30', 'Størst av alt er kjærligheten'),
('2024-02-07', '18:30', 'Størst av alt er kjærligheten'),
('2024-02-12', '18:30', 'Størst av alt er kjærligheten'),
('2024-02-13', '18:30', 'Størst av alt er kjærligheten'),
('2024-02-14', '18:30', 'Størst av alt er kjærligheten');

INSERT INTO Kundegruppe(gruppenavn) VALUES
('Ordinær'),
('Honnør'),
('Student'),
('Gruppe 10'),
('Gruppe honnør 10');

INSERT INTO KostnadForStykke(navnPaStykke, gruppenavn, pris)
VALUES
('Kongsemnene', 'Ordinær', 450),
('Kongsemnene', 'Honnør', 380),
('Kongsemnene', 'Student', 280),
-- med restriksjoner
('Kongsemnene', 'Gruppe 10', 420), 
('Kongsemnene', 'Gruppe honnør 10', 360),
('Størst av alt er kjærligheten', 'Ordinær', 350),
('Størst av alt er kjærligheten', 'Honnør', 300),
('Størst av alt er kjærligheten', 'Student', 220),
('Størst av alt er kjærligheten', 'Barn', 220),
('Størst av alt er kjærligheten', 'Gruppe 10', 320), 
('Størst av alt er kjærligheten', 'Gruppe honnør 10', 270);

-- INSERT INTO Pris(pris) VALUES
-- (450.0), -- Ordinær for Kongsemnene
-- (380.0), -- Honnør for Kongsemnene
-- (280.0), -- Student for Kongsemnene
-- (420.0), -- Gruppe 10 for Kongsemnene
-- (360.0), -- Gruppe honnør 10 for Kongsemnene
-- (350.0), -- Ordinær for Størst av alt er kjærligheten
-- (300.0), -- Honnør for Størst av alt er kjærligheten
-- (220.0), -- Student for Størst av alt er kjærligheten
-- (220.0), -- Barn for Størst av alt er kjærligheten
-- (320.0), -- Gruppe 10 for Størst av alt er kjærligheten
-- (270.0); -- Gruppe honnør 10 for Størst av alt er kjærligheten

-- INSERT INTO KostnadForForestilling(navnPaStykke, prisID) VALUES
-- ('Kongsemnene', 1), -- Ordinær for Kongsemnene
-- ('Kongsemnene', 2), -- Honnør for Kongsemnene
-- ('Kongsemnene', 3), -- Student for Kongsemnene
-- ('Kongsemnene', 4), -- Gruppe 10 for Kongsemnene
-- ('Kongsemnene', 5), -- Gruppe honnør 10 for Kongsemnene
-- ('Størst av alt er kjærligheten', 6), -- Ordinær for Størst av alt er kjærligheten
-- ('Størst av alt er kjærligheten', 7), -- Honnør for Størst av alt er kjærligheten
-- ('Størst av alt er kjærligheten', 8), -- Student for Størst av alt er kjærligheten
-- ('Størst av alt er kjærligheten', 9), -- Barn for Størst av alt er kjærligheten
-- ('Størst av alt er kjærligheten', 10); -- Gruppe 10 for Størst av alt er kjærligheten
