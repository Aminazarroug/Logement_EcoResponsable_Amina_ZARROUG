-- Fichier Logement.sql
-- Première étape : Suppression des tables éventuelles pour éviter toutes erreurs.

-- Tables que nous avons : Logement, pièce, facture, device, type_de_capteur, mesure

DROP TABLE IF EXISTS Mesure;
DROP TABLE IF EXISTS Device_TYPE;
DROP TABLE IF EXISTS Device;
DROP TABLE IF EXISTS Pièce;
DROP TABLE IF EXISTS Logement;
DROP TABLE IF EXISTS Facture; 

-- Création des Tables : 

-- Table 1 : Logement 

-- Nous ajoutons un ID unique qui s'autoincémente, ça sera la clé primaire de la table
-- Nous avons 4 attributs : Adresse qu'on met en VARCHAR avec 255 caractères. 
-- Téléphone, nous savons qu'il ne dépassera pas les 15 valeurs
-- Adresse IP ne dépasse pas les 50 caractères. Pour la date d'insertion nous utilisons l'instruction du TP 

CREATE TABLE Logement(
    ID_Logement INTEGER PRIMARY KEY AUTOINCREMENT,
    Adresse VARCHAR(255),
    Téléphone VARCHAR(15),     -- Etant donné que le numéro est purement numérique et ne sera pas utilisé pour des calculs mathématiques nous utilisons VARCHAR
    Adresse_IP VARCHAR(50),
    Date_Insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 2 : Pièce 

-- Nous ajoutons un ID unique qui s'autoincémente, ça sera la clé primaire de la table
-- En plus, nous avons 5 attributs : Nom qu'on met en VARCHAR et qui ne dépassera pas les 50 caracètres. 
-- Localisation_X représente la coordonnées X du système cartésien de localisation en float
-- Localisation_Y représente la coordonnées Y de localisation en float
-- Localisation_Z représente la coordonnées Z de localisation en float
-- Nous ajoutons une clé étrangère : l'ID du logement de la table précédente pour savoir à quel logement appartient la pièce 

CREATE TABLE Pièce(
    ID_Pièce INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom VARCHAR(50),     -- Nous supposons que le nom de la pièce n'excédera pas 50 caractères  
    Localisation_X FLOAT,
    Localisation_Y FLOAT, 
    Localisation_Z FLOAT,
    ID_Logement INTEGER,
    FOREIGN KEY (ID_Logement) REFERENCES Logement(ID_Logement)
);

-- Table 3 : Facture

-- Nous ajoutons un ID unique qui s'autoincémente, ça sera la clé primaire de la table
-- En plus, nous avons 5 attributs : Type de facture qu'on met en VARCHAR et qui ne dépassera pas les 50 caracètres. 
-- La date de facture qui sera une variable 'date'
-- Le montant de la facture en float
-- La valeur consommée en float
-- Nous ajoutons une clé étrangère : l'ID du logement de la table précédente pour savoir à quel logement appartient la facture


CREATE TABLE Facture(
    ID_Facture INTEGER PRIMARY KEY AUTOINCREMENT,
    Type_facture VARCHAR(50), 
    Date_facture DATE ,
    Montant FLOAT, 
    Valeur_consommée FLOAT, 
    ID_Logement INTEGER,
    FOREIGN KEY (ID_Logement) REFERENCES Logement(ID_Logement)  
);

-- Table 4 : Type Device

-- Nous ajoutons un ID unique qui s'autoincémente, ça sera la clé primaire de la table
-- En plus nous avons 3 attributs : Type du device (Capteur/actionneur) qu'on met en VARCHAR et qui ne dépassera pas les 50 caracètres. 
-- Unité de mesure 
-- Plage de précision qu'on met en VARCHAR car elle est numérique et ne sera pas utilisée pour des opérations mathématiques

CREATE TABLE Device_TYPE (
    ID_Type INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom_Type VARCHAR(50),
    Unité_Mesure VARCHAR(20),
    Plage_Précision VARCHAR(50)
);

-- Table 5 : Device

-- Nous ajoutons un ID unique qui s'autoincémente, ça sera la clé primaire de la table
-- Nous avons, en plus, 6 attributs : Référence commerciale qu'on met en VARCHAR et qui ne dépassera pas les 100 caracètres. 
-- Référence de la pièce en 50 caractères VARCHAR
-- Date d'insertion et port du communication
-- Nous ajoutons 2 clés étrangères : l'ID du de device et du type pour savoir à quel pièce appartient le device et quel est son type


CREATE TABLE Device(
    ID_Device INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Pièce INTEGER,
    ID_Type INTEGER,
    Référence_commerciale VARCHAR(100),
    Port_communication VARCHAR(50),
    Date_insert TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Pièce) REFERENCES Pièce(ID_Pièce),
    FOREIGN KEY (ID_Type) REFERENCES Device_TYPE(ID_Type)
);

