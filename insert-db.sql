INSERT INTO Teatersal(salnavn) VALUES
('Hovedscenen'),
('Gamle scene');

INSERT INTO Teaterstykke(navnPaStykke, salnavn, klokkeslett)
VALUES 
('Kongsemnene', 'Hovedscenen', '19:00'),
('Størst av alt er kjærligheten', 'Gamle scene', '18:30');

INSERT INTO Skuespiller(fornavn, etternavn)
VALUES 
--størst av alt er kjærligheten
('Sunniva Du Mond', 'Nordal'),
('Jo', 'Saberniak'),
('Marte M.', 'Steinholt'),
('Tor Ivar', 'Hagen'),
('Trond-Ove', 'Skrødal'),
('Natalie Grøndahl', 'Tangen'),
('Åsmund', 'Flaten'),
--Kongsemnene
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

INSERT INTO Omraade(omraadenavn) 
VALUES
('Parkett'),
('Balkong'),
('Galleri');

INSERT INTO Akt(navnPaStykke, nummer, aktNavn) 
VALUES
('Størst av alt er kjærligheten', 1, 'Akt 1'),
('Kongsemnene', 1, 'Akt 1'),
('Kongsemnene', 2, 'Akt 2'),
('Kongsemnene', 3, 'Akt 3'),
('Kongsemnene', 4, 'Akt 4'),
('Kongsemnene', 5, 'Akt 5');

INSERT INTO SpillerRolle(skuespillerID, rolleID) 
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8), -- Arturo Scotti as Haakon Haakonssønn
(9, 9), -- Ingunn Beate Strige Øyen as Inga fra Vartejg
(10, 10), -- Hans Petter Nilsen as Skule jarl
(11, 11), -- Madeleine Brandtzæg Nilsen as Fru Ragnhild
(12, 12), -- Synnøve Fossum Eriksen as Margrete
(13, 13), -- Emma Caroline Deichmann as Sigrid
(13, 14), -- Emma Caroline Deichmann as Sigrid
(14, 15),  -- thomas
(15, 16), -- per bogstad
(16, 17), -- isak holmen
(16, 18), -- isak holmen
(17, 18), -- fabian
(17, 19), -- fabian
(18, 20), -- emil
(18, 21), -- emil
(19, 22); -- snorre

INSERT INTO rolleIAkt(navnPaStykke, nummer, rolleID)
VALUES
--Størst av alt er kjærligheten
('Størst av alt er kjærligheten', 1, 1),
('Størst av alt er kjærligheten', 1, 2),
('Størst av alt er kjærligheten', 1, 3),
('Størst av alt er kjærligheten', 1, 4),
('Størst av alt er kjærligheten', 1, 5),
('Størst av alt er kjærligheten', 1, 6),
('Størst av alt er kjærligheten', 1, 7),
-- Kongsemnene
-- Håkon Håkonsson
('Kongsemnene', 1, 8),
('Kongsemnene', 2, 8),
('Kongsemnene', 3, 8),
('Kongsemnene', 4, 8),
('Kongsemnene', 5, 8),
-- Dagfinn Bonde
('Kongsemnene', 1, 21),
('Kongsemnene', 2, 21),
('Kongsemnene', 3, 21),
('Kongsemnene', 4, 21),
('Kongsemnene', 5, 21),
-- Jatgeir Skald
('Kongsemnene', 4, 20),
--Sigrid
('Kongsemnene', 1, 13),
('Kongsemnene', 2, 13),
('Kongsemnene', 5, 13),
--Ingeborg
('Kongsemnene', 4, 14),
-- Det ser ikke ut til at Guttorm Ingesson er med (på nettsiden til teateret)
--Skule Jarl
('Kongsemnene', 1, 10),
('Kongsemnene', 2, 10),
('Kongsemnene', 3, 10),
('Kongsemnene', 4, 10),
('Kongsemnene', 5, 10),
--Inga fra Vartejg
('Kongsemnene', 1, 9),
('Kongsemnene', 3, 9),
-- Paal Flida
('Kongsemnene', 1, 17),
('Kongsemnene', 2, 17),
('Kongsemnene', 3, 17),
('Kongsemnene', 4, 17),
('Kongsemnene', 5, 17),
-- Ragnhild
('Kongsemnene', 1, 11),
('Kongsemnene', 5, 11),
--Gregorius Jonsson
('Kongsemnene', 1, 16),
('Kongsemnene', 2, 16),
('Kongsemnene', 3, 16),
('Kongsemnene', 4, 16),
('Kongsemnene', 5, 16),
-- Margrete
('Kongsemnene', 1, 12),
('Kongsemnene', 2, 12),
('Kongsemnene', 3, 12),
('Kongsemnene', 4, 12),
('Kongsemnene', 5, 12),
--Biskop Nikolas
('Kongsemnene', 1, 15),
('Kongsemnene', 2, 15),
('Kongsemnene', 3, 15),
-- Peter
('Kongsemnene', 3, 22),
('Kongsemnene', 4, 22),
('Kongsemnene', 5, 22);

INSERT INTO SpillerIAkt(skuespillerID, navnPaStykke, nummer) 
VALUES
(8, 'Kongsemnene', 1), -- Arturo Scotti in Act 1 of Kongsemnene
(9, 'Kongsemnene', 1), -- Ingunn Beate Strige Øyen in Act 1 of Kongsemnene
(10, 'Kongsemnene', 1), -- Hans Petter Nilsen in Act 1 of Kongsemnene
(11, 'Kongsemnene', 1), -- Madeleine Brandtzæg Nilsen in Act 1 of Kongsemnene
(12, 'Kongsemnene', 1), -- Synnøve Fossum Eriksen in Act 1 of Kongsemnene
(13, 'Kongsemnene', 1), -- Emma Caroline Deichmann in Act 1 of Kongsemnene
(14, 'Kongsemnene', 1), -- Thomas Jensen Takyi in Act 1 of Kongsemnene
(15, 'Kongsemnene', 1), -- Per Bogstad Gulliksen in Act 1 of Kongsemnene
(16, 'Kongsemnene', 1), -- Isak Holmen Sørensen in Act 1 of Kongsemnene
(17, 'Kongsemnene', 1), -- Fabian Heidelberg Lunde in Act 1 of Kongsemnene
(18, 'Kongsemnene', 1), -- Emil Olafsson in Act 1 of Kongsemnene
(19, 'Kongsemnene', 1); -- Snorre Ryen Tøndel in Act 1 of Kongsemnene

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
('Inga fra Vartejg (Haakons mor)', 'Kongsemnene'),
('Skule jarl', 'Kongsemnene'),
('Fru Ragnhild (Skules hustru)', 'Kongsemnene'),
('Margrete (Skules datter)', 'Kongsemnene'),
('Sigrid (Skules søster)', 'Kongsemnene'),
('Ingebjørg', 'Kongsemnene'),
('Biskop Nikolas', 'Kongsemnene'),
('Gregorius Jonssønn', 'Kongsemnene'),
('Paal Flida', 'Kongsemnene'),
('Trønder', 'Kongsemnene'),
('Baard Bratte', 'Kongsemnene'),
('Jatgeir Skald', 'Kongsemnene'),
('Dagfinn Bonde', 'Kongsemnene'),
('Peter (prest og Ingebjørgs sønn)', 'Kongsemnene');

INSERT INTO Forestilling(dato, tid, navnPaStykke) 
VALUES 
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

INSERT INTO Kundegruppe(gruppenavn) 
VALUES
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


