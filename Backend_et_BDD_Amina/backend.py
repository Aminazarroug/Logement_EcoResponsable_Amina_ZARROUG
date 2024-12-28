#Importation des bibliothèques nécessaires 
from fastapi import FastAPI, HTTPException, Query, File, UploadFile
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

#Création de l'application FastAPI
app = FastAPI() 

# Middleware CORS pour gérer les requêtes préflight et autoriser les origines croisées
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

#********************************************************************************************************
# LOGIN
#********************************************************************************************************

# Modèle pour les données de connexion
class LoginRequest(BaseModel):
    email: str
    password: str

# Fonction pour se connecter à la base de données SQLite
def get_db_connection():
    conn = sqlite3.connect("Amina.db")
    conn.row_factory = sqlite3.Row
    return conn

# Route POST pour authentifier l'utilisateur et récupérer les informations du logement
@app.post("/login")
def login(request: LoginRequest):
    """
    Authentifie un utilisateur avec son email et mot de passe.
    Retourne les détails du logement associé  si l'authentification est réussie.
    """
    conn = get_db_connection()
    try:
        # Requête pour vérifier les identifiants et récupérer les données du logement
        query = """
        SELECT ID_Logement, Adresse, Téléphone, Adresse_IP, Date_Insertion 
        FROM Logement 
        WHERE adresse_email = ? AND mot_de_passe = ?
        """
        logement = conn.execute(query, (request.email, request.password)).fetchone()

        if not logement:
            raise HTTPException(status_code=401, detail="Email ou mot de passe invalide")

        # Chemin de l'image du logement
        image_path = f'/public/{logement["ID_Logement"]}.png'


        return {
            "message": "Connexion réussie",
            "logement": {
                "ID_Logement": logement["ID_Logement"],
                "Adresse": logement["Adresse"],
                "Téléphone": logement["Téléphone"],
                "Adresse_IP": logement["Adresse_IP"],
                "Date_Insertion": logement["Date_Insertion"],
                "Image": image_path,
            }
        }
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()



#********************************************************************************************************
# DEVICES
#********************************************************************************************************


@app.post("/devices")
def get_devices(request: LoginRequest):
    """
    Récupère les capteurs associés au logement de l'utilisateur.
    """
    conn = get_db_connection()
    try:
        # Vérifier les identifiants et récupérer l'ID du logement
        logement_query = """
        SELECT ID_Logement 
        FROM Logement 
        WHERE adresse_email = ? AND mot_de_passe = ?
        """
        logement = conn.execute(logement_query, (request.email, request.password)).fetchone()

        if not logement:
            raise HTTPException(status_code=401, detail="Email ou mot de passe invalide")

        # Récupérer les capteurs associés aux pièces du logement
        devices_query = """
        SELECT 
            Device.ID_Device,
            Device_TYPE.Nom_Type,
            Device.Référence_commerciale,
            Device.Port_communication,
            (CASE WHEN MAX(Mesure.Valeur) > 0 THEN 1 ELSE 0 END) AS Etat
        FROM Device
        INNER JOIN Pièce ON Device.ID_Pièce = Pièce.ID_Pièce
        INNER JOIN Device_TYPE ON Device.ID_Type = Device_TYPE.ID_Type
        LEFT JOIN Mesure ON Device.ID_Device = Mesure.ID_Device
        WHERE Pièce.ID_Logement = ?
        GROUP BY Device.ID_Device
        """
        devices = conn.execute(devices_query, (logement["ID_Logement"],)).fetchall()

        return {
            "devices": [
                {
                    "ID_Device": device["ID_Device"],
                    "Nom_Type": device["Nom_Type"],
                    "Référence_commerciale": device["Référence_commerciale"],
                    "Port_communication": device["Port_communication"],
                    "Etat": device["Etat"],
                }
                for device in devices
            ]
        }
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()

# Route OPTIONS pour gérer les requêtes preflight
@app.options("/{full_path:path}")
def preflight_handler():
    """
    Gère les requêtes OPTIONS pour les vérifications CORS (préflight).
    """
    return {"message": "Préflight CORS handled"}


# Route pour récupérer la liste des types de capteurs (exclut les actionneurs)
@app.get("/capteurs/types")
def get_sensor_types():
    conn = get_db_connection()
    try:
        query = """
        SELECT DISTINCT Device_TYPE.Nom_Type
        FROM Device_TYPE
        WHERE Device_TYPE.Nom_Type NOT IN ('Volet') -- Exclut les actionneurs
        """
        types = conn.execute(query).fetchall()
        return {"types": [row["Nom_Type"] for row in types]}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()


#********************************************************************************************************
# MESURES
#********************************************************************************************************


