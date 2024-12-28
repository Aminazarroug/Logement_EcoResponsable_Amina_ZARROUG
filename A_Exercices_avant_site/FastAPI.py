from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from fastapi.responses import HTMLResponse

app = FastAPI()

# --- Modèles de validation pour les requêtes POST ---
class Logement(BaseModel):
    Adresse: str
    Téléphone: str
    Adresse_IP: str

class Piece(BaseModel):
    Nom: str
    Localisation_X: float
    Localisation_Y: float
    Localisation_Z: float
    ID_Logement: int

class Mesure(BaseModel):
    ID_Device: int
    Valeur: float
    Date_Insertion: str

class Facture(BaseModel):
    ID_Logement: int
    Type_facture: str
    Date_facture: str
    Montant: float
    Valeur_consommée: float

# --- Fonctions de base pour se connecter à SQLite ---
def get_db_connection():
    conn = sqlite3.connect("Amina.db")
    conn.row_factory = sqlite3.Row  # Pour retourner les données sous forme de dictionnaire
    return conn

# --- Endpoints pour Logement ---
@app.get("/logements")
def get_logements():
    conn = get_db_connection()
    logements = conn.execute("SELECT * FROM Logement").fetchall()
    conn.close()
    return [dict(logement) for logement in logements]

@app.post("/logements")
def create_logement(logement: Logement):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Logement (Adresse, Téléphone, Adresse_IP) VALUES (?, ?, ?)",
        (logement.Adresse, logement.Téléphone, logement.Adresse_IP),
    )
    conn.commit()
    conn.close()
    return {"message": "Logement ajouté avec succès"}

# --- Endpoints pour Pièce ---
@app.get("/pieces")
def get_pieces():
    conn = get_db_connection()
    pieces = conn.execute("SELECT * FROM Pièce").fetchall()
    conn.close()
    return [dict(piece) for piece in pieces]

@app.post("/pieces")
def create_piece(piece: Piece):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Pièce (Nom, Localisation_X, Localisation_Y, Localisation_Z, ID_Logement) VALUES (?, ?, ?, ?, ?)",
        (piece.Nom, piece.Localisation_X, piece.Localisation_Y, piece.Localisation_Z, piece.ID_Logement),
    )
    conn.commit()
    conn.close()
    return {"message": "Pièce ajoutée avec succès"}

# --- Endpoints pour Mesure ---
@app.get("/mesures")
def get_mesures():
    conn = get_db_connection()
    mesures = conn.execute("SELECT * FROM Mesure").fetchall()
    conn.close()
    return [dict(mesure) for mesure in mesures]

@app.post("/mesures")
def create_mesure(mesure: Mesure):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Mesure (ID_Device, Valeur, Date_Insertion) VALUES (?, ?, ?)",
        (mesure.ID_Device, mesure.Valeur, mesure.Date_Insertion),
    )
    conn.commit()
    conn.close()
    return {"message": "Mesure ajoutée avec succès"}

# --- Endpoints pour Facture ---
@app.get("/factures")
def get_factures():
    conn = get_db_connection()
    factures = conn.execute("SELECT * FROM Facture").fetchall()
    conn.close()
    return [dict(facture) for facture in factures]

@app.post("/factures")
def create_facture(facture: Facture):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Facture (ID_Logement, Type_facture, Date_facture, Montant, Valeur_consommée) VALUES (?, ?, ?, ?, ?)",
        (facture.ID_Logement, facture.Type_facture, facture.Date_facture, facture.Montant, facture.Valeur_consommée),
    )
    conn.commit()
    conn.close()
    return {"message": "Facture ajoutée avec succès"}

# --- Endpoint racine ---
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API RESTful pour la gestion des logements IoT"}


@app.get("/factures/chart", response_class=HTMLResponse)
def generate_pie_chart():
    # Connexion à la base de données
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Récupérer les types de factures et leurs montants totaux
    cursor.execute("""
        SELECT Type_facture, SUM(Montant) AS Total
        FROM Facture
        GROUP BY Type_facture
    """)
    factures = cursor.fetchall()
    conn.close()
    
    # Préparer les données pour Google Charts
    chart_data = [["Type de Facture", "Montant Total"]]
    for facture in factures:
        chart_data.append([facture["Type_facture"], facture["Total"]])
    
    # Convertir les données en format JavaScript
    chart_data_js = str(chart_data).replace("'", '"')
    
    # Générer le HTML avec Google Charts
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
            google.charts.load('current', {{'packages':['corechart']}});
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {{
                var data = google.visualization.arrayToDataTable({chart_data_js});

                var options = {{
                    title: 'Répartition des Factures',
                    is3D: true,
                }};

                var chart = new google.visualization.PieChart(document.getElementById('piechart'));

                chart.draw(data, options);
            }}
        </script>
    </head>
    <body>
        <h1>Répartition des Factures</h1>
        <div id="piechart" style="width: 900px; height: 500px;"></div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
