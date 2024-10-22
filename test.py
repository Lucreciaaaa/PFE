import json

# Charger le fichier JSON
with open('3cf596e2bcc34862abc89bd2eca4a985.json') as file:
    data = json.load(file)

# Extraire les métadonnées du participant
participant_info = data.get("participant", {})
GUID = data.get("GUID", "N/A")
age = participant_info.get("age", "N/A")
gender = participant_info.get("gender", "N/A")
fitzpatrick = participant_info.get("fitzpatrick", "N/A")

# Extraire la série temporelle PPG pour un scénario
scenarios = data.get("scenarios", [])
if scenarios:
    ppg_timeseries = scenarios[0]["recordings"]["ppg"]["timeseries"]  # Prendre le premier scénario

    # Calculer les différences de temps et de valeurs PPG
    time_differences = []
    ppg_differences = []

    for i in range(1, len(ppg_timeseries)):
        time_diff = ppg_timeseries[i][0] - ppg_timeseries[i-1][0]
        ppg_diff = ppg_timeseries[i][1] - ppg_timeseries[i-1][1]
        time_differences.append(time_diff)
        ppg_differences.append(ppg_diff)

    # Afficher les 5 premiers points de la série temporelle avec les différences
    print("Premiers points de la série temporelle PPG avec différences :")
    for i in range(5):
        print(f"Temps écoulé : {ppg_timeseries[i][0]} ms, Valeur PPG : {ppg_timeseries[i][1]}, "
              f"Diff. de temps / Période temporelle : {time_differences[i] if i < len(time_differences) else 'N/A'} ms, "
              f"Diff. PPG : {ppg_differences[i] if i < len(ppg_differences) else 'N/A'}")
else:
    print("Aucun scénario disponible")

# Afficher les métadonnées du participant
print(f"\nGUID : {GUID}")
print(f"Âge : {age}")
print(f"Genre : {gender}")
print(f"Type de peau Fitzpatrick : {fitzpatrick}")