# Route pour récupérer les mesures selon le type de capteur et la période
@app.get("/consommation")
def get_measurements(
    type_capteur: str = Query(..., description="Type de capteur à filtrer"),
    periode: str = Query(..., description="Période de la consommation : annuelle, mensuelle, hebdomadaire")
):
    conn = get_db_connection()
    try:
        # Vérifier si le type de capteur existe
        type_query = "SELECT COUNT(*) FROM Device_TYPE WHERE Nom_Type = ?"
        type_exists = conn.execute(type_query, (type_capteur,)).fetchone()[0]

        if not type_exists:
            raise HTTPException(status_code=400, detail=f"Type de capteur '{type_capteur}' non trouvé.")

        # Récupérer les mesures filtrées par type de capteur
        if periode == "annuelle":
            # Grouper les mesures par année
            query = """
            SELECT 
                strftime('%Y', Mesure.Date_Insertion) AS Periode,
                AVG(Mesure.Valeur) AS Consommation
            FROM Mesure
            INNER JOIN Device ON Mesure.ID_Device = Device.ID_Device
            INNER JOIN Device_TYPE ON Device.ID_Type = Device_TYPE.ID_Type
            WHERE Device_TYPE.Nom_Type = ?
            GROUP BY strftime('%Y', Mesure.Date_Insertion)
            ORDER BY Periode
            """
        elif periode == "mensuelle":
            # Grouper les mesures par mois
            query = """
            SELECT 
                strftime('%Y-%m', Mesure.Date_Insertion) AS Periode,
                AVG(Mesure.Valeur) AS Consommation
            FROM Mesure
            INNER JOIN Device ON Mesure.ID_Device = Device.ID_Device
            INNER JOIN Device_TYPE ON Device.ID_Type = Device_TYPE.ID_Type
            WHERE Device_TYPE.Nom_Type = ?
            GROUP BY strftime('%Y-%m', Mesure.Date_Insertion)
            ORDER BY Periode
            """
        elif periode == "hebdomadaire":
            # Grouper les mesures par semaine
            query = """
            SELECT 
                strftime('%Y-W%W', Mesure.Date_Insertion) AS Periode,
                AVG(Mesure.Valeur) AS Consommation
            FROM Mesure
            INNER JOIN Device ON Mesure.ID_Device = Device.ID_Device
            INNER JOIN Device_TYPE ON Device.ID_Type = Device_TYPE.ID_Type
            WHERE Device_TYPE.Nom_Type = ?
            GROUP BY strftime('%Y-W%W', Mesure.Date_Insertion)
            ORDER BY Periode
            """
        else:
            raise HTTPException(status_code=400, detail="Période invalide. Utilisez 'annuelle', 'mensuelle' ou 'hebdomadaire'.")

        results = conn.execute(query, (type_capteur,)).fetchall()
        return {
            "type_capteur": type_capteur,
            "periode": periode,
            "donnees": [{"periode": row["Periode"], "consommation": row["Consommation"]} for row in results],
        }
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()
    
    
#********************************************************************************************************
# ECONOMIES
#********************************************************************************************************

    
@app.get("/economies/consommation")
def get_economies_consommation(date: str, periode: str = Query("mensuelle", description="Période d'analyse")):
    """
    Retourne la consommation moyenne pour un mois donné (électricité, eau, gaz),
    comparée à la moyenne de toute la période précédente.
    """
    conn = get_db_connection()
    try:
        # Types de capteurs à inclure
        types_inclus = ["Électricité", "Eau", "Gaz"]
        prix_unitaire = {
            "Électricité": 0.15,  # €/kWh
            "Eau": 0.0025,       # €/litre
            "Gaz": 0.8           # €/m³
        }

        # Moyenne actuelle pour le mois sélectionné
        consommation_actuelle_query = f"""
        SELECT 
            Device_TYPE.Nom_Type AS Type,
            AVG(Mesure.Valeur) AS Moyenne
        FROM Mesure
        INNER JOIN Device ON Mesure.ID_Device = Device.ID_Device
        INNER JOIN Device_TYPE ON Device.ID_Type = Device_TYPE.ID_Type
        WHERE strftime('%Y-%m', Mesure.Date_Insertion) = ?
        AND Device_TYPE.Nom_Type IN ({",".join(["?" for _ in types_inclus])})
        GROUP BY Device_TYPE.Nom_Type
        """
        consommation_actuelle = conn.execute(consommation_actuelle_query, (date, *types_inclus)).fetchall()

        # Moyenne pour toutes les données avant le mois sélectionné
        consommation_periode_precedente_query = f"""
        SELECT 
            Device_TYPE.Nom_Type AS Type,
            AVG(Mesure.Valeur) AS Moyenne
        FROM Mesure
        INNER JOIN Device ON Mesure.ID_Device = Device.ID_Device
        INNER JOIN Device_TYPE ON Device.ID_Type = Device_TYPE.ID_Type
        WHERE strftime('%Y-%m', Mesure.Date_Insertion) < ?
        AND Device_TYPE.Nom_Type IN ({",".join(["?" for _ in types_inclus])})
        GROUP BY Device_TYPE.Nom_Type
        """
        consommation_periode_precedente = conn.execute(consommation_periode_precedente_query, (date, *types_inclus)).fetchall()

        # Calcul des économies
        result = {}
        for actuel in consommation_actuelle:
            type_capteur = actuel["Type"]
            moyenne_actuelle = actuel["Moyenne"] or 0
            moyenne_periode_precedente = next(
                (item["Moyenne"] for item in consommation_periode_precedente if item["Type"] == type_capteur), 0
            )
            economie_consommation = moyenne_periode_precedente - moyenne_actuelle
            economie_financiere = economie_consommation * prix_unitaire[type_capteur]


            result[type_capteur] = {
                "moyenne_actuelle": round(moyenne_actuelle, 2),
                "moyenne_periode_precedente": round(moyenne_periode_precedente, 2),
                "economie_consommation": round(economie_consommation, 2),
                "economie_financiere": round(economie_financiere, 2)
            }

        return {"date": date, "periode": periode, "economies": result}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()


