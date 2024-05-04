import matplotlib.pyplot as plt

def read_malicious_rates(file_path):
    counters = []
    rates = []
    with open(file_path, "r") as file:
        for line in file:
            counter, rate = line.strip().split(" : ")
            counters.append(int(counter))
            rates.append(float(rate))
    return counters, rates

def plot_malicious_rates(counters, rates):
    plt.figure(figsize=(10, 6))
    plt.plot(counters, rates,linestyle='-', color='b');""" marker='o',""" 
    plt.title("Rate of Malicious Nodes in Views Over Time")
    plt.xlabel("Counter")
    plt.ylabel("Rate of Malicious Nodes (%)")
    plt.grid(True)
    # Sauvegardez le graphique au lieu de l'afficher
    plt.savefig("/mnt/c/Users/LENOVO/Desktop/Projet S8/tests/malicious_rates_plot.png")
    plt.show()


file_path = "rates.txt"  # Assurez-vous que le chemin correspond à votre fichier de données

# Lire les données
counters, rates = read_malicious_rates(file_path)

# Tracer le graphe
plot_malicious_rates(counters, rates)