-- Table 6 : Mesure

-- Nous ajoutons un ID unique qui s'autoincémente, ça sera la clé primaire de la table
-- Nous avons, en plus 3 attributs : Valeur en float
-- Date d'insertion 
-- Nous ajoutons une clé étrangère : l'ID du de device pour savoir à quelle device appartient la mesure



CREATE TABLE Mesure (
    ID_Mesure INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Device INTEGER,
    Valeur FLOAT,
    Date_Insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Device) REFERENCES Device(ID_Device)
);


-- Ajout d'un logement avec 4 pièces

-- Insertion du logement
INSERT INTO Logement (Adresse, Téléphone, Adresse_IP)
VALUES 
    ('8, rue Jean Dolent, 75014 Paris', '0636021242', '192.168.0.1'), -- Logement urbain
    ('22, avenue Victor Hugo, 75016 Paris', '0654321987', '192.168.1.1'), -- Logement urbain
    ('10, rue des Lilas, 59800 Lille', '0765432109', '192.168.2.1'), -- Logement régional
    ('14, chemin du Bocage, 44000 Nantes', '0712345678', '192.168.3.1'); -- Logement suburbain

--on peut suivre les IDs avec AUTOINCREMENT

-- Insertion des pièces associées
-- Remarque : Ces pièces sont rattachées au logement avec l'ID = 1 (le premier logement inséré).
INSERT INTO Pièce (Nom, Localisation_X, Localisation_Y, Localisation_Z, ID_Logement)
VALUES
    ('Salon', 3.0, 3.0, 0, 1),
    ('Cuisine', 1.0, 1.0, 0, 1),
    ('Chambre', 4.5, 5.0, 0, 1),
    ('Salle de bains', 6.0, 2.0, 0, 1),
    ('Bureau', 2.0, 4.5, 0, 2),
    ('Salon', 4.0, 4.0, 0, 2),
    ('Cuisine', 2.0, 1.0, 0, 3),
    ('Balcon', 3.5, 2.5, 0, 3);

INSERT INTO Device_TYPE (Nom_Type, Unité_Mesure, Plage_Précision)
VALUES 
    ('Température', '°C', '±0.5°C'),
    ('Humidité', '%', '±1%'),
    ('Électricité', 'kWh', '±0.1 kWh'),
    ('Présence', 'Binaire', 'NA'),
    ('Gaz', 'ppm', '±1000 ppm'),
    ('Lumière', 'Lux', '±10 Lux'), -- Capteur de lumière
    ('CO2', 'ppm', '±500 ppm'), -- Détecteur de CO2
    ('Volet', 'Binaire', 'NA'); -- Actionneur pour contrôler les volets

INSERT INTO Device (ID_Pièce, ID_Type, Référence_commerciale, Port_communication)
VALUES
    (1, 3, 'ELEC_3302', 'COM4'), -- Capteur électrique dans le salon
    (2, 1, 'TEMP_2023', 'COM5'), -- Capteur de température dans la cuisine
    (3, 5, 'GAZ_2028', 'COM7'), -- Capteur de gaz dans la chambre
    (4, 4, 'PRES_0376', 'COM9'), -- Détecteur de présence dans la salle de bains
    (1, 6, 'LUM_4810', 'COM6'), -- Capteur de lumière dans le salon
    (2, 7, 'CO2_5900', 'COM8'), -- Détecteur de CO2 dans la cuisine
    (3, 8, 'VOLET_1000', 'COM10'); -- Actionneur volet dans la chambre


INSERT INTO Mesure (ID_Device, Valeur)
VALUES
    (1, 120.5), -- Électricité en kWh
    (2, 22.3), -- Température en °C
    (3, 350.0), -- Gaz en ppm
    (4, 1), -- Présence détectée
    (5, 300.0), -- Lumière en Lux
    (6, 450.0), -- CO2 en ppm
    (7, 0); -- Volet fermé

-- Insertion des factures
INSERT INTO Facture (ID_Logement, Type_facture, Date_facture, Montant, Valeur_consommée)
VALUES
    (1, 'Électricité', '2024-01-15', 90.50, 250.0),
    (1, 'Eau', '2024-02-01', 45.00, 15.0),
    (1, 'Internet', '2024-03-01', 30.00, 0.0),
    (2, 'Gaz', '2024-02-15', 65.00, 50.0),
    (2, 'Électricité', '2024-01-10', 110.00, 300.0),
    (3, 'Électricité', '2024-01-20', 95.00, 280.0),
    (3, 'Déchets', '2024-02-10', 20.00, 0.0);

