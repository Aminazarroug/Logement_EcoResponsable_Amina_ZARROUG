-- Suppression des tables pour éviter toute erreur
DROP TABLE IF EXISTS Mesure;
DROP TABLE IF EXISTS Device_TYPE;
DROP TABLE IF EXISTS Device;
DROP TABLE IF EXISTS Pièce;
DROP TABLE IF EXISTS Logement;
DROP TABLE IF EXISTS Facture;

-- Création des Tables :

-- Table Logement : Inclut des identifiants uniques pour chaque utilisateur
CREATE TABLE Logement (
    ID_Logement INTEGER PRIMARY KEY AUTOINCREMENT,
    Adresse VARCHAR(255),
    Téléphone VARCHAR(15),      -- Le numéro est stocké comme VARCHAR car il n'est pas utilisé pour des calculs
    Adresse_IP VARCHAR(50),
    adresse_email VARCHAR(255) UNIQUE NOT NULL, -- Email unique pour chaque utilisateur
    mot_de_passe VARCHAR(255) NOT NULL,         -- Mot de passe pour le compte utilisateur
    Date_Insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table Pièce : Inclut la relation avec Logement
CREATE TABLE Pièce (
    ID_Pièce INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom VARCHAR(50),      -- Nom de la pièce
    Localisation_X FLOAT,
    Localisation_Y FLOAT,
    Localisation_Z FLOAT,
    ID_Logement INTEGER,
    FOREIGN KEY (ID_Logement) REFERENCES Logement(ID_Logement)
);

-- Table Facture : Ajoutée pour chaque logement, reliée via ID_Logement
CREATE TABLE Facture (
    ID_Facture INTEGER PRIMARY KEY AUTOINCREMENT,
    Type_facture VARCHAR(50), 
    Date_facture DATE,
    Montant FLOAT, 
    Valeur_consommée FLOAT, 
    ID_Logement INTEGER,
    FOREIGN KEY (ID_Logement) REFERENCES Logement(ID_Logement)
);

-- Table Device_TYPE : Définit les types de capteurs/actionneurs
CREATE TABLE Device_TYPE (
    ID_Type INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom_Type VARCHAR(50),
    Unité_Mesure VARCHAR(20),
    Plage_Précision VARCHAR(50)
);

-- Table Device : Chaque device est lié à une pièce et un logement
CREATE TABLE Device (
    ID_Device INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Pièce INTEGER,
    ID_Type INTEGER,
    Référence_commerciale VARCHAR(100),
    Port_communication VARCHAR(50),
    ID_Logement INTEGER,
    Date_insert TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Pièce) REFERENCES Pièce(ID_Pièce),
    FOREIGN KEY (ID_Type) REFERENCES Device_TYPE(ID_Type),
    FOREIGN KEY (ID_Logement) REFERENCES Logement(ID_Logement)
);

-- Table Mesure : Ajout des mesures associées aux devices
CREATE TABLE Mesure (
    ID_Mesure INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Device INTEGER,
    Valeur FLOAT,
    Date_Insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ID_Logement INTEGER,
    FOREIGN KEY (ID_Device) REFERENCES Device(ID_Device),
    FOREIGN KEY (ID_Logement) REFERENCES Logement(ID_Logement)
);

-- Insertion des données des logements
INSERT INTO Logement (Adresse, Téléphone, Adresse_IP, adresse_email, mot_de_passe)
VALUES 
    ('8, rue Jean Dolent, 75014 Paris', '0636021242', '192.168.0.1', 'aminazarroug@gmail.com', 'hello123'), 
    ('22, avenue Victor Hugo, 75016 Paris', '0654321987', '192.168.1.1', 'client1@gmail.com', 'bonjourvous');

-- Insertion des pièces
INSERT INTO Pièce (Nom, Localisation_X, Localisation_Y, Localisation_Z, ID_Logement)
VALUES
    ('Salon', 0.0, 0.0, 0, 1),
    ('Cuisine', 0.0, 10.0, 0, 1),
    ('Bureau', 0.0, 0.0, 0, 2),
    ('Salon', 0.0, 10.0, 0, 2),
    ('Bureau', 0.0, 0.0, 0, 1),
    ('Balcon', 0.0, 10.0, 0, 2);

-- Insertion des types de devices
INSERT INTO Device_TYPE (Nom_Type, Unité_Mesure, Plage_Précision)
VALUES 
    ('Température', '°C', '±0.5°C'),
    ('Électricité', 'kWh', '±0.1 kWh'),
    ('Présence', 'Binaire', 'NA'),
    ('Gaz', 'ppm', '±1000 ppm'),
    ('Lumière', 'Lux', '±10 Lux'),
    ('Volet', 'Binaire', 'NA'),
    ('Eau', 'L', '±0.5L');

-- Insertion des devices
INSERT INTO Device (ID_Pièce, ID_Type, Référence_commerciale, Port_communication, ID_Logement)
VALUES
    (1, 2, 'ELEC_3302', 'COM4', 1),  --Logement 1 pièce 1  
    (2, 1, 'TEMP_2023', 'COM5', 1),    --Logement 1 pièce 2 
    (5, 4, 'GAZ_2028', 'COM7', 1),   --Logement 1 pièce 5 
    (1, 3, 'PRES_0376', 'COM9', 1),     
    (2, 5, 'LUM_4810', 'COM2', 1),
    (5, 7, 'EAU_5634', 'COM10', 1),
    (3, 2, 'ELEC_3502', 'COM3', 2),    --Logement 2 pièce 3
    (4, 1, 'TEMP_2VC23', 'COM12', 2),   --Logement 2 pièce 4
    (3, 4, 'GAZ_20F28', 'COM11', 2),
    (4, 3, 'PRES_3D476', 'COM8', 2),
    (6, 5, 'LUM_481DF0', 'COM6', 2),    --Logement 2 pièce 6
    (6, 7, 'EAU_5DF634', 'COM13', 2);


-- Insertion des mesures
INSERT INTO Mesure (ID_Device, Valeur, ID_Logement)
VALUES
    (1, 2.3, 1),
    (2, 22.0, 1),
    (3, 50.0, 2),
    (4, 1.0, 2),
    (5, 300.0, 1);

-- Insertion des factures
INSERT INTO Facture (ID_Logement, Type_facture, Date_facture, Montant, Valeur_consommée)
VALUES
    (1, 'Électricité', '2024-01-15', 90.50, 250.0),
    (1, 'Eau', '2024-02-01', 45.00, 15.0),
    (2, 'Gaz', '2024-02-15', 65.00, 50.0),
    (2, 'Électricité', '2024-01-10', 110.00, 300.0),
    (1, 'Électricité', '2024-01-20', 95.00, 280.0),
    (2, 'Déchets', '2024-02-10', 20.00, 0.0);
