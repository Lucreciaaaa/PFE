import json
import matplotlib.pyplot as plt



# Chemin du fichier JSON
json_file_path = 'patient1_data.json'


# Extraire et reconstruire le signal PPG
def extract_ppg_signal(json_file_path):
    # Charger le fichier JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Vérifier si le fichier contient des scénarios et des enregistrements PPG
    if 'scenarios' in data and len(data['scenarios']) > 0:
        # Extraire les données PPG du premier scénario
        ppg_data = data['scenarios'][0]['recordings']['ppg']['timeseries']

        # Séparer le temps écoulé et les valeurs PPG
        times = [entry[0] for entry in ppg_data]
        ppg_values = [entry[1] for entry in ppg_data]

        # Retourner les données de la série temporelle PPG
        return times, ppg_values
    else:
        print("Aucun scénario ou données PPG trouvés dans le fichier JSON.")
        return None, None


# Calculer la fréquence d'échantillonnage, la période, l'amplitude
def calculate_ppg_stats(times, ppg_values):
    # Fréquence d'échantillonnage en Hz (nombre d'échantillons par seconde)
    sampling_interval = (times[-1] - times[0]) / len(times)  # Calculer l'intervalle moyen
    sampling_frequency = 1000 / sampling_interval  # Conversion de ms à s pour obtenir la fréquence en Hz
    period = 1 / sampling_frequency  # Période en secondes

    # Calcul de l'amplitude max et min
    max_amplitude = max(ppg_values)
    min_amplitude = min(ppg_values)

    return sampling_frequency, period, max_amplitude, min_amplitude


# Tracer le signal PPG
def plot_ppg_signal(times, ppg_values):
    plt.figure(figsize=(10, 5))
    plt.plot(times, ppg_values, label="PPG Signal")
    plt.title('Photoplethysmogram (PPG) Signal')
    plt.xlabel('Time (ms)')
    plt.ylabel('PPG Value')
    plt.legend()
    plt.grid(True)
    plt.show()



# Extraire et reconstruire le signal PPG
times, ppg_values = extract_ppg_signal(json_file_path)

# Si des données PPG sont trouvées, tracer le signal et calculer les statistiques
if times and ppg_values:
    plot_ppg_signal(times, ppg_values)

    # Calculer et afficher les statistiques du signal PPG
    sampling_frequency, period, max_amplitude, min_amplitude = calculate_ppg_stats(times, ppg_values)
    print(f"Fréquence d'échantillonnage : {sampling_frequency:.2f} Hz")
    print(f"Période : {period:.4f} secondes")
    print(f"Amplitude maximale : {max_amplitude}")
    print(f"Amplitude minimale : {min_amplitude}")
