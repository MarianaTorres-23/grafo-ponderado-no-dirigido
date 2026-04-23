import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, pos, title):
    plt.figure(figsize=(10,6))
    
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1800)
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)
    
    plt.title(title)
    plt.axis('off')
    plt.show()


estados = {
    "Aguascalientes": 11,
    "Baja California": 7,
    "Baja California Sur": 5,
    "Campeche": 13,
    "Chiapas": 124,
    "Chihuahua": 67,
    "Ciudad de Mexico": 16,
    "Coahuila": 38,
    "Colima": 10,
    "Durango": 39,
    "Guanajuato": 46,
    "Guerrero": 85,
    "Hidalgo": 84,
    "Jalisco": 125,
    "Mexico": 125,
    "Michoacan": 113,
    "Morelos": 36,
    "Nayarit": 20,
    "Nuevo Leon": 51,
    "Oaxaca": 570,
    "Puebla": 217,
    "Queretaro": 18,
    "Quintana Roo": 11,
    "San Luis Potosi": 58,
    "Sinaloa": 18,
    "Sonora": 72,
    "Tabasco": 17,
    "Tamaulipas": 43,
    "Tlaxcala": 60,
    "Veracruz": 212,
    "Yucatan": 106,
    "Zacatecas": 58
}

ordenados = sorted(estados.items(), key=lambda x: x[1])
print("Estados ordenados:", ordenados)


G = nx.Graph()

municipios = [
    "Balancan","Cardenas","Centla","Centro","Comalcalco","Cunduacan",
    "Emiliano Zapata","Huimanguillo","Jalapa","Jalpa de Mendez",
    "Jonuta","Macuspana","Nacajuca","Paraiso","Tacotalpa","Teapa","Tenosique"
]

G.add_nodes_from(municipios)


G.add_edge("Centro","Nacajuca", weight=20)
G.add_edge("Centro","Jalpa de Mendez", weight=30)
G.add_edge("Centro","Macuspana", weight=50)
G.add_edge("Centro","Jalapa", weight=35)
G.add_edge("Centro","Cunduacan", weight=40)

G.add_edge("Nacajuca","Jalpa de Mendez", weight=15)
G.add_edge("Jalpa de Mendez","Comalcalco", weight=25)
G.add_edge("Comalcalco","Paraiso", weight=20)

G.add_edge("Cunduacan","Comalcalco", weight=18)
G.add_edge("Cunduacan","Cardenas", weight=30)

G.add_edge("Cardenas","Huimanguillo", weight=45)

G.add_edge("Macuspana","Tacotalpa", weight=40)
G.add_edge("Tacotalpa","Teapa", weight=15)
G.add_edge("Teapa","Jalapa", weight=20)

G.add_edge("Macuspana","Jonuta", weight=60)
G.add_edge("Jonuta","Balancan", weight=50)
G.add_edge("Balancan","Tenosique", weight=30)
G.add_edge("Tenosique","Emiliano Zapata", weight=70)


print("Cantidad de nodos:", G.number_of_nodes())
print("Cantidad de aristas:", G.number_of_edges())
print("Lista de aristas:", list(G.edges(data=True)))


pos = {
    "Huimanguillo": (0,2),
    "Cardenas": (1,2.2),
    "Comalcalco": (2,2.3),
    "Paraiso": (3,2.2),

    "Cunduacan": (1.5,1.7),
    "Jalpa de Mendez": (2.5,1.7),

    "Nacajuca": (2.2,1.2),
    "Centro": (3,1.2),
    "Centla": (4,2),

    "Jalapa": (3.8,0.9),
    "Teapa": (4.2,0.6),
    "Tacotalpa": (4.8,0.3),

    "Macuspana": (4.2,1.3),

    "Jonuta": (5.5,1.8),
    "Balancan": (6.8,1.8),
    "Tenosique": (7.8,1.3),
    "Emiliano Zapata": (6.8,0.7)
}


draw_graph(G, pos, "Grafo de Municipios de Tabasco")