import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Tracer les graphiques
plt.plot(x, y1, label='Données 1', color='blue', marker='o')
plt.plot(x, y2, label='Données 2', color='red', marker='s')

# Titres et légendes
plt.title('Graphique avec légende et titres')
plt.xlabel('Axe des abscisses')
plt.ylabel('Axe des ordonnées')
plt.legend()

# Personnalisation des échelles
plt.xlim(0, 6)  # Limite de l'axe des abscisses
plt.ylim(0, 50) # Limite de l'axe des ordonnées

# Ajout de grille
plt.grid(True)  # Activer la grille


# Annotation
plt.text(3, 6, 'Point important', fontsize=10, color='green')

# Afficher le graphique
plt.show()
