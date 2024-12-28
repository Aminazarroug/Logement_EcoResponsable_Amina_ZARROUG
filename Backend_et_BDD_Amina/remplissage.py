import sqlite3
import random
from datetime import datetime, timedelta

# Connexion à la base de données SQLite
db_path = "Amina.db"  
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Générer une date aléatoire dans une plage donnée
def generate_date(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    random_date = start + timedelta(days=random.randint(0, (end - start).days))
    return random_date.strftime("%Y-%m-%d %H:%M:%S")  # Format avec horodatage complet

# Générer une valeur réaliste en fonction du type de capteur
def generate_value(type_name):
    if type_name == 'Température':
        return round(random.uniform(10, 40), 2)  # Température en °C
    elif type_name == 'Électricité':
        return round(random.uniform(1, 10), 2)  # Consommation en kWh
    elif type_name == 'Gaz':
        return round(random.uniform(200, 1000), 2)  # Consommation en ppm
    elif type_name == 'Lumière':
        return round(random.uniform(0, 1000), 2)  # Intensité lumineuse en Lux
    elif type_name == 'Eau':
        return round(random.uniform(0, 500), 2)  
    else:
        return 0  # Valeur par défaut

# Ajouter des mesures pour tous les capteurs d'un logement donné
def add_measurements_for_logement(logement_id, num_measurements=50):
    query = """
        SELECT Device.ID_Device, Device_TYPE.Nom_Type
        FROM Device
        JOIN Device_TYPE ON Device.ID_Type = Device_TYPE.ID_Type
        WHERE Device.ID_Logement = ?
    """
    c.execute(query, (logement_id,))
    sensors = c.fetchall()

    if not sensors:
        print(f"Aucun capteur trouvé pour le logement {logement_id}.")
        return

    print(f"{len(sensors)} capteurs trouvés pour le logement {logement_id}. Ajout des mesures...")

    for sensor_id, type_name in sensors:
        for _ in range(num_measurements):
            value = generate_value(type_name)
            date = generate_date("2020-01-01", "2024-12-31")
            c.execute(
                "INSERT INTO Mesure (ID_Device, Valeur, Date_Insertion) VALUES (?, ?, ?)",
                (sensor_id, value, date)
            )
            print(f"Mesure ajoutée : ID_Device={sensor_id}, Type={type_name}, Valeur={value}, Date={date}")

# Script principal
def main():
    query = "SELECT ID_Logement FROM Logement"
    c.execute(query)
    logements = [row[0] for row in c.fetchall()]

    if not logements:
        print("Aucun logement trouvé dans la base de données.")
        return

    for logement_id in logements:
        print(f"Traitement des mesures pour le logement {logement_id}...")
        add_measurements_for_logement(logement_id)

    conn.commit()
    print("Données insérées avec succès dans la table Mesure.")

# Exécuter le script
if __name__ == "__main__":
    main()
    conn.close()