#********************************************************************************************************
# AJOUT ET SUPRESSION DE DEVICES
#********************************************************************************************************

class DeviceRequest(BaseModel):
    id_piece: int
    id_type: int
    reference_commerciale: str
    port_communication: str

class DeviceDeleteRequest(BaseModel):
    id_device: int

# Route pour ajouter un capteur
@app.post("/devices/add")
def add_device(request: DeviceRequest):
    """
    Ajoute un nouveau capteur dans la base de données.
    """
    conn = get_db_connection()
    try:
        # Validation pour vérifier si la pièce et le type de capteur existent
        piece_exists = conn.execute("SELECT COUNT(*) FROM Pièce WHERE ID_Pièce = ?", (request.id_piece,)).fetchone()[0]
        type_exists = conn.execute("SELECT COUNT(*) FROM Device_TYPE WHERE ID_Type = ?", (request.id_type,)).fetchone()[0]

        if not piece_exists:
            raise HTTPException(status_code=400, detail=f"Pièce avec ID {request.id_piece} non trouvée.")
        if not type_exists:
            raise HTTPException(status_code=400, detail=f"Type de capteur avec ID {request.id_type} non trouvé.")

        # Insertion du capteur dans la base de données
        query = """
        INSERT INTO Device (ID_Pièce, ID_Type, Référence_commerciale, Port_communication)
        VALUES (?, ?, ?, ?)
        """
        conn.execute(query, (request.id_piece, request.id_type, request.reference_commerciale, request.port_communication))
        conn.commit()

        return {"message": "Capteur ajouté avec succès"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()

# Route pour supprimer un capteur
@app.delete("/devices/delete")
def delete_device(request: DeviceDeleteRequest):
    """
    Supprime un capteur de la base de données.
    """
    conn = get_db_connection()
    try:
        # Vérifier si le capteur existe avant de le supprimer
        device_exists = conn.execute("SELECT COUNT(*) FROM Device WHERE ID_Device = ?", (request.id_device,)).fetchone()[0]

        if not device_exists:
            raise HTTPException(status_code=404, detail=f"Capteur avec ID {request.id_device} non trouvé.")

        # Suppression du capteur
        query = "DELETE FROM Device WHERE ID_Device = ?"
        conn.execute(query, (request.id_device,))
        conn.commit()

        return {"message": f"Capteur avec ID {request.id_device} supprimé avec succès"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()

# Route pour récupérer les types de capteurs
@app.get("/devices/types")
def get_device_types():
    """
    Retourne la liste des types de capteurs disponibles.
    """
    conn = get_db_connection()
    try:
        query = "SELECT ID_Type, Nom_Type FROM Device_TYPE"
        types = conn.execute(query).fetchall()

        if not types:
            return {"types": []}  # Retourne une liste vide si aucun type n'est trouvé

        return {"types": [{"id_type": row["ID_Type"], "nom_type": row["Nom_Type"]} for row in types]}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()


#********************************************************************************************************
# NOUVEAU LOGEMENT
#********************************************************************************************************


class SimpleLogementRequest(BaseModel):
    adresse: str
    telephone: str
    adresse_ip: str
    adresse_email: str
    mot_de_passe: str
    
@app.post("/logements")
def create_logement(logement: SimpleLogementRequest):
    """
    Insère un nouveau logement 
    """
    conn = get_db_connection()
    try:
        # Insertion des données dans la table Logement
        query = """
        INSERT INTO Logement (Adresse, Téléphone, Adresse_IP, adresse_email, mot_de_passe)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor = conn.execute(
            query,
            (
                logement.adresse,
                logement.telephone,
                logement.adresse_ip,
                logement.adresse_email,
                logement.mot_de_passe,
            ),
        )
        conn.commit()

        # Récupérer l'ID du logement nouvellement créé 
        logement_id = cursor.lastrowid 

        return {"message": "Logement créé avec succès", "id_logement": logement_id}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur de base de données : {str(e)}")
    finally:
        conn.close()
